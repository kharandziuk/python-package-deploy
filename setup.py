from setuptools import setup

setup(
    name='my_project',
    version='0.1.0',
    packages=['my_package'],
    entry_points={
      'console_scripts': [
        'my_package = my_package.__main__:main'
      ]
    },
)
