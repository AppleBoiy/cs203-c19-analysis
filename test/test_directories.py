import os
import inspect
import platform

from directories import Path, Url

dir_path = inspect.getfile(Path)
if platform.system() == 'Windows':
    file_name = r'\\directories.py'
else:
    file_name = '/directories.py'
__root__ = dir_path.replace(file_name, '')


def test_root():
    assert Path.ROOT.value == __root__


def test_data_dir():
    assert Path.DATA.value == os.path.join(__root__, 'data')


def test_src():
    assert Path.SRC.value == os.path.join(__root__, 'src')


def test_test():
    assert Path.TEST.value == os.path.join(__root__, 'test')


def test_api():
    assert Path.API.value == os.path.join(__root__, 'src', 'api')


def test_data():
    assert Url.DATA.value == 'https://drive.google.com/file/d/1ZRKl7ZBfEqS3dhYaUcCjDmuqGeBSmlYL/view?usp=sharing'


def test_raw():
    assert Url.RAW.value == 'https://drive.google.com/file/d/1srMUv1YXig0cKc-YfaZfdGRmg2X0uOGL/view?usp=sharing'


def test_fips():
    assert Url.FIPS.value == 'https://drive.google.com/file/d/10xHEi7f5UemavfczphU1nFa-pjvM_vNS/view?usp=sharing'


def test_validated():
    assert Url.VALIDATED.value == 'https://drive.google.com/file/d/1p65YghN0OXOD3Dvd2hgSIfaks2z4h6Td/view?usp=sharing'
