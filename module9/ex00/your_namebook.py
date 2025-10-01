#!/usr/bin/env python3

def array_of_names(persons):
    namebook = []
    for name, lastname in persons.items():
        full_name = (f"{name.capitalize()} {lastname.capitalize()}")
        namebook.append(full_name)
    return namebook
persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
}

print(array_of_names(persons))
