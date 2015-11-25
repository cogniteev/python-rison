from setuptools import setup, find_packages


setup(
    name='rison',
    version='0.0.2',
    description='A Python rison encoder/decoder',
    long_description='A Python rison encoder/decoder',
    url='https://github.com/cogniteev/python-rison',
    author='Aaron Forsander',
    author_email='tech@cogniteev.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Encoding',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='rison',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        'six>=1.10.0',
    ],
)
