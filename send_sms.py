from twilio.rest import Client 
from credentials import *

client = Client(account_sid, auth_token) 


message = client.messages.create( 
                              from_='+19782082449',  
                              body='how are you?',      
                              to='+15555555555' 
                              # enter phone number to send message to here
                          ) 

# print(message.sid)


