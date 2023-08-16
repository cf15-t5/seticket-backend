
import src.utils.jwt as jwt 
import src.utils.getResponse as response
from flask import request,g
def isAuthenticated():
  print('isAuthenticated')
  if(request.headers.get('Authorization') == None):
    return response.error(message="Unauthorized",errors=None,status_code=401)
  else:
    token = request.headers.get('Authorization').split(" ")[1]
    try:
      decode = jwt.decode(token)
      g.user= decode['user']
      return None
    except Exception as e:
      return response.error(message="Unauthorized",errors=None,status_code=401)