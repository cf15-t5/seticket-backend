import string
import fnmatch
from src.config.permission import permissions


def check_role_is_have_access(role: str, path: str):
    return any(
        fnmatch.fnmatch(path, pattern)
        if not pattern.startswith("!")
        else not fnmatch.fnmatch(path, pattern[1:])
        for pattern in permissions.get(role.lower(), [])
    )
