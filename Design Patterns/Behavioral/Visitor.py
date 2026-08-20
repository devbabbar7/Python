from __future__ import annotations
from abc import ABC, abstractmethod


# ==========================================
# 1. ELEMENT INTERFACE (The Visitable Objects)
# ==========================================
class ItemElement(ABC):
    """
    The Element interface declares an `accept` method that takes
    the base visitor interface as an argument.
    """
    @abstractmethod
    def accept(self, visitor: ItemVisitor) -> float:
        pass


# ==========================================
# 2. CONCRETE ELEMENTS
# ==========================================
class Book(ItemElement):
    def __init__(self, title: str, price: float, weight_kg: float):
        self.title = title
        self.price = price
        self.weight_kg = weight_kg

    def accept(self, visitor: ItemVisitor) -> float:
        # Double Dispatch: tells the visitor "I am a Book, visit me!"
        return visitor.visit_book(self)


class Fruit(ItemElement):
    def __init__(self, name: str, price_per_kg: float, weight_kg: float):
        self.name = name
        self.price_per_kg = price_per_kg
        self.weight_kg = weight_kg

    def get_total_price(self) -> float:
        return self.price_per_kg * self.weight_kg

    def accept(self, visitor: ItemVisitor) -> float:
        # Double Dispatch: tells the visitor "I am a Fruit, visit me!"
        return visitor.visit_fruit(self)


# ==========================================
# 3. VISITOR INTERFACE
# ==========================================
class ItemVisitor(ABC):
    """
    The Visitor interface declares a set of visiting methods corresponding
    to each concrete element class.
    """
    @abstractmethod
    def visit_book(self, book: Book) -> float:
        pass

    @abstractmethod
    def visit_fruit(self, fruit: Fruit) -> float:
        pass


# ==========================================
# 4. CONCRETE VISITORS (Adding Operations)
# ==========================================
class TaxVisitor(ItemVisitor):
    """
    Operation 1: Calculates sales tax.
    Rule: Books are tax-free (0%), Fruits have 5% food tax.
    """
    def visit_book(self, book: Book) -> float:
        tax = 0.0  # Books are tax-exempt
        print(f"[Tax] '{book.title}': Tax-exempt ($0.00)")
        return tax

    def visit_fruit(self, fruit: Fruit) -> float:
        tax = fruit.get_total_price() * 0.05
        print(f"[Tax] Fruit '{fruit.name}': 5% tax = ${tax:.2f}")
        return tax


class ShippingCostVisitor(ItemVisitor):
    """
    Operation 2: Calculates shipping cost based on weight.
    Rule: Books cost $2.00 per kg; Fresh fruit requires refrigeration ($4.00 per kg).
    """
    def visit_book(self, book: Book) -> float:
        cost = book.weight_kg * 2.00
        print(f"[Shipping] '{book.title}' ({book.weight_kg}kg): ${cost:.2f}")
        return cost

    def visit_fruit(self, fruit: Fruit) -> float:
        cost = fruit.weight_kg * 4.00  # Cold storage rate
        print(f"[Shipping] '{fruit.name}' ({fruit.weight_kg}kg refrigerated): ${cost:.2f}")
        return cost


# ==========================================
# 5. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    # Our shopping cart of mixed elements
    cart: list[ItemElement] = [
        Book("Design Patterns in Python", price=45.00, weight_kg=1.2),
        Fruit("Bananas", price_per_kg=2.50, weight_kg=3.0),
        Book("Clean Code", price=40.00, weight_kg=0.8),
    ]

    # Operation 1: Calculate Total Tax using TaxVisitor
    print("--- 1. Calculating Taxes ---")
    tax_visitor = TaxVisitor()
    total_tax = sum(item.accept(tax_visitor) for item in cart)
    print(f"Total Tax to pay: ${total_tax:.2f}\n")

    # Operation 2: Calculate Total Shipping using ShippingCostVisitor
    print("--- 2. Calculating Shipping Costs ---")
    shipping_visitor = ShippingCostVisitor()
    total_shipping = sum(item.accept(shipping_visitor) for item in cart)
    print(f"Total Shipping Cost: ${total_shipping:.2f}")