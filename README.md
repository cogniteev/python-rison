# python-rison

[![Build Status](https://travis-ci.org/cogniteev/python-rison.svg)](https://travis-ci.org/cogniteev/python-rison)
[![Coverage Status](https://coveralls.io/repos/cogniteev/python-rison/badge.svg?branch=master&service=github)](https://coveralls.io/github/cogniteev/python-rison?branch=master)
[![Code Climate](https://codeclimate.com/github/cogniteev/python-rison/badges/gpa.svg)](https://codeclimate.com/github/cogniteev/python-rison)
[![Code Health](https://landscape.io/github/cogniteev/python-rison/master/landscape.svg?style=flat)](https://landscape.io/github/cogniteev/python-rison/master)

Python version of the rison encoder/decoder originally taken from http://mjtemplate.org/examples/rison.html

## Usage

```python
import rison

print rison.dumps({'foo': 'bar'})  # '(foo:bar)'

print rison.loads('(foo:bar)')  # {'foo': 'bar'}
```

## Tests

```
pip install nose
nosetests tests/*.py
```
