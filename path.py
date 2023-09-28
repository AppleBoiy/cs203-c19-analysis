import os


def root():
    return os.path.dirname(__file__)


def data():
    return os.path.join(root(), 'data')


def src():
    return os.path.join(root(), 'src')


def test():
    return os.path.join(root(), 'test')


def api():
    return os.path.join(src(), 'api')
