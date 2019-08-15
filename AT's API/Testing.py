# works with both python 2 and 3
from __future__ import print_function

import africastalking
class SMS:
    def __init__(self):
        # Set your app credentials

        self.username="sandbox"
        self.api_key="20c1f645476cfd5178802fd1e1879e6d1339a9a179591b1de9305ba93bca628b"
        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
            # Set the numbers you want to send to in international format
            recipients = ["+25470085097", "+254722295983"]

            # Set your message
            message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"

            # Set your shortCode or senderId
            # sender = "shortCode or senderId"
            try:
                # Thats it, hit send and we'll take care of the rest.
                response = self.sms.send(message, recipients)
                print (response)
            except Exception as e:
                print ('Encountered an error while sending: %s' % str(e))

if __name__ == '__main__':
    SMS().send()