from abc import ABC, abstractmethod


# 1. Base Component Interface
class Coffee(ABC):
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> int:
        pass


# 2. Concrete Component (The core item being wrapped)
class PlainCoffee(Coffee):
    def description(self) -> str:
        return "Plain Coffee"

    def cost(self) -> int:
        return 5  # Base price: $5


# 3. Base Decorator
# It implements Coffee AND holds an instance of Coffee inside.
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._decorated_coffee = coffee

    def description(self) -> str:
        return self._decorated_coffee.description()

    def cost(self) -> int:
        return self._decorated_coffee.cost()


# 4. Concrete Decorators (Wrappers that add behavior/state)
class MilkDecorator(CoffeeDecorator):
    def description(self) -> str:
        return f"{self._decorated_coffee.description()}, Milk"

    def cost(self) -> int:
        return self._decorated_coffee.cost() + 2  # Adds $2 for Milk


class SugarDecorator(CoffeeDecorator):
    def description(self) -> str:
        return f"{self._decorated_coffee.description()}, Sugar"

    def cost(self) -> int:
        return self._decorated_coffee.cost() + 1  # Adds $1 for Sugar


# --- Execution Examples ---
if __name__ == "__main__":
    # Example 1: Plain Coffee ($5)
    simple_coffee = PlainCoffee()
    print(f"{simple_coffee.description()} -> ${simple_coffee.cost()}")
    # Output: Plain Coffee -> $5

    # Example 2: Plain Coffee ($5) + Milk ($2) + Sugar ($1)
    custom_coffee = SugarDecorator(MilkDecorator(PlainCoffee()))
    print(f"{custom_coffee.description()} -> ${custom_coffee.cost()}")
    # Output: Plain Coffee, Milk, Sugar -> $8

    # Example 3: Plain Coffee ($5) + Milk ($2) + Sugar ($1) + Sugar ($1)
    double_sugar_coffee = PlainCoffee()
    double_sugar_coffee = MilkDecorator(double_sugar_coffee)
    double_sugar_coffee = SugarDecorator(double_sugar_coffee)
    double_sugar_coffee = SugarDecorator(double_sugar_coffee)

    print(f"{double_sugar_coffee.description()} -> ${double_sugar_coffee.cost()}")
    # Output: Plain Coffee, Milk, Sugar, Sugar -> $9