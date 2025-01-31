import check50
from test import checks


@check50.check(points=3)
def hello():
    checks.hello('python3 hello.py')
