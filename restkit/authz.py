from importlib import import_module

from werkzeug.exceptions import Forbidden


class Requirement(object):
    """ Checks a function call and raises an exception if the
    function returns a non-True value. """

    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __getattr__(self, attr):
        real = getattr(self.wrapped, attr)
        return Requirement(real)

    def __call__(self, *args, **kwargs):
        fc = self.wrapped(*args, **kwargs)
        if fc is not True:
            raise Forbidden('Sorry, you\'re not permitted to do this.')
        return fc

    @classmethod
    def here(cls, t):
        return cls(import_module(t))
