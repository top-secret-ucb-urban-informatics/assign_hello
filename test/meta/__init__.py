import check50
from pathlib import Path
from test import check


@check50.check()
def hello():
    path = Path(
        __file__,
        '..',
        'pass_hello.py'
    ).resolve()
    return check.hello(f"python {path}")


@check50.check()
def goodbye():
    path = Path(
        __file__,
        '..',
        'pass_goodbye.py'
    ).resolve()
    return check.goodbye(f"python {path}")


@check50.check()
def fail_hello():
    path = Path(
        __file__,
        '..',
        'fail_hello.py'
    ).resolve()
    try:
        check.hello(f"python {path}")
    except Exception as e:
        ...
    else:
        raise check50.Failure("Expected an error, but program ran successfully")


@check50.check()
def fail_goodbye():
    path = Path(
        __file__,
        '..',
        'fail_goodbye.py'
    ).resolve()
    try:
        check.goodbye(f"python {path}")
    except Exception as e:
        ...
    else:
        raise check50.Failure("Expected an error, but program ran successfully")
