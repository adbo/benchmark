"""Module containing classes for comparing objects"""
import senders
import reporters

class Comparator:
    """Class for comparing objects"""

    def compare(self, compared, competitors):
        reporter = reporters.Reporter()
        rules = ComparatorExtensions(compared, competitors, reporter)

        send_with_email = senders.SendWithEmail()
        send_with_sms = senders.SendWithSms()
        save_to_file = senders.SendToFile()
        show_on_console = senders.ShowOnConsole()

        if rules.rule_valid_compared():
            if rules.rule_compared_smaller():
                send_with_email.send(reporter.format_report())

            if rules.rule_compared_two_times_smaller():
                send_with_sms.send(reporter.format_report())

        report = reporter.format_report()
        save_to_file.send(report)
        show_on_console.send(report)


class ComparatorExtensions:
    """Class for extensions for comparator class"""

    def __init__(self, compared, competitors, reporter):
        self.compared = compared
        self.competitors = (item for item in competitors if self.valid_item(item))
        self._reporter = reporter

    def valid_item(self, item):
        result = 'loading_time' in item
        if not result:
            self._reporter.report_invalid(item)
        return result

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
        rule_valid = self.valid_item(self.compared)
        if rule_valid:
            self._reporter.report_loading_time(self.compared)
        return rule_valid
