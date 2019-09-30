import numpy as np
# import openmc
from openmc import _utils
import pytest

import os

# import _utils

print('hello')
teapot = _utils.download('https://tinyurl.com/y4mcmc3u')
assert os.path.getsize('jig') == os.path.getsize('y4mcmc3u')
print('world')
