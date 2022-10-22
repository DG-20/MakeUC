def FormErrors(*args):
    message = ""
    for f in args:
        if f.errors:
            message = f.errors.as_text()
    return message
