import os
from enum import Enum


class Path(Enum):
    ROOT = os.path.dirname(__file__)
    DATA = os.path.join(ROOT, 'data')
    SRC = os.path.join(ROOT, 'src')
    TEST = os.path.join(ROOT, 'test')
    API = os.path.join(SRC, 'api')
