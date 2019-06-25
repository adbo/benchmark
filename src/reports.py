"""Module containing classes for reporting benchmarks"""
import smtplib, ssl

class ReportToFile:
    """Class reporting to file"""

    def report(self, message):
        #TODO - move to config file
        path = 'log.txt'

        with open(path, 'w') as handle:
            handle.write(message)


class ReportToConsole:
    """Class reporting to console"""

    def report(self, message):
        print(message)


class ReportToEmail:
    """Class reporting to email"""

    def report(self, message):
        pass

        # TODO: move to config file and uncomment
        # port = 465
        # smtp_server = "smtp.gmail.com"
        # sender_email = "my@gmail.com"
        # receiver_email = "your@gmail.com"
        # password = "password"

        # context = ssl.create_default_context()
        # with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        #     server.login(sender_email, password)
        #     server.sendmail(sender_email, receiver_email, message)

class ReportToSms:
    """Class reporting to sms. Dummy implementation"""

    def report(self, message):
        pass

