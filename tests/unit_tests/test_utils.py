from openmc import _utils
import pytest

import os


@pytest.fixture(scope='module')
def download_photos():
    """use _utils download() function to download the same picture four times,
       twice to get unique names, and a third time to use the already downloaded
       block of code, and a fourth time to use the checksum block"""
    # _utils.download('https://media.gettyimages.com/photos/' +
    #                 'flamingo-picture-id957054810?s=2048x2048')
    _utils.download('https://i.ibb.co/HhKFc8x/small.jpg')
    _utils.download('https://tinyurl.com/y4t38ugb')
    _utils.download('https://tinyurl.com/y4t38ugb', as_browser = True)


@pytest.fixture(scope='module')
def get_checksum_error():
    """use download() in such a way that will test the checksum error line"""
    _utils.download('https://tinyurl.com/y4t38ugb', as_browser = True,
                    checksum = '9ab7330c8fac75e18874570f582aec56')


def test_photos(download_photos):
    assert os.path.getsize('small.jpg') == \
           os.path.getsize('y4t38ugb')
    os.remove('y4t38ugb')
    os.remove('small.jpg')

# def test_error(get_checksum_error):
#     _utils.download('https://tinyurl.com/y4t38ugb',
#                     checksum = 'not none')
#     # assert True
#     os.remove('y4t38ugb')
