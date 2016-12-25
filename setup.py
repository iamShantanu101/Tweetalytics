from setuptools import setup, find_packages

setup(
    name='smm',
    version='0.2',
    packages=['smm'],
    url='https://github.com/iamShantanu101/Tweetalytics',
    license='GPLv3',
    author='Shantanu Deshpandde',
    author_email='shantanud106@gmail.com',
    description='Real-Time, multi-lingual Twitter sentiment analyzer engine',
    install_requires=[
        "requests",
        "requests_oauthlib",
        "mongoengine",
        "nltk",
        'numpy',
        'gevent',
        'gevent-socketio',
        'flask',
        'argcomplete'
    ],
)
