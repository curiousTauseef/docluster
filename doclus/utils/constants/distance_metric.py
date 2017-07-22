import numpy as np
from enum import Enum
from numpy import *
import numpy as np
from numpy.linalg import norm

class DistanceMetric(Enum):
    eucledian = staticmethod(lambda v1, v2 : sqrt(np.sum(square(array(v1) - array(v2)), axis=1)))
    manhattan = staticmethod(lambda v1, v2 : np.sum(absolute(array(v1) - array(v2)), axis=1))
    chebyshev = staticmethod(lambda v1, v2 : np.max(absolute(array(v1) - array(v2)), axis=1))
    angular = staticmethod(lambda v1, v2 : np.sum(array(v1)*array(v2), axis=1) / (norm(array(v1), axis=1) * norm(array(v2), axis=1)))
