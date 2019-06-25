"""Module containing classes for benchmarking sites"""

class Benchmark:
    """Class for benchmarking websites"""
    
    def __init__(self, compared, competitors, measurer, comparator):
        self.compared = compared
        self.competitors = competitors
        self._measurer = measurer
        self._comparator = comparator

    def make_benchmark(self):
        comapared_measure = self._measurer.measure(self.compared)
        extension = BenchmarkExtensions(comapared_measure)

        if extension.rule_valid_compared():
            competitors_measures = (self._measurer.measure(url) for url in self.competitors)
            self._comparator.compare(comapared_measure, competitors_measures)

class BenchmarkExtensions:

    def __init__(self, compared):
        self.compared = compared

    def rule_valid_compared(self):
        if 'loading_time' in self.compared:
            return True
        return False
        




        
    