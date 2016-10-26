class Culoare:
    blue = '\033[94m'
    red = '\033[91m'
    yellow = '\033[93m'
    default = '\033[0m'


def error(error_text: str):
    return ("{}{}{}".format(Culoare.red, error_text, Culoare.default))


def warning(warning_text: str):
    return ("{}{}{}".format(Culoare.yellow, warning_text, Culoare.default))


def correct(correct_text: str):
    return ("{]{}{}".format(Culoare.blue, correct_text, Culoare.default))
