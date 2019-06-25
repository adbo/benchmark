import datetime

class Formater:

    def format(self, report):
        return f'\nResults:\n{datetime.datetime.now()} - {report}'