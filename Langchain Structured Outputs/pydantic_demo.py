from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class CXEX(BaseModel):
    name: str = "Default Name" # DEFAULT
    age: Optional[int] = None # OPTIONAL & DEFAULT | if absent, it will be None
    profession: str
    email: EmailStr
    cgpa: float = Field(gt=0.0, le=4.0) # CONSTRAINT | gt: greater than, le: less than or equal to
    gpa: float = Field(gt=0.0, le=4.0, default=2, description="GPA of a university student for a single semester") # CONSTRAINT & DEFAULT & DESCRIPTION| if gpa is absent, it will be 2.0


ammar = {'name': "Ammar Zafar", 'age': 22, 'profession': "Software Engineer", 'email': "ammarz@google.com", 'cgpa': 3.5}

person = CXEX(**ammar)

dictionary_person = person.model_dump() # dictionary
print(dictionary_person)

json_person = person.model_dump_json() # JSON string
print(json_person)