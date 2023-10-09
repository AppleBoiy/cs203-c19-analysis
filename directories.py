import os
from enum import Enum


class Path(Enum):
    ROOT: str = os.path.dirname(__file__)
    DATA: str = os.path.join(ROOT, "data")
    SRC: str = os.path.join(ROOT, "src")
    TEST: str = os.path.join(ROOT, "test")
    API: str = os.path.join(SRC, "api")


class Url(Enum):
    DATA: str = "https://drive.google.com/file/d/1ZRKl7ZBfEqS3dhYaUcCjDmuqGeBSmlYL/view?usp=sharing"
    RAW: str = "https://drive.google.com/file/d/1srMUv1YXig0cKc-YfaZfdGRmg2X0uOGL/view?usp=sharing"
    FIPS: str = "https://drive.google.com/file/d/10xHEi7f5UemavfczphU1nFa-pjvM_vNS/view?usp=sharing"
    VALIDATED: str = "https://drive.google.com/file/d/1p65YghN0OXOD3Dvd2hgSIfaks2z4h6Td/view?usp=sharing"
