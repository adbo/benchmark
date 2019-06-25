"""Module containing classes for comparing objects"""
import reports as reports
import formaters as formaters

class Comparator:
    """Class for comparing objects"""

    def compare(self, compared, competitors):
        results = ''
        rules = ComparatorExtensions(compared, competitors)
        formater = formaters.Formater()
        report_to_email = reports.ReportToEmail()
        report_to_sms = reports.ReportToSms()
        report_to_file = reports.ReportToFile()
        report_to_console = reports.ReportToConsole()

        results = results + rules.rule_valid_compared()
        if results:
            results = results + rules.rule_compared_smaller()
            if results:
                report_to_email.report(formater.format(results))

            results = results + rules.rule_compared_smaller()
            if results:
                report_to_sms.report(formater.format(results))

        report_to_file.report(results)
        report_to_console.report(results)


class ComparatorExtensions:
    """Class for extensions for comparator class"""

    def __init__(self, compared, competitors):
        self.compared = compared
        self.competitors = (competitor for competitor in competitors if self.rule_valid(competitor))

    def rule_valid(self, item):
        return 'loading_time' in item

    def rule_compared_smaller(self):
        results = ''
        for item in self.competitors:
            results = results + f'Loading time of {item.get("url")} is {item.get("loading_time")}.\n'
            if item.get('loading_time') < self.compared.get('loading_time'):
                results = results + f'Site {item.get("url")} is loading faster than {self.compared.get("url")}.\n'

        return results

    def rule_compared_two_times_smaller(self):
        results = ''
        for item in self.competitors:
            if (item.get('loading_time') * 2) <= self.compared.get('loading_time'):
                results = results + f'Site {item.get("url")} is loading two times faster than {self.compared.get("url")}.\n'

        return results

    def rule_valid_compared(self):
        results = ''

        if self.rule_valid(self.compared):
            results = f'Loading time of {self.compared.get("url")} is {self.compared.get("loading_time")}.\n'
        return results