"""Unit tests for ScaledRiemannianMetric."""
import random

import geomstats.backend as gs
import geomstats.tests
from geomstats.geometry.euclidean import Euclidean
from geomstats.geometry.hyperboloid import Hyperboloid
from geomstats.geometry.hypersphere import Hypersphere
# from geomstats.geometry.minkowski import Minkowski
from geomstats.geometry.scaled_riemannian_metric import ScaledRiemannianMetric
from geomstats.geometry.special_orthogonal import SpecialOrthogonal
from tests.conftest import Parametrizer
from tests.data_generation import _ManifoldTestData, _RiemannianMetricTestData
from tests.geometry_test_cases import ManifoldTestCase, RiemannianMetricTestCase

# should be done on all these manifolds
smoke_manifolds = [Euclidean(3), Minkowski(3), SpecialOrthogonal(3),
                   Hypersphere(dim=2), Hyperboloid(dim=2)]
smoke_metrics = [Euclidean(3).metric, Minkowski(3).metric, SpecialOrthogonal(3).metric,
                 Hypersphere(dim=2).metric, Hyperboloid(dim=2).metric]



class TestScalesRiemannianMetric(TestCase, metaclass=Parametrizer):
    original_metric = Hypersphere(dim=2).netric
    metric = ScaledRiemannianMetric(original_metric=original_metric, scale=4.0)

    class ScaledRiemannianMetricTestData(TestData):
        pass

    testing_data = ScaledRiemannianMetricTestData()

    def test_metric_matrix(self):
        # need a random base_point, 2 random tg_vectors at this base_point.
        result =

    def test_inner_product_matrix(self):
        pass



