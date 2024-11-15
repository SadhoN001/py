# dip-------------->
class notificationservice:
     def send(self,msg):
          pass
 
class Emailservice:
     def send(self,msg):
          print(f"sending email: {msg}")

class notification:
     def __init__(self,service:notificationservice):
          self.service=service
     def notify(self,msg):
          self.service.send(msg)
          
email_service=Emailservice()

notification=notification(email_service)
notification.notify("hello")