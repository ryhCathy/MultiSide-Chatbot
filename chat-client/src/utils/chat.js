
class Chat{
    constructor(){
        // 当前登录的用户
        this._user = null;
        // 会话数组
        this._sessions = []; // user,messages,unread
        // 当前的会话
        this._current_session = null;
    }

    setUser(user){
        this._user = user;
    }

    get user(){
        return this._user;
    }

    get sessions(){
        return this._sessions;
    }

    get logined(){
        if(this._user){
            return true;
        }else{
            return false;
        }
    }

    addSession(user){ // initialized session info
        this._sessions.push({
            "user": user, // the user newly logged in user
            "messages": [],
            "unread": 0
        })
        console.log(this._sessions);
    }
}

export default new Chat()