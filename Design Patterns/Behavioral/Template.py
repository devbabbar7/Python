from abc import ABC, abstractmethod


# ==========================================
# 1. ABSTRACT CLASS (Template Skeleton)
# ==========================================
class BeverageMaker(ABC):
    """
    The Abstract Class defines a template method containing the skeleton
    of the beverage preparation algorithm.
    """
    def __init__(self, with_condiments: bool = True) -> None:
        self._with_condiments = with_condiments

    def make_beverage(self) -> None:
        """The Template Method: orchestrates the step sequence."""
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()
        print("--- Drink is ready! ---\n")

    # Common steps (Shared concrete implementations)
    def boil_water(self) -> None:
        print("1. Boiling water...")

    def pour_in_cup(self) -> None:
        print("3. Pouring beverage into cup...")

    # Abstract steps (Must be implemented by subclasses)
    @abstractmethod
    def brew(self) -> None:
        pass

    @abstractmethod
    def add_condiments(self) -> None:
        pass

    # Hook: Evaluates the instance configuration rather than hardcoding True
    def customer_wants_condiments(self) -> bool:
        return self._with_condiments


# ==========================================
# 2. CONCRETE CLASSES (Specific Step Details)
# ==========================================
class TeaMaker(BeverageMaker):
    def brew(self) -> None:
        print("2. Steeping the tea leaves...")

    def add_condiments(self) -> None:
        print("4. Adding fresh lemon slices...")


class CoffeeMaker(BeverageMaker):
    def brew(self) -> None:
        print("2. Filtering coffee through drip filter...")

    def add_condiments(self) -> None:
        print("4. Adding steamed milk and brown sugar...")


# ==========================================
# 3. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    print("--- Making Lemon Tea (With Condiments) ---")
    tea = TeaMaker(with_condiments=True)
    tea.make_beverage()

    print("--- Making Black Coffee (Without Condiments) ---")
    black_coffee = CoffeeMaker(with_condiments=False)
    black_coffee.make_beverage()