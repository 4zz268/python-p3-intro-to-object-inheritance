import pytest
from inheritance_example import Animal, Dog, Collar, PetDog, Parrot

def test_animal_speak():
    animal = Animal("Generic")
    assert animal.speak() == "Generic makes a sound."

def test_dog_inheritance():
    dog = Dog("Fido", "Beagle")
    assert dog.speak() == "Fido barks!"
    assert dog.info() == "Fido is a Beagle."

def test_collar_composition():
    collar = Collar("blue")
    assert collar.describe() == "Collar color: blue"

def test_petdog_composition():
    petdog = PetDog("Max", "Bulldog", "green")
    assert petdog.speak() == "Max barks!"
    assert petdog.info() == "Max is a Bulldog."
    assert petdog.show_collar() == "Collar color: green"

def test_parrot_decorator():
    parrot = Parrot("Polly")
    assert parrot.speak() == "Polly says hello!!!"
