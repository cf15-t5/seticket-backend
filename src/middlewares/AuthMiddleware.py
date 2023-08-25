from functools import wraps  #
import src.utils.jwt as jwt
import src.utils.getResponse as response
from flask import request, g, jsonify
from src.repositories.UserRepository import UserRepository
from src.utils.permission import check_role_is_have_access
from src.utils.convert import queryResultToDict

user_repository = UserRepository()


def isAuthenticated(func):
    @wraps(func)  # Apply the wraps decorator
    def wrapper(*args, **kwargs):
        if request.headers.get("Authorization") is None:
            return response.error(message="Unauthorized", errors=None, status_code=401)
        else:
            auth_header = request.headers.get("Authorization")
            if auth_header is not None:
                token = auth_header.split(" ")[1]
            else:
                return response.error(
                    message="Missing Authorization Header", errors=None, status_code=401
                )
            try:
                decode = jwt.decode(token)
                user = user_repository.getUserById(decode["user_id"])
                is_have_access = check_role_is_have_access(user.role, request.path)
                if not is_have_access:
                    return response.error(
                        message="Forbidden", errors=None, status_code=403
                    )
                g.user = queryResultToDict([user])[0]
                return func(*args, **kwargs)
            except jwt.jwt.InvalidKeyError as e:
                return response.error(
                    message="Unauthorized", errors=None, status_code=401
                )

    return wrapper


def isAdmin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user["role"] != "admin":
            return jsonify({"message": "Unauthorized access"}), 403
        return f(*args, **kwargs)

    return decorated_function
