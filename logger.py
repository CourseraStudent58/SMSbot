import inspect


def log(*args):
    if debug is not True:
        return
    for s in args:
        print(s)
        if inspect.isclass(s):
            print(inspect.getmembers(s))


debug = True

