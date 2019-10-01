import numpy as np
from openmc import _utils
import pytest

import os


@pytest.fixture(scope='module')
def download_photos():
    """use _utils download() function to download the same picture three times,
       twice to get unique names, and a third time to use the already downloaded
       block of code"""
    _utils.download('https://media.gettyimages.com/photos/' +
                    'flamingo-picture-id957054810?s=2048x2048',
                     as_browser = True)
    _utils.download('https://tinyurl.com/y5cmtka3', as_browser = True)
    _utils.download('https://tinyurl.com/y5cmtka3', as_browser = True)


def test_photos(download_photos):
    assert os.path.getsize('y5cmtka3') == \
           os.path.getsize('flamingo-picture-id957054810')
    os.remove('y5cmtka3')
    os.remove('flamingo-picture-id957054810')
