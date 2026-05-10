# Type annotations
from collections import defaultdict, OrderedDict, Counter, deque

collection1: defaultdict[str, int] = defaultdict(int)
collection2: OrderedDict[str, int] = OrderedDict()
collection3: Counter[str] = Counter()
collection4: deque[int] = deque()

# Some types for type annotations
num1: int = 42
num2: float = 3.14
num3: complex = 1 + 2j
flag: bool = True
string: str = "Hello, World!"
type1: type[int] = type(42)

# Example how to use:
def abc(a: set[str, int]) -> list[int]:
    print(a)
    return [1, 2, 3]

data: dict[str, list[int]] = {"a": [1, 2, 3], "b": [4, 5, 6]}

print(abc({"hello", "world", 1, 2}))
print(type1)