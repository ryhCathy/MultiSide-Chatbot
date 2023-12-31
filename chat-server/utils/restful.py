# Restful API

class HttpCode(object):
  # 响应正常
  ok = 200
  # 没有登陆错误
  unloginerror = 401
  # 没有权限错误
  permissionerror = 403
  # 客户端参数错误
  paramserror = 400
  # 服务器错误
  servererror = 500


def _restful_result(code, message, data):
  return {"message": message or "", "data": data or {}, "code": code}


def ok(message=None, data=None):
  return _restful_result(code=HttpCode.ok, message=message, data=data)


def unlogin_error(message="Please Login"):
  return _restful_result(code=HttpCode.unloginerror, message=message, data=None)


def permission_error(message="Permission Error"):
  return _restful_result(code=HttpCode.permissionerror, message=message, data=None)


def params_error(message="Parameter Error"):
  return _restful_result(code=HttpCode.paramserror, message=message, data=None)


def server_error(message="Server Error"):
  return _restful_result(code=HttpCode.servererror, message=message or '服务器内部错误', data=None)
