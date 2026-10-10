"""Анализ каталога фильмов."""

import math
from collections.abc import Iterable

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

BEST_RATING = 9
GOOD_RATING = 7
MID_RATING = 5

MID_FILM_YEAR = 2020
OLD_FILM_YEAR = 2015


def check_if_movie_is_valid(movie: dict) -> None:
    """Вызывает ошибку, если movie не является словарём описания фильма.

    Args:
        movie (dict): описание фильма

    """
    msg = "'movie' должен быть корректным описанием фильма."

    if not isinstance(movie, dict):
        raise TypeError(msg)

    if not (
        isinstance(movie.get("title"), str)
        and isinstance(movie.get("genres"), set)
        and isinstance(movie.get("actors"), list)
        and isinstance(movie.get("rating"), (float, int))
        and not isinstance(movie.get("rating"), bool)
        and isinstance(movie.get("year"), int)
        and not isinstance(movie.get("year"), bool)
        and isinstance(movie.get("duration_min"), int)
        and not isinstance(movie.get("duration_min"), bool)
    ):
        raise TypeError(msg)

    if not (
        all(isinstance(g, str) for g in movie["genres"])
        and all(isinstance(a, str) for a in movie["actors"])
    ):
        raise TypeError(msg)


def check_if_catalog_is_valid(movies: list) -> None:
    """Вызывает ошибку, если movies не является корректным каталогом фильмов.

    Каталог фильмов слабоструктурирован. По-хорошему его изначально нужно
    предобработать и перевести в нормальную структуру, но т.к. по условию
    задачи этого не сделать, то его нужно проверить на валидность.
    Предположим, что эта проверка быстрая (что было бы так, если бы мы
    предобработали и перевели каталог в адекватную структуру) и её
    допускается вызывать в каждой функции (т.к. это необходимо), тогда...
    Будем её так и использовать.

    Args:
        movies (list): каталог фильмов

    """
    msg = "'movies' должен быть каталогом фильмов."
    if not isinstance(movies, list):
        raise TypeError(msg)

    for movie in movies:
        try:
            check_if_movie_is_valid(movie)
        except TypeError as ex:
            raise TypeError(msg) from ex


# 1. Часть


def average_rating(movies: list) -> float:
    """Возвращает среднюю оценку по каталогу.

    Args:
        movies (list): каталог

    Returns:
        float: средняя оценка по каталогу

    """
    check_if_catalog_is_valid(movies)

    # Использует реккурентную формулу рассчёта среднего
    avg_rating = 0

    for i in range(len(movies)):
        movie = movies[i]

        avg_rating += (movie["rating"] - avg_rating) / (i + 1)

    return round(avg_rating, 1)


def catalog_age_stats(movies: list, current_year: int = 2026) -> tuple:
    """Возвращает самый старый, самый новый фильм и среднее.

    Args:
        movies (list): каталог
        current_year (int, optional): текущий год. По умолчанию 2026.

    Returns:
        tuple: кортеж (самый старый фильм в годах, самый новый фильм в годах, среднее)

    """
    check_if_catalog_is_valid(movies)

    # Использует реккурентную формулу рассчёта среднего
    min_year = float("inf")
    avg_year = 0
    max_year = float("-inf")

    for i in range(len(movies)):
        movie = movies[i]

        year = movie["year"]

        min_year = min(year, min_year)
        avg_year += (year - avg_year) / (i + 1)
        max_year = max(year, max_year)

    return (
        current_year - min_year,
        current_year - max_year,
        math.ceil(current_year - avg_year),
    )


def duration_in_hours(minutes: int) -> str:
    """Переводит минуты в формат "2ч 35м".

    Args:
        minutes (int | float): минуты

    Returns:
        str: строка времени формата "2ч 35м"

    """
    if not isinstance(minutes, int):
        msg = "'minutes' должно быть целочисленным"
        raise TypeError(msg)

    return f"{minutes // 60}ч {minutes % 60}м"


# 2. Часть


def rating_tier(rating: float) -> str:
    """Возвращает категорию по оценке.

    Категории: "шедевр" (≥9), "хорошо" (7-8.9), "средне" (5-6.9), "слабо" (<5).

    Args:
        rating (float): оценка

    Returns:
        str: категория

    """
    if not isinstance(rating, (int | float)):
        msg = "'rating' должно быть числом"
        raise TypeError(msg)

    tier = None

    if rating >= GOOD_RATING:
        tier = "шедевр" if rating >= BEST_RATING else "хорошо"
    elif rating >= MID_RATING:
        tier = "средне"
    else:
        tier = "слабо"

    return tier


def decade_label(year: int) -> str:
    """Возвращает оценку старости фильму.

    Args:
        year (int): год фильма

    Returns:
        str: оценка старости

    """
    if not isinstance(year, int):
        msg = "'year' должно быть целым числом"
        raise TypeError(msg)

    match year:
        case _ if year >= MID_FILM_YEAR:
            return "новые"
        case _ if year >= OLD_FILM_YEAR:
            return "недавние"
        case _:
            return "старые"


# 3. Часть


# Замечание - названия этой функции в ДЗ нет, выбрано произвольное
def print_some_data(movies: list) -> None:
    """Выводит не комедии и один из шедевров среди всех фильмов.

    Args:
        movies (list): каталог фильмов

    """
    check_if_catalog_is_valid(movies)

    print("Комедии:")
    for movie in movies:
        if "comedy" not in movie["genres"]:
            continue
        print(f"- {movie['title']}")
    print()

    i = 0
    while i < len(movies):
        movie = movies[i]
        if not isinstance(movie, dict):
            msg = "'movies' должен быть каталогом фильмов"
            raise TypeError(msg)
        if "genres" not in movie:
            msg = "'movies' должен быть каталогом фильмов"
            raise TypeError(msg)
        if not isinstance(movie["genres"], set):
            msg = "'movies' должен быть каталогом фильмов"
            raise TypeError(msg)

        movies[i]
        i += 1
    print("Шедевров не найдено")


# 4. Часть
def normalize_title(title: str) -> str:
    """Приводит строку к Title Case.

    Args:
        title (str): название фильма

    Returns:
        str: название фильма в Title Case

    """
    if not isinstance(title, str):
        msg = "'title' должен быть str"
        raise TypeError(msg)

    new_words = [word[0].upper() + word[1:].lower() for word in title.split(" ")]

    return " ".join(new_words)


def make_slug(title: str) -> str:
    """Приводит строку к slug.

    Пример slug: "the-quiet-algorithm"

    Args:
        title (str): название фильма

    Returns:
        str: название фильма в формате slug

    """
    if not isinstance(title, str):
        msg = "'title' должен быть str"
        raise TypeError(msg)

    new_words = [word.lower() for word in title.split(" ")]

    # Хз зачем тут replace, но так требует условие задачи...
    return " ".join(new_words).replace(" ", "-")


def format_report_line(movie: dict) -> str:
    """Возвращает описание фильма.

    Args:
        movie (dict): словарь описания фильма

    Returns:
        str: строка с описанием фильма

    """
    check_if_movie_is_valid(movie)

    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    # Результат join'а set не идемпотентен (итерируется каждый раз по разному)
    genres = ", ".join(
        sorted(movie["genres"]),
    )

    return f'"{title}" ({year}) - {rating}/10, {duration}, жанры: {genres}'


# 5. Часть
def titles_sorted_by_rating(movies: list) -> list:
    """Сортирует фильмы по убыванию рейтинга.

    Args:
        movies (list): каталог фильмов

    Returns:
        list: список названий фильмов

    """
    check_if_catalog_is_valid(movies)

    return [
        m["title"]
        for m in sorted(
            movies,
            key=lambda m: m["rating"],
            reverse=True,
        )
    ]


def top_n_by_rating(movies: list, n: int = 3) -> list:
    """Находит топ n фильмов.

    Args:
        movies (list): каталог фильмов
        n (int, optional): количество фильмов в топе. По умолчанию 3.

    Returns:
        list: список первых n пар (title, rating) в порядке убывания рейтинга

    """
    check_if_catalog_is_valid(movies)

    return [
        (m["title"], m["rating"])
        for m in sorted(
            movies,
            key=lambda m: m["rating"],
            reverse=True,
        )
    ][:n]


# 6. Часть


def count_by_genre(movies: list) -> dict:
    """Возвращает количество фильмов в каждом жанре.

    Args:
        movies (list): каталог фильмов

    Returns:
        dict: словарь формата {жанр: количество фильмов}

    """
    check_if_catalog_is_valid(movies)

    genre_info = {}
    for movie in movies:
        for genre in movie["genres"]:
            # ХЗ куда его ещё можно было впихнуть...
            genre_info[genre] = genre_info.get(genre, 0) + 1
    return genre_info


def actor_filmography(movies: list) -> dict:
    """Возвращает фильмографию актёров.

    Args:
        movies (list): каталог фильмов

    Returns:
        dict: словарь формата {актер: [список названий фильмов]}

    """
    check_if_catalog_is_valid(movies)

    actor_info = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in actor_info:
                actor_info[actor] = []
            actor_info[actor].append(movie["title"])

    return actor_info


# Замечание - названия этой функции в ДЗ нет, выбрано произвольное
def calc_more_than_avg(movies: list) -> dict:
    """Возвращает фильмы с оценкой выше средней.

    Args:
        movies (list): каталог фильмов

    Returns:
        dict: словарь формата {title: rating}

    """
    check_if_catalog_is_valid(movies)

    avg = average_rating(movies)

    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}


# 7. Часть


def all_genres(movies: list) -> set:
    """Находит множество всех уникальных жанров каталога.

    Args:
        movies (list): каталог фильмов

    Returns:
        set: множество уникальных жанров каталога

    """
    check_if_catalog_is_valid(movies)

    _all_genres = set()
    for movie in movies:
        _all_genres |= movie["genres"]

    return _all_genres


def common_actors(movie1: dict, movie2: dict) -> set:
    """Возвращает множество актеров, снимавшихся в обоих фильмах.

    Args:
        movie1 (dict): фильм
        movie2 (dict): фильм

    Returns:
        set: множество имён актёров (str)

    """
    check_if_movie_is_valid(movie1)
    check_if_movie_is_valid(movie2)

    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a: list, movies_b: list) -> set:
    """Возвращает жанры, встречающиеся в movies_a, но не в movies_b.

    Args:
        movies_a (dict): каталог фильмов
        movies_b (dict): каталог фильмов

    Returns:
        set: множество имён актёров (str)

    """
    check_if_catalog_is_valid(movies_a)
    check_if_catalog_is_valid(movies_b)

    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)

    return genres_a - genres_b


# 8. Часть


def iter_high_rated(movies: list, min_rating: float = 8.0) -> Iterable[dict]:
    """Лениво отдает фильмы с рейтингом не ниже min_rating.

    Args:
        movies (list): каталог фильмов
        min_rating (float, optional): минимальный рейтинг. По умолчанию 8.0.

    Returns:
        Iterable[dict]: итератор каталога фильмов

    """
    check_if_catalog_is_valid(movies)

    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


# Замечание - названия этой функции в ДЗ нет, выбрано произвольное
def show_iter_high_rated_work() -> list[str]:
    """Демонстрирует работу iter_high_rated.

    Returns:
        list[str]: список описаний наиболее оценённых фильмов

    """
    result = []
    for movie in iter_high_rated(movies):
        line = format_report_line(movie)
        print(line)
        result.append(line)

    return result


# Замечание - названия этой функции в ДЗ нет, выбрано произвольное
def show_generated_sum() -> int:
    """Демонстрирует работу iter_high_rated.

    Returns:
        int: суммарное время для просмотра всех наиболее оценённых фильмов

    """
    min_rating = 7
    result = sum(m["duration_min"] for m in movies if m["rating"] > min_rating)

    print(result)

    return result


# 9. Часть


def build_report(movies: list) -> None:
    """Выводить отчёт по каталогу фильмов.

    Args:
        movies (list): каталог фильмов

    """
    avg_rating = average_rating(movies)
    avg_age = catalog_age_stats(movies)[2]

    # Лучше, конечно, заново функцию адекватную именно под эту задачу реализовать...
    best_3_films = [
        next(m for m in movies if m["title"] == title)
        for title, rating in top_n_by_rating(movies)
    ]
    top_n_films = [format_report_line(f) for f in best_3_films]

    genres_count = sorted(
        count_by_genre(movies).items(),
        key=lambda gc: gc[1],
        reverse=True,
    )
    _all_genres = sorted(
        all_genres(movies),
    )

    print(
        f"""ОТЧЁТ ПО КАТАЛОГУ
Средний рейтинг: {avg_rating}
Средний возраст фильмов: {avg_age} лет

Топ-3 фильма:
  {"\n  ".join(top_n_films)}

Фильмов по жанрам:
  {"\n  ".join(f"{g[0]} - {g[1]}" for g in genres_count)}

Все жанры каталога: {", ".join(_all_genres)}
""",
    )


if __name__ == "__main__":
    build_report(movies)
