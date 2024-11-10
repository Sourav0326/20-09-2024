def list_planets():
    return "Mercury", "Venus", "Earth", "Mars"


def distance_from_sun(planet):
    distance = {
        "Mercury": "63.883 million km",
        "Venus": "108.79 million km",
        "Earth": "149.54 million km",
        "Mars": "227.23 million km"
    }
    return distance.get(planet,"unknown distance")

planets = list_planets()
for planet in planets:
    dis = distance_from_sun(planet)
    print(f"{planet} is {dis} away from the sun")