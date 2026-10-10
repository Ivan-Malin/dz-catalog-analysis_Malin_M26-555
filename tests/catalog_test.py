# Популярный грязный хак по импорту проекта
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
                                   
from catalog_analysis import (
    average_rating,
    catalog_age_stats,
    duration_in_hours,
    movies,
)


def test_avg() -> None:
    assert average_rating(movies) == 7.2


def test_catalog_age_stats() -> None:
    min_year, max_year, avg_year = catalog_age_stats(movies)
    assert min_year == 15
    assert max_year == 2
    assert avg_year == 7


def test_duration_in_hours() -> None:
    assert duration_in_hours(121) == "2ч 1м"
    assert duration_in_hours(1) == "0ч 1м"