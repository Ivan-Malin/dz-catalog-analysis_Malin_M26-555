# Популярный грязный хак по импорту проекта
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
                                   
from catalog_analysis import (
    actor_filmography,
    all_genres,
    average_rating,
    calc_more_than_avg,
    catalog_age_stats,
    common_actors,
    count_by_genre,
    decade_label,
    duration_in_hours,
    format_report_line,
    genres_only_in_one,
    make_slug,
    movies,
    normalize_title,
    rating_tier,
    titles_sorted_by_rating,
    top_n_by_rating,
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

def test_titles_sorted_by_rating() -> None:
    sorted_titles = [
        'The Quiet Algorithm', 
        'midnight in oslo', 
        'The Dune Chronicles', 
        'The Last Bakery', 
        'Red Harbor', 
        'Kitchen Stories', 
        'silent hours', 
        'Two Left Shoes', 
        'Comet Racers', 
        'Garden of Static'
    ]
    sorted_titles_calculated = titles_sorted_by_rating(movies)
    # Сравнение листов в питоне идёт по элементно
    assert list(sorted_titles_calculated) == list(sorted_titles)

def test_top_n_by_rating() -> None:
    top_n = [
        ("The Quiet Algorithm", 9.2),
        ("midnight in oslo", 8.9),
        ("The Dune Chronicles", 8.6)
    ]
    top_n_calculated = top_n_by_rating(movies)
    # Сравнение tuple в питоне идёт по элементно
    assert list(top_n_calculated) == list(top_n)

def test_count_by_genre() -> None:
    genre_info = {
        "drama": 5,
        "sci-fi": 3,
        "comedy": 3,
        "thriller": 3,
        "action": 2,
        "mystery": 1
    } 
    genre_info_calculated = count_by_genre(movies)
    assert genre_info_calculated == genre_info

def test_actor_filmography() -> None:
    actor_info = {
        "T. Chalamet": ["The Dune Chronicles", "The Last Bakery", "Red Harbor"],
        "R. Ferguson": ["The Dune Chronicles", "midnight in oslo"],
        "O. Isaac": ["The Dune Chronicles", "Comet Racers", "The Quiet Algorithm"],
        "A. Novak": ["Kitchen Stories", "The Last Bakery", "Two Left Shoes"],
        "M. Ferguson": ["Kitchen Stories", "The Quiet Algorithm"],
        "J. Bloom": ["silent hours", "Garden of Static"],
        "K. Lee": ["silent hours", "midnight in oslo", "Two Left Shoes"],
        "P. Diaz": ["Comet Racers", "Garden of Static", "Red Harbor"],
    }
    actor_info_calculated = actor_filmography(movies)
    assert actor_info_calculated == actor_info

def test_calc_more_than_avg() -> None:
    more_than_avg = {
        'The Dune Chronicles': 8.6,
        'The Last Bakery': 7.8,
        'midnight in oslo': 8.9,
        'The Quiet Algorithm': 9.2,
        'Red Harbor': 7.3,
    }
    more_than_avg_calculated = calc_more_than_avg(movies)
    assert more_than_avg_calculated == more_than_avg

def test_all_genres() -> None:
    _all_genres = {'action', 'comedy', 'drama', 'mystery', 'sci-fi', 'thriller'}
    all_genres_calculated = all_genres(movies)
    assert all_genres_calculated == _all_genres

def test_common_actors() -> None:
    _common_actors = {"O. Isaac"}
    common_actors_calculated = common_actors(movies[0], movies[3])
    assert common_actors_calculated == _common_actors

def test_genres_only_in_one() -> None:
    genres = {"mystery"} 
    genres_calculated = genres_only_in_one(movies[5:6], movies[:5])
    assert genres_calculated == genres