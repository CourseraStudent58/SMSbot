import inspect


def log(*args):
    if debug is not True:
        return
    for s in args:
        print(s)
        if inspect.isclass(s):
            print(inspect.getmembers(s))


debug = True

# publicFQDN = '969dfd1c.ngrok.io'  #urllib.request.urlopen('https://ident.me').read().decode('utf8')
# logger(publicFQDN)
