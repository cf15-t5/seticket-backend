import string
from src.config.permission import permissions
def check_role_is_have_access(role:string,path:string):
    return path in permissions.get(role.lower(), [])
  