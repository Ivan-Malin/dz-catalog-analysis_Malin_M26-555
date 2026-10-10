# Популярный грязный хак по импорту проекта
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
                                   
from catalog_analysis import (
    average_rating,
    catalog_age_stats,
    decade_label,
    duration_in_hours,
    format_report_line,
    make_slug,
    movies,
    normalize_title,
    rating_tier,
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

def test_rating_tier() -> None:
    assert rating_tier(9) == "шедевр"
    assert rating_tier(8.9999) == "хорошо"
    assert rating_tier(6.5) == "средне"
    assert rating_tier(4) == "слабо"

def test_decade_label() -> None:
    assert decade_label(2020) == "новые"
    assert decade_label(2017) == "недавние"
    assert decade_label(2014) == "старые"

def test_normalize_title() -> None:
    assert normalize_title("каждый") == "Каждый"
    assert normalize_title("каждый ДеНь") == "Каждый День"

def test_make_slug() -> None:
    assert make_slug("Каждый День") == "каждый-день"
    assert make_slug("Кони и Ко") == "кони-и-ко"

def test_format_report_line() -> None:
    assert (format_report_line(movies[7]) ==
            '"The Quiet Algorithm" (2024) - 9.2/10, 1ч 58м, жанры: drama, sci-fi')