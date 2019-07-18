"""Module containing classes for comparing objects"""
import reporters
import senders

class Comparator:
    """Class for comparing objects"""

    def __init__(self):
        self.send_with_email = senders.SendWithEmail()
        self.send_with_sms = senders.SendWithSms()
        self.save_to_file = senders.SendToFile()
        self.show_on_console = senders.ShowOnConsole()

    def compare(self, compared, competitors):
        reporter = reporters.Reporter()
        rules = ComparatorExtensions(compared, competitors, reporter)

        if rules.rule_valid_compared():
            if rules.rule_compared_smaller():
                self.send_with_email.send(reporter.format_report())

            if rules.rule_compared_two_times_smaller():
                self.send_with_sms.send(reporter.format_report())

        report = reporter.format_report()
        self.save_to_file.send(report)
        self.show_on_console.send(report)


class ComparatorExtensions:
    """Class for extensions for comparator class"""

    def __init__(self, compared, competitors, reporter):
        self.compared = compared
        self.competitors = [item for item in competitors if self.valid_item(item)]
        self._reporter = reporter

    def valid_item(self, item):
        result = 'loading_time' in item
        if not result:
            
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
        return self.valid_item(self.compared)

    def report_valid_item(self, item):
        is_valid = self.valid_item(self.compared)
        if is_valid:
            self._reporter.report_loading_time(self.compared)
        else:
            self._reporter.report_invalid(item)
