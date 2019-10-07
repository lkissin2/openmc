from openmc import _utils
import pytest

import os


# @pytest.fixture(scope='module')
@pytest.fixture()
def download_photos(run_in_tmpdir):
    """use _utils download() function to download the same picture four times,
       twice to get unique names, and a third time to use the already downloaded
       block of code, and a fourth time to use the checksum block"""
    # _utils.download('https://media.gettyimages.com/photos/' +
    #                 'flamingo-picture-id957054810?s=2048x2048')
    _utils.download('https://i.ibb.co/HhKFc8x/small.jpg')
    _utils.download('https://tinyurl.com/y4t38ugb')
    _utils.download('https://tinyurl.com/y4t38ugb', as_browser = True)


# @pytest.fixture(scope='module')
@pytest.fixture()
def get_checksum_error(run_in_tmpdir):
    """use download() in such a way that will test the checksum error line"""
    with pytest.raises(OSError):
        _utils.download('https://tinyurl.com/y4t38ugb', as_browser = True,
                        checksum = 'not none')


def test_photos(download_photos):
    assert os.path.getsize('small.jpg') == \
           os.path.getsize('y4t38ugb')

def test_error(get_checksum_error):
    print('hi')
