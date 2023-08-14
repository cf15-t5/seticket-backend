from dotenv import dotenv_values
env = dotenv_values(".env")
BASE_URL = env["BASE_URL"] or "http://localhost"
PORT= env['PORT'] or 5000
DEBUG= env['DEBUG'] or True
DATABASE_URL = env['DATABASE_URL'] or "mysq;://root:root@localhost:3306/se_ticket"
