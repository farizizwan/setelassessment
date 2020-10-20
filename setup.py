from setuptools import setup
setup(
    name = 'setelassessment',
    version = '0.1.0',
    packages = ['problem1'],
    entry_points = {
        'console_scripts': [
            'problem1 = problem1.__main__:main'
        ]
    })


    