from abc import ABC, abstractmethod


# ==========================================
# 1. ABSTRACT EXPRESSION
# ==========================================
class Expression(ABC):
    """
    The Abstract Expression declares the interpret method that all
    nodes in the syntax tree must implement.
    """
    @abstractmethod
    def interpret(self, context: dict[str, int]) -> int:
        pass


# ==========================================
# 2. TERMINAL EXPRESSIONS (Leaf Nodes)
# ==========================================
class Number(Expression):
    """Represents a literal constant integer."""
    def __init__(self, value: int):
        self._value = value

    def interpret(self, context: dict[str, int]) -> int:
        return self._value


class Variable(Expression):
    """Represents a named variable resolved via the context dictionary."""
    def __init__(self, name: str):
        self._name = name

    def interpret(self, context: dict[str, int]) -> int:
        if self._name not in context:
            raise KeyError(f"Undefined variable: '{self._name}'")
        return context[self._name]


# ==========================================
# 3. NON-TERMINAL EXPRESSIONS (Composite Nodes)
# ==========================================
class Add(Expression):
    """Represents addition of two sub-expressions."""
    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: dict[str, int]) -> int:
        return self._left.interpret(context) + self._right.interpret(context)


class Subtract(Expression):
    """Represents subtraction of two sub-expressions."""
    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: dict[str, int]) -> int:
        return self._left.interpret(context) - self._right.interpret(context)


class Multiply(Expression):
    """Represents multiplication of two sub-expressions."""
    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: dict[str, int]) -> int:
        return self._left.interpret(context) * self._right.interpret(context)


# ==========================================
# 4. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    # Context holds our variable values
    context = {"x": 10, "y": 20, "z": 5}

    # Construct the AST (Abstract Syntax Tree) for: (x + y) - (z * 2)
    # Target calculation: (10 + 20) - (5 * 2) = 30 - 10 = 20
    expression_tree = Subtract(
        Add(Variable("x"), Variable("y")),
        Multiply(Variable("z"), Number(2))
    )

    result = expression_tree.interpret(context)
    print(f"Context: {context}")
    print(f"Expression: (x + y) - (z * 2)")
    print(f"Evaluated Result: {result}")

    # Changing context variables dynamically without rebuilding the tree
    context_2 = {"x": 100, "y": 50, "z": 10}
    # Calculation: (100 + 50) - (10 * 2) = 150 - 20 = 130
    print(f"\nNew Context: {context_2}")
    print(f"Re-evaluated Result: {expression_tree.interpret(context_2)}")