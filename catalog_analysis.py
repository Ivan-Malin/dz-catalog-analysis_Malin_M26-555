"""Анализ каталога фильмов."""

import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies: list) -> float:
    """Возвращает среднюю оценку по каталогу

    Args:
        movies (list): каталог

    Returns:
        float: средняя оценка по каталогу
    """

    assert isinstance(movies, list), "movies должен быть каталогом фильмов"

    # Использует реккурентную формулу
    avg_rating = 0

    for i in range(len(movies)):
        movie = movies[i]
        assert isinstance(movie, dict), (
            "movies содержит неверный формат представления фильмов"
        )
        assert "rating" in movie, (
            "movies содержит неверный формат представления фильмов"
        )
        assert isinstance(movie["rating"], (int, float)), (
            "movies содержит неверный формат представления фильмов"
        )

        avg_rating += (movie["rating"] - avg_rating) / (i + 1)

    return round(avg_rating, 1)


def catalog_age_stats(movies: list, current_year: int = 2026) -> tuple:
    """Возвращает самый старый, самый новый фильм и среднее

    Args:
        movies (list): каталог
        current_year (int, optional): текущий год. По умолчанию 2026.

    Returns:
        tuple: кортеж (самый старый фильм в годах, самый новый фильм в годах, среднее)
    """

    assert isinstance(movies, list), "movies должен быть каталогом фильмов"

    # Использует реккурентную формулу рассчёта среднего
    min_year = float("inf")
    avg_year = 0
    max_year = float("-inf")

    for i in range(len(movies)):
        movie = movies[i]

        assert isinstance(movie, dict), (
            "movies содержит неверный формат представления фильмов"
        )
        assert "year" in movie, "movies содержит неверный формат представления фильмов"
        assert isinstance(movie["year"], int), (
            "movies содержит неверный формат представления фильмов"
        )

        year = movie["year"]

        min_year = min(year, min_year)
        avg_year += (year - avg_year) / (i + 1)
        max_year = max(year, max_year)

    return (
        current_year - min_year,
        current_year - max_year,
        current_year - math.ceil(avg_year),
    )


def duration_in_hours(minutes: int) -> str:
    """Переводит минуты в формат "2ч 35м"

    Args:
        minutes (int | float): минуты

    Returns:
        str: строка времени формата "2ч 35м"
    """
    
    assert isinstance(minutes, int), "minutes должно быть целочисленным"
    
    return f"{minutes // 60}ч {minutes % 60}м"


def main() -> None:
    """Точка входа программы."""
    print("Hello from dz-catalog-analysis-malin-m26-555!")


# Tests
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


if __name__ == "__main__":
    test_duration_in_hours()
