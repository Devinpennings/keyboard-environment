from .uppercase_modifier import UppercaseModifier

modifiers = {
    'UppercaseModifier': UppercaseModifier,
}


def get_handler(k):
    if k in modifiers:
        return modifiers[k]
    raise NotImplementedError(f'Handler {k} is not implemented')
