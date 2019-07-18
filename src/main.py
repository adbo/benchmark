import benchmarks
import measurements
import comparators

class App:
    """Class of main application"""

    def get_user_input(self):
        """Methon for getting user input"""

        print('Benchmark of loading time of websites.')

        competitors = []
        user_input = ''
        compared = input('Please provide url of compared website (with http): ')

        print('Please provide urls of competitors (z - to stop)')
        while user_input != 'z':
            if user_input:
                competitors.append(user_input)
            user_input = input('Please provide url of competitor (with http): ')

        self.compared = compared
        self.competitors = competitors

    def run_benchmark(self):
        """Method for run benchmark"""

        measurer = measurements.MeasureLoadingTime()
        comparator = comparators.Comparator()

        benchmark = benchmarks.Benchmark(self.compared, self.competitors, measurer, comparator)
        benchmark.run_benchmark()

if __name__ == '__main__':
    app = App()
    app.get_user_input()
    app.run_benchmark()
