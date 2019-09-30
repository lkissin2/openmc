import numpy as np
from openmc import _utils
import pytest

import os

print('hello')
plug1 = _utils.download('https://tinyurl.com/y4mcmc3u')
plug2 = _utils.download('https://tinyurl.com/y4mcmc3u')
assert os.path.getsize('plug1') == os.path.getsize('plug2')
print('world')
