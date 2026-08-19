from abc import ABC, abstractmethod


# ==========================================
# 1. ABSTRACT CLASS (Template Skeleton)
# ==========================================
class BeverageMaker(ABC):
    """
    The Abstract Class defines a template method that contains the skeleton
    of an algorithm composed of calls to abstract and concrete operations.
    """

    def make_beverage(self) -> None:
        """The Template Method: orchestrates the step sequence."""
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()
        print("--- Drink is ready! ---\n")

    # Common steps (Concrete implementations)
    def boil_water(self) -> None:
        print("1. Boiling water...")

    def pour_in_cup(self) -> None:
        print("3. Pouring beverage into cup...")

    # Primitive steps (Abstract methods to be overridden)
    @abstractmethod
    def brew(self) -> None:
        pass

    @abstractmethod
    def add_condiments(self) -> None:
        pass

    # Hook (Provides default behavior, can be optionally overridden)
    def customer_wants_condiments(self) -> bool:
        return True


# ==========================================
# 2. CONCRETE CLASSES (Specific Step Details)
# ==========================================
class TeaMaker(BeverageMaker):
    def brew(self) -> None:
        print("2. Steeping the tea leaves...")

    def add_condiments(self) -> None:
        print("4. Adding fresh lemon slices...")


class CoffeeMaker(BeverageMaker):
    def __init__(self, with_milk_and_sugar: bool = True):
        self._with_condiments = with_milk_and_sugar

    def brew(self) -> None:
        print("2. Filtering coffee through drip filter...")

    def add_condiments(self) -> None:
        print("4. Adding steamed milk and brown sugar...")

    def customer_wants_condiments(self) -> bool:
        return self._with_condiments


# ==========================================
# 3. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    print("--- Making Lemon Tea ---")
    tea = TeaMaker()
    tea.make_beverage()

    print("--- Making Black Coffee (No Condiments) ---")
    black_coffee = CoffeeMaker(with_milk_and_sugar=False)
    black_coffee.make_beverage()