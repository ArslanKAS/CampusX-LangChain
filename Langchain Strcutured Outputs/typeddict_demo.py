from typing import TypedDict

class CXEX(TypedDict):
    name: str
    age: int


person : CXEX = {'name': "John Doe", 'age': 30}

print(person)