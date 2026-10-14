import pytest

from trips.risk import Risk, wind_level, rain_level, snow_level

@pytest.mark.parametrize(
    "mph, expected",
    [(0, Risk.LOW),
     (24.9, Risk.LOW),
     (25, Risk.MODERATE),
     (34.9, Risk.MODERATE),
     (35, Risk.HIGH),
     (44.9, Risk.HIGH),
     (45, Risk.SEVERE),
     (54.9, Risk.SEVERE),
     (55, Risk.NO_TRAVEL),
     (80, Risk.NO_TRAVEL)
     ],
)

def test_wind_level(mph, expected):
    assert wind_level(mph) == expected

@pytest.mark.parametrize(
    "inches_per_hour, expected",
    [(0, Risk.LOW),
     (0.09, Risk.LOW),
     (0.1, Risk.MODERATE),
     (0.24,Risk.MODERATE),
     (0.25, Risk.HIGH),
     (0.49, Risk.HIGH),
     (0.5, Risk.SEVERE),
     (1, Risk.SEVERE),
     (1.01, Risk.NO_TRAVEL),
     ],
)

def test_rain_level(inches_per_hour, expected):
    assert rain_level(inches_per_hour) == expected

@pytest.mark.parametrize(
    "inches_per_hour, expected",
    [(0, Risk.LOW),
     (0.49, Risk.LOW),
     (0.5, Risk.MODERATE),
     (0.99, Risk.MODERATE),
     (1, Risk.HIGH),
     (1.99, Risk.HIGH),
     (2, Risk.SEVERE),
     (3, Risk.SEVERE),
     (3.01, Risk.NO_TRAVEL)
     ],
)

def test_snow_level(inches_per_hour, expected):
   assert snow_level(inches_per_hour) == expected