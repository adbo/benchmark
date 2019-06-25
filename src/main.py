import benchmarks
import measurements
import comparators

if __name__ == '__main__':
    print('Benchmark of loading time of websites.')

    competitors = []
    competitor = ''
    compared = input('Please provide url of compared website (with http): ')

    print('Please provide urls of competitors (z - to stop)')
    while competitor != 'z':
        if competitor:
            competitors.append(competitor)
        competitor = input('Please provide url of competitor (with http): ')

    measurer = measurements.MeasureLoadingTime()
    comparator = comparators.Comparator()

    benchmark = benchmarks.Benchmark(compared, competitors, measurer, comparator)
    benchmark.make_benchmark()
