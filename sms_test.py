from twilio.rest import Client
from os import environ as env

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = env.get('TWILIO_SID')
auth_token = env.get('TWILIO_AUTH')
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='insert_text_here',
                              from_='+12565810321',
                              to='+17089969412'
                          )

print(message.sid)