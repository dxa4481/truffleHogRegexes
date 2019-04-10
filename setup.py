from setuptools import setup, find_packages

setup(
    name='truffleHogRegexes',
    version='0.0.7',
    description='These regexes power truffleHog.',
    url='https://github.com/dxa4481/truffleHogRegexes',
    author='Dylan Ayrey',
    author_email='dylanayrey@gmail.com',
    license='GNU',
    packages = find_packages(),
    package_data={'': ['regexes.json']},
)
