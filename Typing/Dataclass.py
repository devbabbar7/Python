from dataclasses import dataclass, astuple, asdict, field

# Order = True means now it can act as a tuble when using comparison operators, you can add the instances in a list and sort them also, also only frozen dataclasses are hashable.
# Frozen = True means one the class is initialized, the fields cannot be changed. Also now you can use it as a key in a dictionary.
@dataclass(frozen=False, order = True)
class Comment:
    id: int
    text: str = '' # Default value will be empty string
    replies: list[int] = field(default_factory=list, compare = False, hash = True, repr = False)
    # repr = False means when you print an instance, replies will not show.
    # hash = False makes it so the field won't affect the class' fingerprint
    # compare = False when comparing two instances, replies will be irrelevant
    # default_factory = list, we have to use this to set a default value for list, dict or sets
    # if we don't use default_factory for multiple value datatypes and use list[int] = [], then all instances will share same object.

@dataclass(frozen=True) # Frozen=True makes the class hashable by default
class Book:
    isbn: str
    price: float = field(hash=False) # Price doesn't affect the 'fingerprint'

def main():
    comment1 = Comment(1, "I just subscribed.")
    comment1.id = 2 # this is not allowed if frozen=True
    print(comment1) # Comment(id=2, text='I just subscribed.')
    print(astuple(comment1)) # (2, 'I just subscribed.', [])
    print(asdict(comment1)) # {'id': 2, 'text': 'I just subscribed.', 'replies': []}
    comment2 = Comment(3, 'Hello.')
    print(comment1 < comment2) # True, compared instances as a tuple
    comment3 = Comment(2, "I just subscribed.", [1])
    print(comment1 == comment3) # True, because compare is off for replies
    book1 = Book("978-3-16", 29.99)
    book2 = Book("978-3-16", 39.99)
    # Even though the prices are different, the hashes will be IDENTICAL
    # because 'price' is excluded from the hash calculation.
    print(hash(book1)) # -1055225817505390245
    print(hash(book1) == hash(book2)) # Returns: True

if __name__ == "__main__":
    main()