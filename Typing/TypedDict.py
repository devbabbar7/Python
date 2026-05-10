from typing import TypedDict, Required, NotRequired, ReadOnly

class EmergencyContact(TypedDict):
    name: str
    phone: str
    relationship: str

# Total = False assumes that every field unless specified is not required.
class Person(TypedDict, total = False):
    id: ReadOnly[int]
    name: Required[str]
    email: NotRequired[str]
    phone: Required[str]
    emergency_contact: EmergencyContact

user: Person = {'id': 0, 'name': 'Dev', 'phone': '1234567890'}

print(user['phone'])
user['id'] = 1 # It will allow even though read-only because TypedDict doesn't have validations, only reminders for developer.