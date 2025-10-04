from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'saurabh', 'age':'24'}

print(new_person)
