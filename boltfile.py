import os

import bolt

bolt.register_task('ut', ['clear-pyc', 'nose'])
bolt.register_task('ct', ['conttest'])
bolt.register_task('clear-pyc', ['delete-pyc', 'delete-pyc.from-tests'])

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
_src_dir = os.path.join(PROJECT_ROOT, 'src')
_tests_dir = os.path.join(PROJECT_ROOT, 'tests')

config = {
    'conttest': {
        'task': 'ut',
        'directory': PROJECT_ROOT
    },
    'delete-pyc': {
        'sourcedir': _src_dir,
        'recursive': True,
        'from-tests': {
            'sourcedir': _tests_dir,
        }
    },
    'nose': {
        'directory': _tests_dir,
    }
}