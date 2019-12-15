# -*- coding: utf-8 -*-
"""
Test Colour Samples Spectral Distributions
================================================

Defines the *CIE 1995* test colour samples spectral distributions.

The *CIE 1995* test colour samples data is in the form of a *dict* of
:class:`colour.SpectralDistribution` classes as follows::

    {'name': SpectralDistribution, ..., 'name': SpectralDistribution}

See Also
--------
`Colour Rendering Index Jupyter Notebook
<http://nbviewer.jupyter.org/github/colour-science/colour-notebooks/\
blob/master/notebooks/quality/cri.ipynb>`_

References
----------
-   :cite:`Ohno2008a` : Ohno, Y., & Davis, W. (2008). NIST CQS simulation 7.4.
    Retrieved from https://drive.google.com/file/d/\
1PsuU6QjUJjCX6tQyCud6ul2Tbs8rYWW9/view?usp=sharing
"""

from __future__ import division, unicode_literals

from colour.colorimetry import SpectralDistribution
from colour.utilities import CaseInsensitiveMapping

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2019 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = [
    'TCS_INDEXES_TO_NAMES', 'TCS_APPROXIMATE_MUNSELL_NOTATIONS',
    'TCS_SDS_DATA', 'TCS_SDS'
]

TCS_INDEXES_TO_NAMES = {
    1: 'TCS01',
    2: 'TCS02',
    3: 'TCS03',
    4: 'TCS04',
    5: 'TCS05',
    6: 'TCS06',
    7: 'TCS07',
    8: 'TCS08',
    9: 'TCS09',
    10: 'TCS10',
    11: 'TCS11',
    12: 'TCS12',
    13: 'TCS13',
    14: 'TCS14'
}
"""
Test colour samples indexes to names mapping.

TCS_INDEXES_TO_NAMES : dict
"""

TCS_APPROXIMATE_MUNSELL_NOTATIONS = CaseInsensitiveMapping({
    'TCS01': '7.5 R 6/4',
    'TCS02': '5 Y 6/4',
    'TCS03': '5 GY 6/8',
    'TCS04': '2.5 G 6/6',
    'TCS05': '10 BG 6/4',
    'TCS06': '5 PB 6/8',
    'TCS07': '2.5 P 6/8',
    'TCS08': '10 P 6/8',
    'TCS09': '4.5 R 4/13',
    'TCS10': '5 Y 8/10',
    'TCS11': '4.5 G 5/8',
    'TCS12': '3 PB 3/11',
    'TCS13': '5 YR 8/4',
    'TCS14': '5 GY 4/4'
})
"""
Test colour samples *Munsell* colour approximations.

TCS_APPROXIMATE_MUNSELL_NOTATIONS : CaseInsensitiveMapping
"""

TCS_SDS_DATA = {
    'TCS01': {
        360: 0.116,
        365: 0.136,
        370: 0.159,
        375: 0.190,
        380: 0.219,
        385: 0.239,
        390: 0.252,
        395: 0.256,
        400: 0.256,
        405: 0.254,
        410: 0.252,
        415: 0.248,
        420: 0.244,
        425: 0.240,
        430: 0.237,
        435: 0.232,
        440: 0.230,
        445: 0.226,
        450: 0.225,
        455: 0.222,
        460: 0.220,
        465: 0.218,
        470: 0.216,
        475: 0.214,
        480: 0.214,
        485: 0.214,
        490: 0.216,
        495: 0.218,
        500: 0.223,
        505: 0.225,
        510: 0.226,
        515: 0.226,
        520: 0.225,
        525: 0.225,
        530: 0.227,
        535: 0.230,
        540: 0.236,
        545: 0.245,
        550: 0.253,
        555: 0.262,
        560: 0.272,
        565: 0.283,
        570: 0.298,
        575: 0.318,
        580: 0.341,
        585: 0.367,
        590: 0.390,
        595: 0.409,
        600: 0.424,
        605: 0.435,
        610: 0.442,
        615: 0.448,
        620: 0.450,
        625: 0.451,
        630: 0.451,
        635: 0.451,
        640: 0.451,
        645: 0.451,
        650: 0.450,
        655: 0.450,
        660: 0.451,
        665: 0.451,
        670: 0.453,
        675: 0.454,
        680: 0.455,
        685: 0.457,
        690: 0.458,
        695: 0.460,
        700: 0.462,
        705: 0.463,
        710: 0.464,
        715: 0.465,
        720: 0.466,
        725: 0.466,
        730: 0.466,
        735: 0.466,
        740: 0.467,
        745: 0.467,
        750: 0.467,
        755: 0.467,
        760: 0.467,
        765: 0.467,
        770: 0.467,
        775: 0.467,
        780: 0.467,
        785: 0.467,
        790: 0.467,
        795: 0.466,
        800: 0.466,
        805: 0.466,
        810: 0.466,
        815: 0.466,
        820: 0.465,
        825: 0.464,
        830: 0.464
    },
    'TCS02': {
        360: 0.053,
        365: 0.055,
        370: 0.059,
        375: 0.064,
        380: 0.070,
        385: 0.079,
        390: 0.089,
        395: 0.101,
        400: 0.111,
        405: 0.116,
        410: 0.118,
        415: 0.120,
        420: 0.121,
        425: 0.122,
        430: 0.122,
        435: 0.122,
        440: 0.123,
        445: 0.124,
        450: 0.127,
        455: 0.128,
        460: 0.131,
        465: 0.134,
        470: 0.138,
        475: 0.143,
        480: 0.150,
        485: 0.159,
        490: 0.174,
        495: 0.190,
        500: 0.207,
        505: 0.225,
        510: 0.242,
        515: 0.253,
        520: 0.260,
        525: 0.264,
        530: 0.267,
        535: 0.269,
        540: 0.272,
        545: 0.276,
        550: 0.282,
        555: 0.289,
        560: 0.299,
        565: 0.309,
        570: 0.322,
        575: 0.329,
        580: 0.335,
        585: 0.339,
        590: 0.341,
        595: 0.341,
        600: 0.342,
        605: 0.342,
        610: 0.342,
        615: 0.341,
        620: 0.341,
        625: 0.339,
        630: 0.339,
        635: 0.338,
        640: 0.338,
        645: 0.337,
        650: 0.336,
        655: 0.335,
        660: 0.334,
        665: 0.332,
        670: 0.332,
        675: 0.331,
        680: 0.331,
        685: 0.330,
        690: 0.329,
        695: 0.328,
        700: 0.328,
        705: 0.327,
        710: 0.326,
        715: 0.325,
        720: 0.324,
        725: 0.324,
        730: 0.324,
        735: 0.323,
        740: 0.322,
        745: 0.321,
        750: 0.320,
        755: 0.318,
        760: 0.316,
        765: 0.315,
        770: 0.315,
        775: 0.314,
        780: 0.314,
        785: 0.313,
        790: 0.313,
        795: 0.312,
        800: 0.312,
        805: 0.311,
        810: 0.311,
        815: 0.311,
        820: 0.311,
        825: 0.311,
        830: 0.310
    },
    'TCS03': {
        360: 0.058,
        365: 0.059,
        370: 0.061,
        375: 0.063,
        380: 0.065,
        385: 0.068,
        390: 0.070,
        395: 0.072,
        400: 0.073,
        405: 0.073,
        410: 0.074,
        415: 0.074,
        420: 0.074,
        425: 0.073,
        430: 0.073,
        435: 0.073,
        440: 0.073,
        445: 0.073,
        450: 0.074,
        455: 0.075,
        460: 0.077,
        465: 0.080,
        470: 0.085,
        475: 0.094,
        480: 0.109,
        485: 0.126,
        490: 0.148,
        495: 0.172,
        500: 0.198,
        505: 0.221,
        510: 0.241,
        515: 0.260,
        520: 0.278,
        525: 0.302,
        530: 0.339,
        535: 0.370,
        540: 0.392,
        545: 0.399,
        550: 0.400,
        555: 0.393,
        560: 0.380,
        565: 0.365,
        570: 0.349,
        575: 0.332,
        580: 0.315,
        585: 0.299,
        590: 0.285,
        595: 0.272,
        600: 0.264,
        605: 0.257,
        610: 0.252,
        615: 0.247,
        620: 0.241,
        625: 0.235,
        630: 0.229,
        635: 0.224,
        640: 0.220,
        645: 0.217,
        650: 0.216,
        655: 0.216,
        660: 0.219,
        665: 0.224,
        670: 0.230,
        675: 0.238,
        680: 0.251,
        685: 0.269,
        690: 0.288,
        695: 0.312,
        700: 0.340,
        705: 0.366,
        710: 0.390,
        715: 0.412,
        720: 0.431,
        725: 0.447,
        730: 0.460,
        735: 0.472,
        740: 0.481,
        745: 0.488,
        750: 0.493,
        755: 0.497,
        760: 0.500,
        765: 0.502,
        770: 0.505,
        775: 0.510,
        780: 0.516,
        785: 0.520,
        790: 0.524,
        795: 0.527,
        800: 0.531,
        805: 0.535,
        810: 0.539,
        815: 0.544,
        820: 0.548,
        825: 0.552,
        830: 0.555
    },
    'TCS04': {
        360: 0.057,
        365: 0.059,
        370: 0.062,
        375: 0.067,
        380: 0.074,
        385: 0.083,
        390: 0.093,
        395: 0.105,
        400: 0.116,
        405: 0.121,
        410: 0.124,
        415: 0.126,
        420: 0.128,
        425: 0.131,
        430: 0.135,
        435: 0.139,
        440: 0.144,
        445: 0.151,
        450: 0.161,
        455: 0.172,
        460: 0.186,
        465: 0.205,
        470: 0.229,
        475: 0.254,
        480: 0.281,
        485: 0.308,
        490: 0.332,
        495: 0.352,
        500: 0.370,
        505: 0.383,
        510: 0.390,
        515: 0.394,
        520: 0.395,
        525: 0.392,
        530: 0.385,
        535: 0.377,
        540: 0.367,
        545: 0.354,
        550: 0.341,
        555: 0.327,
        560: 0.312,
        565: 0.296,
        570: 0.280,
        575: 0.263,
        580: 0.247,
        585: 0.229,
        590: 0.214,
        595: 0.198,
        600: 0.185,
        605: 0.175,
        610: 0.169,
        615: 0.164,
        620: 0.160,
        625: 0.156,
        630: 0.154,
        635: 0.152,
        640: 0.151,
        645: 0.149,
        650: 0.148,
        655: 0.148,
        660: 0.148,
        665: 0.149,
        670: 0.151,
        675: 0.154,
        680: 0.158,
        685: 0.162,
        690: 0.165,
        695: 0.168,
        700: 0.170,
        705: 0.171,
        710: 0.170,
        715: 0.168,
        720: 0.166,
        725: 0.164,
        730: 0.164,
        735: 0.165,
        740: 0.168,
        745: 0.172,
        750: 0.177,
        755: 0.181,
        760: 0.185,
        765: 0.189,
        770: 0.192,
        775: 0.194,
        780: 0.197,
        785: 0.200,
        790: 0.204,
        795: 0.210,
        800: 0.218,
        805: 0.225,
        810: 0.233,
        815: 0.243,
        820: 0.254,
        825: 0.264,
        830: 0.274
    },
    'TCS05': {
        360: 0.143,
        365: 0.187,
        370: 0.233,
        375: 0.269,
        380: 0.295,
        385: 0.306,
        390: 0.310,
        395: 0.312,
        400: 0.313,
        405: 0.315,
        410: 0.319,
        415: 0.322,
        420: 0.326,
        425: 0.330,
        430: 0.334,
        435: 0.339,
        440: 0.346,
        445: 0.352,
        450: 0.360,
        455: 0.369,
        460: 0.381,
        465: 0.394,
        470: 0.403,
        475: 0.410,
        480: 0.415,
        485: 0.418,
        490: 0.419,
        495: 0.417,
        500: 0.413,
        505: 0.409,
        510: 0.403,
        515: 0.396,
        520: 0.389,
        525: 0.381,
        530: 0.372,
        535: 0.363,
        540: 0.353,
        545: 0.342,
        550: 0.331,
        555: 0.320,
        560: 0.308,
        565: 0.296,
        570: 0.284,
        575: 0.271,
        580: 0.260,
        585: 0.247,
        590: 0.232,
        595: 0.220,
        600: 0.210,
        605: 0.200,
        610: 0.194,
        615: 0.189,
        620: 0.185,
        625: 0.183,
        630: 0.180,
        635: 0.177,
        640: 0.176,
        645: 0.175,
        650: 0.175,
        655: 0.175,
        660: 0.175,
        665: 0.177,
        670: 0.180,
        675: 0.183,
        680: 0.186,
        685: 0.189,
        690: 0.192,
        695: 0.195,
        700: 0.199,
        705: 0.200,
        710: 0.199,
        715: 0.198,
        720: 0.196,
        725: 0.195,
        730: 0.195,
        735: 0.196,
        740: 0.197,
        745: 0.200,
        750: 0.203,
        755: 0.205,
        760: 0.208,
        765: 0.212,
        770: 0.215,
        775: 0.217,
        780: 0.219,
        785: 0.222,
        790: 0.226,
        795: 0.231,
        800: 0.237,
        805: 0.243,
        810: 0.249,
        815: 0.257,
        820: 0.265,
        825: 0.273,
        830: 0.280
    },
    'TCS06': {
        360: 0.079,
        365: 0.081,
        370: 0.089,
        375: 0.113,
        380: 0.151,
        385: 0.203,
        390: 0.265,
        395: 0.339,
        400: 0.410,
        405: 0.464,
        410: 0.492,
        415: 0.508,
        420: 0.517,
        425: 0.524,
        430: 0.531,
        435: 0.538,
        440: 0.544,
        445: 0.551,
        450: 0.556,
        455: 0.556,
        460: 0.554,
        465: 0.549,
        470: 0.541,
        475: 0.531,
        480: 0.519,
        485: 0.504,
        490: 0.488,
        495: 0.469,
        500: 0.450,
        505: 0.431,
        510: 0.414,
        515: 0.395,
        520: 0.377,
        525: 0.358,
        530: 0.341,
        535: 0.325,
        540: 0.309,
        545: 0.293,
        550: 0.279,
        555: 0.265,
        560: 0.253,
        565: 0.241,
        570: 0.234,
        575: 0.227,
        580: 0.225,
        585: 0.222,
        590: 0.221,
        595: 0.220,
        600: 0.220,
        605: 0.220,
        610: 0.220,
        615: 0.220,
        620: 0.223,
        625: 0.227,
        630: 0.233,
        635: 0.239,
        640: 0.244,
        645: 0.251,
        650: 0.258,
        655: 0.263,
        660: 0.268,
        665: 0.273,
        670: 0.278,
        675: 0.281,
        680: 0.283,
        685: 0.286,
        690: 0.291,
        695: 0.296,
        700: 0.302,
        705: 0.313,
        710: 0.325,
        715: 0.338,
        720: 0.351,
        725: 0.364,
        730: 0.376,
        735: 0.389,
        740: 0.401,
        745: 0.413,
        750: 0.425,
        755: 0.436,
        760: 0.447,
        765: 0.458,
        770: 0.469,
        775: 0.477,
        780: 0.485,
        785: 0.493,
        790: 0.500,
        795: 0.506,
        800: 0.512,
        805: 0.517,
        810: 0.521,
        815: 0.525,
        820: 0.529,
        825: 0.532,
        830: 0.535
    },
    'TCS07': {
        360: 0.150,
        365: 0.177,
        370: 0.218,
        375: 0.293,
        380: 0.378,
        385: 0.459,
        390: 0.524,
        395: 0.546,
        400: 0.551,
        405: 0.555,
        410: 0.559,
        415: 0.560,
        420: 0.561,
        425: 0.558,
        430: 0.556,
        435: 0.551,
        440: 0.544,
        445: 0.535,
        450: 0.522,
        455: 0.506,
        460: 0.488,
        465: 0.469,
        470: 0.448,
        475: 0.429,
        480: 0.408,
        485: 0.385,
        490: 0.363,
        495: 0.341,
        500: 0.324,
        505: 0.311,
        510: 0.301,
        515: 0.291,
        520: 0.283,
        525: 0.273,
        530: 0.265,
        535: 0.260,
        540: 0.257,
        545: 0.257,
        550: 0.259,
        555: 0.260,
        560: 0.260,
        565: 0.258,
        570: 0.256,
        575: 0.254,
        580: 0.254,
        585: 0.259,
        590: 0.270,
        595: 0.284,
        600: 0.302,
        605: 0.324,
        610: 0.344,
        615: 0.362,
        620: 0.377,
        625: 0.389,
        630: 0.400,
        635: 0.410,
        640: 0.420,
        645: 0.429,
        650: 0.438,
        655: 0.445,
        660: 0.452,
        665: 0.457,
        670: 0.462,
        675: 0.466,
        680: 0.468,
        685: 0.470,
        690: 0.473,
        695: 0.477,
        700: 0.483,
        705: 0.489,
        710: 0.496,
        715: 0.503,
        720: 0.511,
        725: 0.518,
        730: 0.525,
        735: 0.532,
        740: 0.539,
        745: 0.546,
        750: 0.553,
        755: 0.559,
        760: 0.565,
        765: 0.570,
        770: 0.575,
        775: 0.578,
        780: 0.581,
        785: 0.583,
        790: 0.585,
        795: 0.587,
        800: 0.588,
        805: 0.589,
        810: 0.590,
        815: 0.590,
        820: 0.590,
        825: 0.591,
        830: 0.592
    },
    'TCS08': {
        360: 0.075,
        365: 0.078,
        370: 0.084,
        375: 0.090,
        380: 0.104,
        385: 0.129,
        390: 0.170,
        395: 0.240,
        400: 0.319,
        405: 0.416,
        410: 0.462,
        415: 0.482,
        420: 0.490,
        425: 0.488,
        430: 0.482,
        435: 0.473,
        440: 0.462,
        445: 0.450,
        450: 0.439,
        455: 0.426,
        460: 0.413,
        465: 0.397,
        470: 0.382,
        475: 0.366,
        480: 0.352,
        485: 0.337,
        490: 0.325,
        495: 0.310,
        500: 0.299,
        505: 0.289,
        510: 0.283,
        515: 0.276,
        520: 0.270,
        525: 0.262,
        530: 0.256,
        535: 0.251,
        540: 0.250,
        545: 0.251,
        550: 0.254,
        555: 0.258,
        560: 0.264,
        565: 0.269,
        570: 0.272,
        575: 0.274,
        580: 0.278,
        585: 0.284,
        590: 0.295,
        595: 0.316,
        600: 0.348,
        605: 0.384,
        610: 0.434,
        615: 0.482,
        620: 0.528,
        625: 0.568,
        630: 0.604,
        635: 0.629,
        640: 0.648,
        645: 0.663,
        650: 0.676,
        655: 0.685,
        660: 0.693,
        665: 0.700,
        670: 0.705,
        675: 0.709,
        680: 0.712,
        685: 0.715,
        690: 0.717,
        695: 0.719,
        700: 0.721,
        705: 0.720,
        710: 0.719,
        715: 0.722,
        720: 0.725,
        725: 0.727,
        730: 0.729,
        735: 0.730,
        740: 0.730,
        745: 0.730,
        750: 0.730,
        755: 0.730,
        760: 0.730,
        765: 0.730,
        770: 0.730,
        775: 0.730,
        780: 0.730,
        785: 0.730,
        790: 0.731,
        795: 0.731,
        800: 0.731,
        805: 0.731,
        810: 0.731,
        815: 0.731,
        820: 0.731,
        825: 0.731,
        830: 0.731
    },
    'TCS09': {
        360: 0.069,
        365: 0.072,
        370: 0.073,
        375: 0.070,
        380: 0.066,
        385: 0.062,
        390: 0.058,
        395: 0.055,
        400: 0.052,
        405: 0.052,
        410: 0.051,
        415: 0.050,
        420: 0.050,
        425: 0.049,
        430: 0.048,
        435: 0.047,
        440: 0.046,
        445: 0.044,
        450: 0.042,
        455: 0.041,
        460: 0.038,
        465: 0.035,
        470: 0.033,
        475: 0.031,
        480: 0.030,
        485: 0.029,
        490: 0.028,
        495: 0.028,
        500: 0.028,
        505: 0.029,
        510: 0.030,
        515: 0.030,
        520: 0.031,
        525: 0.031,
        530: 0.032,
        535: 0.032,
        540: 0.033,
        545: 0.034,
        550: 0.035,
        555: 0.037,
        560: 0.041,
        565: 0.044,
        570: 0.048,
        575: 0.052,
        580: 0.060,
        585: 0.076,
        590: 0.102,
        595: 0.136,
        600: 0.190,
        605: 0.256,
        610: 0.336,
        615: 0.418,
        620: 0.505,
        625: 0.581,
        630: 0.641,
        635: 0.682,
        640: 0.717,
        645: 0.740,
        650: 0.758,
        655: 0.770,
        660: 0.781,
        665: 0.790,
        670: 0.797,
        675: 0.803,
        680: 0.809,
        685: 0.814,
        690: 0.819,
        695: 0.824,
        700: 0.828,
        705: 0.830,
        710: 0.831,
        715: 0.833,
        720: 0.835,
        725: 0.836,
        730: 0.836,
        735: 0.837,
        740: 0.838,
        745: 0.839,
        750: 0.839,
        755: 0.839,
        760: 0.839,
        765: 0.839,
        770: 0.839,
        775: 0.839,
        780: 0.839,
        785: 0.839,
        790: 0.839,
        795: 0.839,
        800: 0.839,
        805: 0.839,
        810: 0.838,
        815: 0.837,
        820: 0.837,
        825: 0.836,
        830: 0.836
    },
    'TCS10': {
        360: 0.042,
        365: 0.043,
        370: 0.045,
        375: 0.047,
        380: 0.050,
        385: 0.054,
        390: 0.059,
        395: 0.063,
        400: 0.066,
        405: 0.067,
        410: 0.068,
        415: 0.069,
        420: 0.069,
        425: 0.070,
        430: 0.072,
        435: 0.073,
        440: 0.076,
        445: 0.078,
        450: 0.083,
        455: 0.088,
        460: 0.095,
        465: 0.103,
        470: 0.113,
        475: 0.125,
        480: 0.142,
        485: 0.162,
        490: 0.189,
        495: 0.219,
        500: 0.262,
        505: 0.305,
        510: 0.365,
        515: 0.416,
        520: 0.465,
        525: 0.509,
        530: 0.546,
        535: 0.581,
        540: 0.610,
        545: 0.634,
        550: 0.653,
        555: 0.666,
        560: 0.678,
        565: 0.687,
        570: 0.693,
        575: 0.698,
        580: 0.701,
        585: 0.704,
        590: 0.705,
        595: 0.705,
        600: 0.706,
        605: 0.707,
        610: 0.707,
        615: 0.707,
        620: 0.708,
        625: 0.708,
        630: 0.710,
        635: 0.711,
        640: 0.712,
        645: 0.714,
        650: 0.716,
        655: 0.718,
        660: 0.720,
        665: 0.722,
        670: 0.725,
        675: 0.729,
        680: 0.731,
        685: 0.735,
        690: 0.739,
        695: 0.742,
        700: 0.746,
        705: 0.748,
        710: 0.749,
        715: 0.751,
        720: 0.753,
        725: 0.754,
        730: 0.755,
        735: 0.755,
        740: 0.755,
        745: 0.755,
        750: 0.756,
        755: 0.757,
        760: 0.758,
        765: 0.759,
        770: 0.759,
        775: 0.759,
        780: 0.759,
        785: 0.759,
        790: 0.759,
        795: 0.759,
        800: 0.759,
        805: 0.759,
        810: 0.758,
        815: 0.757,
        820: 0.757,
        825: 0.756,
        830: 0.756
    },
    'TCS11': {
        360: 0.074,
        365: 0.079,
        370: 0.086,
        375: 0.098,
        380: 0.111,
        385: 0.121,
        390: 0.127,
        395: 0.129,
        400: 0.127,
        405: 0.121,
        410: 0.116,
        415: 0.112,
        420: 0.108,
        425: 0.105,
        430: 0.104,
        435: 0.104,
        440: 0.105,
        445: 0.106,
        450: 0.110,
        455: 0.115,
        460: 0.123,
        465: 0.134,
        470: 0.148,
        475: 0.167,
        480: 0.192,
        485: 0.219,
        490: 0.252,
        495: 0.291,
        500: 0.325,
        505: 0.347,
        510: 0.356,
        515: 0.353,
        520: 0.346,
        525: 0.333,
        530: 0.314,
        535: 0.294,
        540: 0.271,
        545: 0.248,
        550: 0.227,
        555: 0.206,
        560: 0.188,
        565: 0.170,
        570: 0.153,
        575: 0.138,
        580: 0.125,
        585: 0.114,
        590: 0.106,
        595: 0.100,
        600: 0.096,
        605: 0.092,
        610: 0.090,
        615: 0.087,
        620: 0.085,
        625: 0.082,
        630: 0.080,
        635: 0.079,
        640: 0.078,
        645: 0.078,
        650: 0.078,
        655: 0.078,
        660: 0.081,
        665: 0.083,
        670: 0.088,
        675: 0.093,
        680: 0.102,
        685: 0.112,
        690: 0.125,
        695: 0.141,
        700: 0.161,
        705: 0.182,
        710: 0.203,
        715: 0.223,
        720: 0.242,
        725: 0.257,
        730: 0.270,
        735: 0.282,
        740: 0.292,
        745: 0.302,
        750: 0.310,
        755: 0.314,
        760: 0.317,
        765: 0.323,
        770: 0.330,
        775: 0.334,
        780: 0.338,
        785: 0.343,
        790: 0.348,
        795: 0.353,
        800: 0.359,
        805: 0.365,
        810: 0.372,
        815: 0.380,
        820: 0.388,
        825: 0.396,
        830: 0.403
    },
    'TCS12': {
        360: 0.189,
        365: 0.175,
        370: 0.158,
        375: 0.139,
        380: 0.120,
        385: 0.103,
        390: 0.090,
        395: 0.082,
        400: 0.076,
        405: 0.068,
        410: 0.064,
        415: 0.065,
        420: 0.075,
        425: 0.093,
        430: 0.123,
        435: 0.160,
        440: 0.207,
        445: 0.256,
        450: 0.300,
        455: 0.331,
        460: 0.346,
        465: 0.347,
        470: 0.341,
        475: 0.328,
        480: 0.307,
        485: 0.282,
        490: 0.257,
        495: 0.230,
        500: 0.204,
        505: 0.178,
        510: 0.154,
        515: 0.129,
        520: 0.109,
        525: 0.090,
        530: 0.075,
        535: 0.062,
        540: 0.051,
        545: 0.041,
        550: 0.035,
        555: 0.029,
        560: 0.025,
        565: 0.022,
        570: 0.019,
        575: 0.017,
        580: 0.017,
        585: 0.017,
        590: 0.016,
        595: 0.016,
        600: 0.016,
        605: 0.016,
        610: 0.016,
        615: 0.016,
        620: 0.016,
        625: 0.016,
        630: 0.018,
        635: 0.018,
        640: 0.018,
        645: 0.018,
        650: 0.019,
        655: 0.020,
        660: 0.023,
        665: 0.024,
        670: 0.026,
        675: 0.030,
        680: 0.035,
        685: 0.043,
        690: 0.056,
        695: 0.074,
        700: 0.097,
        705: 0.128,
        710: 0.166,
        715: 0.210,
        720: 0.257,
        725: 0.305,
        730: 0.354,
        735: 0.401,
        740: 0.446,
        745: 0.485,
        750: 0.520,
        755: 0.551,
        760: 0.577,
        765: 0.599,
        770: 0.618,
        775: 0.633,
        780: 0.645,
        785: 0.656,
        790: 0.666,
        795: 0.674,
        800: 0.680,
        805: 0.686,
        810: 0.691,
        815: 0.694,
        820: 0.697,
        825: 0.700,
        830: 0.702
    },
    'TCS13': {
        360: 0.071,
        365: 0.076,
        370: 0.082,
        375: 0.090,
        380: 0.104,
        385: 0.127,
        390: 0.161,
        395: 0.211,
        400: 0.264,
        405: 0.313,
        410: 0.341,
        415: 0.352,
        420: 0.359,
        425: 0.361,
        430: 0.364,
        435: 0.365,
        440: 0.367,
        445: 0.369,
        450: 0.372,
        455: 0.374,
        460: 0.376,
        465: 0.379,
        470: 0.384,
        475: 0.389,
        480: 0.397,
        485: 0.405,
        490: 0.416,
        495: 0.429,
        500: 0.443,
        505: 0.454,
        510: 0.461,
        515: 0.466,
        520: 0.469,
        525: 0.471,
        530: 0.474,
        535: 0.476,
        540: 0.483,
        545: 0.490,
        550: 0.506,
        555: 0.526,
        560: 0.553,
        565: 0.582,
        570: 0.618,
        575: 0.651,
        580: 0.680,
        585: 0.701,
        590: 0.717,
        595: 0.729,
        600: 0.736,
        605: 0.742,
        610: 0.745,
        615: 0.747,
        620: 0.748,
        625: 0.748,
        630: 0.748,
        635: 0.748,
        640: 0.748,
        645: 0.748,
        650: 0.748,
        655: 0.748,
        660: 0.747,
        665: 0.747,
        670: 0.747,
        675: 0.747,
        680: 0.747,
        685: 0.747,
        690: 0.747,
        695: 0.746,
        700: 0.746,
        705: 0.746,
        710: 0.745,
        715: 0.744,
        720: 0.743,
        725: 0.744,
        730: 0.745,
        735: 0.748,
        740: 0.750,
        745: 0.750,
        750: 0.749,
        755: 0.748,
        760: 0.748,
        765: 0.747,
        770: 0.747,
        775: 0.747,
        780: 0.747,
        785: 0.746,
        790: 0.746,
        795: 0.746,
        800: 0.746,
        805: 0.745,
        810: 0.745,
        815: 0.745,
        820: 0.745,
        825: 0.745,
        830: 0.745
    },
    'TCS14': {
        360: 0.036,
        365: 0.036,
        370: 0.036,
        375: 0.036,
        380: 0.036,
        385: 0.036,
        390: 0.037,
        395: 0.038,
        400: 0.039,
        405: 0.039,
        410: 0.040,
        415: 0.041,
        420: 0.042,
        425: 0.042,
        430: 0.043,
        435: 0.044,
        440: 0.044,
        445: 0.045,
        450: 0.045,
        455: 0.046,
        460: 0.047,
        465: 0.048,
        470: 0.050,
        475: 0.052,
        480: 0.055,
        485: 0.057,
        490: 0.062,
        495: 0.067,
        500: 0.075,
        505: 0.083,
        510: 0.092,
        515: 0.100,
        520: 0.108,
        525: 0.121,
        530: 0.133,
        535: 0.142,
        540: 0.150,
        545: 0.154,
        550: 0.155,
        555: 0.152,
        560: 0.147,
        565: 0.140,
        570: 0.133,
        575: 0.125,
        580: 0.118,
        585: 0.112,
        590: 0.106,
        595: 0.101,
        600: 0.098,
        605: 0.095,
        610: 0.093,
        615: 0.090,
        620: 0.089,
        625: 0.087,
        630: 0.086,
        635: 0.085,
        640: 0.084,
        645: 0.084,
        650: 0.084,
        655: 0.084,
        660: 0.085,
        665: 0.087,
        670: 0.092,
        675: 0.096,
        680: 0.102,
        685: 0.110,
        690: 0.123,
        695: 0.137,
        700: 0.152,
        705: 0.169,
        710: 0.188,
        715: 0.207,
        720: 0.226,
        725: 0.243,
        730: 0.260,
        735: 0.277,
        740: 0.294,
        745: 0.310,
        750: 0.325,
        755: 0.339,
        760: 0.353,
        765: 0.366,
        770: 0.379,
        775: 0.390,
        780: 0.399,
        785: 0.408,
        790: 0.416,
        795: 0.422,
        800: 0.428,
        805: 0.434,
        810: 0.439,
        815: 0.444,
        820: 0.448,
        825: 0.451,
        830: 0.454
    }
}

TCS_SDS = CaseInsensitiveMapping(
    dict((key, SpectralDistribution(value, name=key))
         for key, value in TCS_SDS_DATA.items()))
"""
Test colour samples spectral distributions.

References
----------
:cite:`Ohno2008a`

TCS_SDS : CaseInsensitiveMapping
"""
