"""Top level module for Independence"""

__descr__ = "Independence Project"
__version__ = "version"
__license__ = "BSD 3-Clause License"
__author__ = u"Setepenre"
__author_email__ = "setepenre@outlook.com"
__copyright__ = u"2021 Setepenre"
__url__ = "github.com/Delaunay/independence"


def my_function(lhs: int, rhs: int) -> int:
    """Add two numbers together

    Parameters
    ----------
    lhs: int
        first integer

    rhs: int
        second integer

    Raises
    ------
    value errror if lhs == 0

    Examples
    --------

    >>> my_function(1, 2)
    3
    >>> my_function(0, 2)
    Traceback (most recent call last):
      ...
    ValueError

    """
    if lhs == 0:
        raise ValueError()

    return lhs + rhs
