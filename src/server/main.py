from flask import Flask
from src.config.config import BASE_URL, PORT, DEBUG
from src.config.database import database
main_app = Flask(__name__)
db = database(main_app)


print("Server is running on url: "+ BASE_URL +":", PORT)
if(__name__ == "__main__"):
  main_app.run(debug=DEBUG, host=BASE_URL, port=PORT)