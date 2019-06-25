"""Module containing classes for comparing objects"""
import senders
import reporters

class Comparator:
    """Class for comparing objects"""

    def compare(self, compared, competitors):
        reporter = reporters.Reporter()
        rules = ComparatorExtensions(compared, competitors, reporter)

        report_to_email = senders.SendWithEmail()
        report_to_sms = senders.SendWithSms()
        report_to_file = senders.SendToFile()
        report_to_console = senders.ShowOnConsole()

        if rules.rule_valid_compared():
            if rules.rule_compared_smaller():
                report_to_email.report(reporter.format_report())

            if rules.rule_compared_smaller():
                report_to_sms.report(reporter.format_report())

        report = reporter.format_report()
        report_to_file.report(report)
        report_to_console.report(report)


class ComparatorExtensions:
    """Class for extensions for comparator class"""

    def __init__(self, compared, competitors, reporter):
        self.compared = compared
        self.competitors = (competitor for competitor in competitors if self.rule_valid(competitor))
        self._reporter = reporter

    def rule_valid(self, item):
        return 'loading_time' in item

    def rule_compared_smaller(self):
        result = False
        for item in self.competitors:
            self._reporter.report_loading_time(item)
            if item.get('loading_time') < self.compared.get('loading_time'):
                self._reporter.report_smaller(self.compared, item)
                result = True

        return result

    def rule_compared_two_times_smaller(self):
        result = False
        for item in self.competitors:
            if (item.get('loading_time') * 2) <= self.compared.get('loading_time'):
                self._reporter.report_smaller_two_times(self.compared, item)
                result = True

        return result

    def rule_valid_compared(self):
        rule_valid = self.rule_valid(self.compared)
        if rule_valid:
            self._reporter.report_loading_time(self.compared)
        return rule_valid