import numpy as np
from openmc import _utils
import pytest

import os


@pytest.fixture(scope='module')
def download_photos():
    """use _utils download to download the same picture from two different urls
       so the files get different names and can be compared to each other and
       repeat a third time to test the 'already downloaded' lines"""
    _utils.download('https://media.gettyimages.com/photos/' +
                    'flamingo-picture-id957054810?s=2048x2048')
    _utils.download('https://tinyurl.com/y5cmtka3')
    _utils.download('https://tinyurl.com/y5cmtka3')


def test_photos(download_photos):
    assert os.path.getsize('y5cmtka3') == \
           os.path.getsize('flamingo-picture-id957054810')
    os.remove('y5cmtka3')
    os.remove('flamingo-picture-id957054810')
