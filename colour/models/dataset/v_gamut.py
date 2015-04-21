#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
V-Gamut Colourspace
===================

Defines the *V-Gamut* colourspace:

-   :attr:`V_GAMUT_COLOURSPACE`.

See Also
--------
`RGB Colourspaces IPython Notebook
<http://nbviewer.ipython.org/github/colour-science/colour-ipython/blob/master/notebooks/models/rgb.ipynb>`_  # noqa

References
----------
.. [1]  Panasonic. (2014). VARICAM V-Log/V-Gamut. Retrieved from
        http://pro-av.panasonic.net/en/varicam/common/pdf/VARICAM_V-Log_V-Gamut.pdf  # noqa
"""

from __future__ import division, unicode_literals

import numpy as np

from colour.colorimetry import ILLUMINANTS
from colour.models import RGB_Colourspace
from colour.utilities import Structure

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2015 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['V_GAMUT_PRIMARIES',
           'V_GAMUT_ILLUMINANT',
           'V_GAMUT_WHITEPOINT',
           'V_GAMUT_TO_XYZ_MATRIX',
           'XYZ_TO_V_GAMUT_MATRIX',
           'V_LOG_CONSTANTS',
           'V_GAMUT_TRANSFER_FUNCTION',
           'V_GAMUT_INVERSE_TRANSFER_FUNCTION',
           'V_GAMUT_COLOURSPACE']

V_GAMUT_PRIMARIES = np.array(
    [[0.730, 0.280],
     [0.165, 0.840],
     [0.100, -0.030]])
"""
*V-Gamut* colourspace primaries.

V_GAMUT_PRIMARIES : ndarray, (3, 2)
"""

V_GAMUT_ILLUMINANT = 'D65'
"""
*V-Gamut* colourspace whitepoint name as illuminant.

V_GAMUT_WHITEPOINT : unicode
"""

V_GAMUT_WHITEPOINT = ILLUMINANTS.get(
    'CIE 1931 2 Degree Standard Observer').get(V_GAMUT_ILLUMINANT)
"""
*V-Gamut* colourspace whitepoint.

V_GAMUT_WHITEPOINT : tuple
"""

V_GAMUT_TO_XYZ_MATRIX = np.array(
    [[0.679644, 0.152211, 0.118600],
     [0.260686, 0.774894, -0.035580],
     [-0.009310, -0.004612, 1.102980]])
"""
*V-Gamut* colourspace to *CIE XYZ* tristimulus values matrix.

V_GAMUT_TO_XYZ_MATRIX : array_like, (3, 3)
"""

XYZ_TO_V_GAMUT_MATRIX = np.linalg.inv(
    V_GAMUT_TO_XYZ_MATRIX)
"""
*CIE XYZ* tristimulus values to *V-Gamut* colourspace matrix.

XYZ_TO_V_GAMUT_MATRIX : array_like, (3, 3)
"""

V_LOG_CONSTANTS = Structure(cut1=0.01,
                            cut2=0.181,
                            b=0.00873,
                            c=0.241514,
                            d=0.598206)
"""
*V-Log* colourspace constants.

V_LOG_CONSTANTS : Structure
"""


def _v_gamut_rgb_transfer_function(value):
    """
    Defines the *V-Log* transfer function.

    Parameters
    ----------
    value : numeric or array_like
        Value.

    Returns
    -------
    numeric or ndarray
        Companded value.
    """

    value = np.asarray(value)

    cut1 = V_LOG_CONSTANTS.cut1
    b = V_LOG_CONSTANTS.b
    c = V_LOG_CONSTANTS.c
    d = V_LOG_CONSTANTS.d

    value = np.where(value < cut1,
                     5.6 * value + 0.125,
                     c * np.log10(value + b) + d)
    return value


def _v_gamut_rgb_inverse_transfer_function(value):
    """
    Defines the *V-Log* inverse transfer function.

    Parameters
    ----------
    value : numeric or array_like
        Value.

    Returns
    -------
    numeric or ndarray
        Companded value.
    """

    value = np.asarray(value)

    cut2 = V_LOG_CONSTANTS.cut2
    b = V_LOG_CONSTANTS.b
    c = V_LOG_CONSTANTS.c
    d = V_LOG_CONSTANTS.d

    value = np.where(value < cut2,
                     (value - 0.125) / 5.6,
                     np.power(10, ((value - d) / c)) - b)

    return value


V_GAMUT_TRANSFER_FUNCTION = _v_gamut_rgb_transfer_function
"""
Transfer function from linear to *V-Gamut* colourspace.

V_GAMUT_TRANSFER_FUNCTION : object
"""

V_GAMUT_INVERSE_TRANSFER_FUNCTION = _v_gamut_rgb_inverse_transfer_function
"""
Inverse transfer function from *V-Gamut* colourspace to linear.

V_GAMUT_INVERSE_TRANSFER_FUNCTION : object
"""

V_GAMUT_COLOURSPACE = RGB_Colourspace(
    'V-Gamut',
    V_GAMUT_PRIMARIES,
    V_GAMUT_WHITEPOINT,
    V_GAMUT_ILLUMINANT,
    V_GAMUT_TO_XYZ_MATRIX,
    XYZ_TO_V_GAMUT_MATRIX,
    V_GAMUT_TRANSFER_FUNCTION,
    V_GAMUT_INVERSE_TRANSFER_FUNCTION)
"""
*V-Gamut* colourspace.

V_GAMUT_COLOURSPACE : RGB_Colourspace
"""
