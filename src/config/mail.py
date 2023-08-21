from flask_mail import Mail
from src.config.config import MAIL_PORT,MAIL_SERVER,MAIL_USE_SSL,MAIL_USE_TLS,MAIL_USERNAME,MAIL_PASSWORD
def mailConfig(app):
  print(MAIL_SERVER,MAIL_PORT,MAIL_USE_SSL,MAIL_USE_TLS,MAIL_USERNAME,MAIL_PASSWORD)
  print(type(MAIL_SERVER),type(MAIL_PORT),type(MAIL_USE_SSL),type(MAIL_USE_TLS),type(MAIL_USERNAME),type(MAIL_PASSWORD))
  app.config['MAIL_SERVER']= MAIL_SERVER
  app.config['MAIL_PORT'] = MAIL_PORT
  app.config['MAIL_USE_TLS'] = MAIL_USE_TLS == 'True'
  app.config['MAIL_USE_SSL'] = MAIL_USE_SSL == 'True'
  app.config['MAIL_USERNAME'] = MAIL_USERNAME
  app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
  return  Mail(app)
  