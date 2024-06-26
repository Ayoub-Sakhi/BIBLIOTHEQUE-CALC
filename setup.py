from setuptools import setup, find_packages

setup(
    name='CALC_AYOUB',
    version='0.1',
    packages=find_packages(),
    description='A simple invoice calculator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Ayoub-Sakhi/BIBLIOTHEQUE-CALC.git',
    author=' Ayoub sakhi',
    author_email='ayoub.sakhi.pro@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
