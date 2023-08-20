from flask import Flask
from flask_cors import CORS
from src.config.config import BASE_URL, PORT, DEBUG
from src.config.database import database
main_app = Flask(__name__,static_folder='../../public', static_url_path='/')
CORS(main_app)
db = database(main_app)


print("Server is running on url: "+ BASE_URL +":", PORT)
if(__name__ == "__main__"):
  main_app.run(debug=DEBUG, host=BASE_URL, port=PORT)