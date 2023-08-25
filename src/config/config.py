from dotenv import dotenv_values

env = dotenv_values(".env")
BASE_URL = env["BASE_URL"] or "http://localhost"
PORT = env["PORT"] or 5000
DEBUG = env["DEBUG"] or True

DATABASE_URL = env["DATABASE_URL"] or "mysq;://root:root@localhost:3306/se_ticket"

JWT_ACCESS_TOKEN_EXPIRES = env["JWT_ACCESS_TOKEN_EXPIRES"] or 60 * 60 * 24 * 7
JWT_ACCESS_TOKEN_SECRET = env["JWT_ACCESS_TOKEN_SECRET"] or "secret"
JWT_ACCESS_TOKEN_ALGORITHM = env["JWT_ACCESS_TOKEN_ALGORITHM"] or "HS256"


MAIL_SERVER = env["MAIL_SERVER"] or "sandbox.smtp.mailtrap.io"
MAIL_PORT = env["MAIL_PORT"] or 2525
MAIL_USE_TLS = env["MAIL_USE_TLS"] or True
MAIL_USE_SSL = env["MAIL_USE_SSL"] or False
MAIL_USERNAME = env["MAIL_USERNAME"] or "1190969a29319c"
MAIL_PASSWORD = env["MAIL_PASSWORD"] or "39c02575b88bd3"
