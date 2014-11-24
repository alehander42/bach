from bach_macro import register_macro

__all__ = ['BUILTIN_MACROS']

def if_macro(test, if_true, if_false=None):
    return If(test, if_true, if_false)

def lambda_macro(args, *body):
    return Lambda(args, body)

def define_macro(label, value):
    return Define(label, value)

def dict_macro(*elements):
    keys, values = []
    for i, element in enumerate(elements):
        if i % 2 == 0:
            keys.append(element)
        else:
            values.append(element)
    return Dict(keys, values)

BUILTIN_MACROS = {}
register_macro(BUILTIN_MACROS, 'if', if_macro, (2, 3))
register_macro(BUILTIN_MACROS, 'lambda', lambda_macro, (1,))
register_macro(BUILTIN_MACROS, 'define', define_macro, 2)
register_macro(BUILTIN_MACROS, 'dict', dict_macro, (0,))
