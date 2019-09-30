import numpy as np
from openmc import _utils
import pytest

import os

print('hello')
_utils.download('https://media.gettyimages.com/photos/flamingo-picture-id957054810?s=2048x2048')
_utils.download('https://tinyurl.com/y5cmtka3')
assert os.path.getsize('y5cmtka3') == os.path.getsize('flamingo-picture-id957054810')
print('world')
