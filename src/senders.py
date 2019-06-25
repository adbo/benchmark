"""Module containing classes for sending text messages"""
import json
import smtplib, ssl

class SendToFile:
    """Class saving to file"""

    def send(self, message):
        #TODO - move to config file
        path = 'log.txt'

        with open(path, 'w') as handle:
            handle.write(message)


class ShowOnConsole:
    """Class showing text on console"""

    def send(self, message):
        """Print message to the console
        
        Args:
            message (str): text to show
        """
        print(message)


class SendWithEmail:
    """Class sending message with email"""

    def send(self, message):
        with open('config.json', 'r') as f:
            config = json.load(f)

        port = config['DEFAULT']['PORT']
        smtp_server = config['DEFAULT']['SMTP_SERVER']
        sender_email = config['DEFAULT']['SENDER_EMAIL']
        receiver_email = config['DEFAULT']['RECEIVER_EMAIL']
        password = config['DEFAULT']['PASSWORD']

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

class SendWithSms:
    """Class sending with sms. Dummy implementation"""

    def send(self, message):
        pass
