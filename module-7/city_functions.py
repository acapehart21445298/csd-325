def city_country(city, country, population=None, language=None):
    """Return a city, country, population, and language."""
    result = f"{city}, {country}"

    if population:
        result += f" - population {population}"

    if language:
        result += f", {language}"

    return result


print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France", 2100000))
print(city_country("Tokyo", "Japan", 14000000, "Japanese"))