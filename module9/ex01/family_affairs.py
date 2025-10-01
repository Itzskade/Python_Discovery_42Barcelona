#!/usr/bin/env python3

def find_the_redheads(family):
    notebook = []
    for name, haircolor in family.items():
        if haircolor == "red":
            notebook.append(name)
    return notebook

dupont_family = {
        "florian": "red",
        "marie":  "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
}

print(find_the_redheads(dupont_family))
