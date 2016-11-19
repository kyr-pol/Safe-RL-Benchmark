"""Bounded subspace of R^n."""
import numpy as np
from SafeRLBench import Space


class BoundedSpace(Space):
    """
    Bounded subspace of R^n.

    Usage:
    BoundedSpace(np.array(-1,-2), np.array(1,0))
    or
    BoundedSpace(-1, 1)
    """

    def __init__(self, lower, upper):
        """Initialize BoundedSpace."""
        if (np.isscalar(lower) and np.isscalar(upper)):
            self.lower = np.array([lower])
            self.upper = np.array([upper])
        else:
            assert(lower.shape == upper.shape)
            self.lower = lower
            self.upper = upper

    def contains(self, x):
        """Check if element is contained."""
        return (x.shape == self.lower.shape
                and (x > self.lower).all()
                and (x < self.lower).all())

    def element(self):
        """Return element."""
        return self.upper
