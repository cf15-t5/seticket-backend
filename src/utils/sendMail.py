from flask_mail import Message
from flask import render_template
from src.server.main import mail
from datetime import datetime
def sendMail(to,subject,code,event_name,location, date:datetime,name):
    # split date and time 
    event_date = date.strftime("%d %B %Y")
    event_time = date.strftime("%H:%M")
    templates = render_template('html/mail.html',code=code,event_name=event_name,location=location,name=name, date=event_date,time=event_time)
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