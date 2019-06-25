import datetime

class Report:

    def __init__(self):
        self.report_data = ''

    def report_loading_time(self, item):
        self.report_data = f'{self.report_data}. Loading time of {item.get("url")} is {item.get("loading_time")}.\n'

    def report_smaller(self, compared, competitor):
        self.report_data = f'{self.report_data}. Site {competitor.get("url")} is loading faster than {compared.get("url")}.\n'

    def report_smaller_two_times(self, compared, competitor):
        self.report_data = f'{self.report_data}. Site {competitor.get("url")} is loading two times faster than {compared.get("url")}.\n'

    def format_report(self):
        return f'\nResults:\n{datetime.datetime.now()} - {self.report_data}'