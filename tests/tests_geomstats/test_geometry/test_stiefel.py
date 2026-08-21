import random

import pytest

import geomstats.backend as gs
from geomstats.geometry.stiefel import Stiefel, StiefelCanonicalMetric
from geomstats.test.parametrizers import DataBasedParametrizer, Parametrizer
from geomstats.test_cases.geometry.stiefel import (
    StiefelCanonicalMetricTestCase,
    StiefelStaticMethodsTestCase,
    StiefelTestCase,
)

from .data.stiefel import (
    StiefelCanonicalMetricSquareTestData,
    StiefelCanonicalMetricTestData,
    StiefelStaticMethodsTestData,
    StiefelTestData,
)

# TODO: use comparison with limit cases
# TODO: make it work with p=1?


def _get_random_params():
    while True:
        a = random.randint(2, 5)
        b = random.randint(2, 5)

        if a != b:
            break

    if a > b:
        n, p = a, b
    else:
        n, p = b, a

    return n, p


@pytest.fixture(
    scope="class",
    params=[
        _get_random_params(),
    ],
)
def spaces(request):
    n, p = request.param
    request.cls.space = Stiefel(n=n, p=p, equip=False)


@pytest.mark.usefixtures("spaces")
class TestStiefel(StiefelTestCase, metaclass=DataBasedParametrizer):
    testing_data = StiefelTestData()


@pytest.mark.smoke
class TestStiefelStaticMethods(StiefelStaticMethodsTestCase, metaclass=Parametrizer):
    Space = Stiefel
    testing_data = StiefelStaticMethodsTestData()


@pytest.fixture(
    scope="class",
    params=[
        _get_random_params(),
    ],
)
def equipped_spaces(request):
    n, p = request.param
    request.cls.space = Stiefel(n=n, p=p)


@pytest.mark.usefixtures("equipped_spaces")
class TestStiefelCanonicalMetric(
    StiefelCanonicalMetricTestCase, metaclass=DataBasedParametrizer
):
    testing_data = StiefelCanonicalMetricTestData()

    def test_log_antipodal_raises(self):
        """Log of antipodal points is not well-defined."""
        space = Stiefel(n=3, p=2)
        point = gs.array([[1.0, 0.0], [0.0, 1.0], [0.0, 0.0]])
        with pytest.raises(ValueError, match="antipodal"):
            space.metric.log(-point, point)


class TestStiefelCanonicalMetricSquare(
    StiefelCanonicalMetricTestCase, metaclass=DataBasedParametrizer
):
    k = random.randint(2, 5)
    space = Stiefel(n=k, p=k, equip=False)
    space.equip_with_metric(StiefelCanonicalMetric)
    testing_data = StiefelCanonicalMetricSquareTestData()
