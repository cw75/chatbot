from setuptools import setup, find_packages

setup(
    name='bot',
    version='1.0',
    packages=find_packages(),
    description='bot',
    include_package_data=True,
    install_requires=[
        'emoji==0.5.1',
        'pandas==0.23.4',
        'tweet-preprocessor==0.6.0',
        'scikit_learn==0.20.0',
        'spacy==2.0.16',
        'spacy_cld==0.1.0',
        'torch==0.4.1',
        'torchtext==0.3.1',
        'msgpack==0.5.6',
    ],
)