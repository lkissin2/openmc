import numpy as np
from openmc import _utils
import pytest

import os


@pytest.fixture(scope='module')
def download_photos():
    print('hello')
    _utils.download('https://media.gettyimages.com/photos/flamingo-picture-id957054810?s=2048x2048')
    _utils.download('https://tinyurl.com/y5cmtka3')
    print('world')
    print('!')


def test_photos(download_photos):
    assert os.path.getsize('y5cmtka3') == os.path.getsize('flamingo-picture-id957054810')
    os.remove('y5cmtka3')
    os.remove('flamingo-picture-id957054810')
