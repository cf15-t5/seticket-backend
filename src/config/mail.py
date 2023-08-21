from flask_mail import Mail
from src.config.config import MAIL_PORT,MAIL_SERVER,MAIL_USE_SSL,MAIL_USE_TLS,MAIL_USERNAME,MAIL_PASSWORD
def mailConfig(app):
  app.config['MAIL_SERVER']= 'sandbox.smtp.mailtrap.io'
  app.config['MAIL_PORT'] = 2525
  app.config['MAIL_USE_TLS'] = True
  app.config['MAIL_USE_SSL'] = False
  app.config['MAIL_USERNAME'] = '1190969a29319c'
  app.config['MAIL_PASSWORD'] = '39c02575b88bd3'
  return  Mail(app)
  

# MAIL_SERVER='sandbox.smtp.mailtrap.io'
# MAIL_PORT = 2525
# MAIL_USERNAME = '1190969a29319c'
# MAIL_PASSWORD = '39c02575b88bd3'
# MAIL_USE_TLS = True
# MAIL_USE_SSL = False