import string
from src.config.permission import permissions
def check_role_is_have_access(role:string,path:string):
    print(role,path,permissions.get(role.lower(), []))
    return path in permissions.get(role.lower(), [])
  