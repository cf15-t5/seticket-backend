from flask_mail import Message
from src.server.main import mail
from datetime import datetime
def sendMail(to,subject,templates):
    # split date and time 
   
    msg = Message(
      subject,
      recipients=[to],
      html=templates,
      sender="Ticket@gmail.com"
    )
    try:
      print("sending mail")
      mail.send(msg)
      return True
    except Exception as e:
      print(e)
      print("failed to send mail : ",e.with_traceback)
      return False