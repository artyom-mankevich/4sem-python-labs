from setuptools import setup

setup(
    packages=['Serializers'],
    entry_points={
        'console_scripts': [
            'run = serializers.main:main'
        ]
    }
)
