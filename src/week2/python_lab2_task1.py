
def average(values):
    """Return the average of values, or 0.0 if empty."""
    if not values:
        return 0.0

    return sum(values) / len(values)


def largest_city(populations):
    """Return the city with the largest population."""
    if not populations:
        return ("", 0)

    largest_name = ""
    largest_population = -1

    for city, population in populations.items():
        if population > largest_population:
            largest_name = city
            largest_population = population

    return (largest_name, largest_population)


def smallest_city(populations):
    """Return the city with the smallest population."""
    if not populations:
        return ("", 0)

    smallest_name = ""
    smallest_population = None

    for city, population in populations.items():
        if smallest_population is None or population < smallest_population:
            smallest_name = city
            smallest_population = population

    return (smallest_name, smallest_population)


def total_population(populations):
    """Return the sum of all populations."""
    return sum(populations.values())


if __name__ == "__main__":

    temperatures = [4.5, 6.2, 3.8, 7.1, 5.4, 2.9, 8.0]

    city_population = {
        "Riga": 605000,
        "Daugavpils": 78000,
        "Liepaja": 67000,
        "Jelgava": 55000,
        "Jurmala": 50000
    }

    print(f"Average temperature: {average(temperatures):.1f}")

    largest = largest_city(city_population)
    print(f"Largest city: {largest[0]} - {largest[1]}")

    smallest = smallest_city(city_population)
    print(f"Smallest city: {smallest[0]} - {smallest[1]}")

    print(f"Total population: {total_population(city_population)}")
