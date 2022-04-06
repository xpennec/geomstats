"""Scaled Riemannian and pseudo-Riemannian metric.

Define a metric from an existing one, scaled by a positive scalar.
This only affects the metric (and the distance) and not the  exp and log maps
that are expressed in a non orthonormal basis for the scaled metric.

Lead author: Xavier Pennec.
"""


class ScaledRiemannianMetric(RiemannianMetric):
    """Class for scaled Riemannian metrics.

    Parameters
    ----------
    original_metric : ??
        Original metric.
    scale : float
        Scaling factor on the metric matrix
    """

    def __init__(self, original_metric, scale=1.0):
        super(ProductRiemannianMetric, self).__init__(
            dim=original_metric.dim,
            shape=original_metric.shape,
            signature=original_metric.signature,
            default_point_type=original_metric.default_point_type,
        )

    def metric_matrix(self, base_point=None):
        """Metric matrix at the tangent space at a base point.

        Parameters
        ----------
        base_point : array-like, shape=[..., dim]
            Base point.
            Optional, default: None.

        Returns
        -------
        mat : array-like, shape=[..., dim, dim]
            Inner-product matrix.
        """
        raise NotImplementedError(
            "The computation of the metric matrix" " is not implemented."
        )