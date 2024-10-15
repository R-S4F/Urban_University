from multiprocessing import Pool
from pprint import pprint
import inspect

def not_callable(obj):
    if callable(obj):
        return False
    else:
        return True

def introspection_info(obj):
    return {'type': type(obj),
            'module': inspect.getmodule(obj),
            'attrs': [x[0] for x in inspect.getmembers(obj, not_callable)],
            'methods': [x[0] for x in inspect.getmembers(obj, inspect.ismethod)]}




from extr import Bank
b1 = Bank()
pprint(introspection_info(b1), compact=True)

