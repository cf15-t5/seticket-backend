from  src.server.main import main_app, DEBUG, BASE_URL, PORT
from src.routes.main import routes

for route in routes:
  main_app.register_blueprint(route["name"], url_prefix=route["url"])

print("Server is running on url: "+ BASE_URL +":", PORT)
if(__name__ == "__main__"):
  main_app.run(debug=DEBUG, host=BASE_URL, port=PORT)  