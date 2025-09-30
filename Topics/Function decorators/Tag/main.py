def tagged(func):
    def wrapper(text):
        return f'<title>{func(text)}</title>'
    return wrapper
