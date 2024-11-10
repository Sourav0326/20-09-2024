def list_animals():
    return "Dog", "Cat", "Cow", "Lion"


def animal_sound(animal):
    sounds = {
        "Dog": "bark",
        "Cat": "meow",
        "Cow": "moo",
        "Lion": "roar"
    }
    return sounds.get(animal, "unknown sound")

animals = list_animals()
for animal in animals:
    sound = animal_sound(animal)
    print(f"A {animal} {sound}.")