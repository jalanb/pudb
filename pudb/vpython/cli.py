from pprint import pformat
def main(locals_=None, globals_=None):
    locals_ = locals_ or {}
    globals_ = globals_ or {}
    raise NotImplementedError(pformat(dir()))

if __name__ == '__main__':
    main(locals())
