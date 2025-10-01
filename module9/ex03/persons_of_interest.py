#!/usr/bin/env python3

def famous_births(date):
    for scientist in women_scientists.values(), key=lambda x: x["date_of_birth"]):
        print(f'{scientist["name"]} is a great scientist born in {scientist["date_of_birth"]}')

women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecilia Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
