#!/usr/bin/env python3

def greetings(name="nombre stranger"):
    try:
        print(f"Hello, {name}.")
    except Exception:
            print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
