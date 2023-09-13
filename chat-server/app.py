from flask import Flask, request, send_from_directory, url_for, render_template
from flask_socketio import SocketIO, emit
from utils import restful
from flask_avatars import Avatars, Identicon
import os
from hashlib import md5
from flask_cors import CORS

# pip install gunicorn==20.1.0 eventlet==0.30.2 is working for me. Try this maybe.

BASE_DIR = os.path.dirname(__file__)

app = Flask(__name__)
# the path to save avatars
app.config['AVATARS_SAVE_PATH'] = os.path.join(BASE_DIR, "media", "avatars")

cors = CORS(app, resources={r"/socket.io/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

avatars = Avatars(app)

online_users = []


@app.route('/media/avatars/<path:filename>')
def get_avatar(filename):
    return send_from_directory(app.config['AVATARS_SAVE_PATH'], filename)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connect")
def connect():
    print("ip: " + request.remote_addr)  # current ip address
    print("sid: " + request.sid)  # sid randomly assigned by socketio: later for user


@socketio.on("disconnect")
def disconnect():    # need to be listened
    sid = request.sid
    for user in online_users:
        if user['sid'] == sid:
            online_users.remove(user)
            emit("friend offline", {"user": user}, broadcast=True)
            break


@socketio.on("login")  # name of the event: should be same as in the front-end
def login(data):
    username = data.get('username')
    if not username:
        return restful.params_error("Please enter username")
    for user in online_users:
        if user['username'] == username:
            return restful.params_error("Username already existed")

    filenames = Identicon().generate(md5(username.encode("utf-8")).hexdigest())
    # if use username, the file name will be username, so better encoding and hashing to md5
    avatar_name = filenames[2]
    # filenames[0]: small; [1]: median; [2]: large
    avatar_url = url_for("get_avatar", filename=avatar_name)
    # avatar_url = "/media/avatars/" + avatar_name
    user = {
        "username": username,
        "ip": request.remote_addr,
        "avatar": avatar_url,
        "sid": request.sid
    }
    users = online_users.copy()
    online_users.append(user)
    emit("friend online", {"user": user}, broadcast=True)
    # an event: "friend online"; content: the user logined
    # will be received by List in the front end
    return restful.ok(data={"user": user, "online_users": users})
    #print(user["username"])
    #return restful.ok(data=user)


@socketio.on("send message")
def send_message(data):
    # print("send message emitted")
    to = data.get('to')  # the target user that the user want to send message to
    # print(to)
    if not to:
        return restful.params_error("Please select the userID you want to connect")
    for user in online_users:  # find the user in the current user list
        # print("check user" + user['sid'])
        if user['sid'] == to:
            break
    else:
        return restful.params_error("User not existing or is not online")

    message = data.get('message')
    # print("message sent:" + message)
    if not message:
        return restful.params_error("Please enter message")
    emit("receive message", {"message": message, "from": request.sid}, room=[to])
    # print("emitted")
    # to: sid; if not specify room: will send to self
    return restful.ok()

# eventlet/gevent/uWsgi：WebSocket协议，有一个好处，只要客户端一断开连接，服务器就能立马收到disconnect事件
# Flask自带的服务器：长轮询，每隔大约5分钟的时间向客户端发送消息，来判断客户端是否断开连接

if __name__ == '__main__':
    socketio.run(app, debug=True, host="127.0.0.1")
