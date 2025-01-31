import check50

# implement checks here

# Here just as an example
def hello(*args, **kwargs):
    result = (
        check50
        .run(*args, **kwargs)
        .stdout()
        .rstrip('\n')
        .lower()
    )
    if result != "Hello, world!":
        raise check50.Mismatch(
            'Hello, world!',
            result,
            help="What are you doing? "
                 "Literally just print('Hello, world!')"
        )
    return result
