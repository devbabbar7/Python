# ==========================================
# 1. FLYWEIGHT (Shared Intrinsic State)
# ==========================================
class TreeType:
    """
    The Flyweight stores intrinsic state (heavy, shared data) that belongs
    to multiple objects.
    """
    def __init__(self, name: str, color: str, texture: str):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x: int, y: int) -> None:
        # Extrinsic state (x, y) is passed in at execution time
        print(f"Drawing '{self.name}' [{self.color}] at ({x}, {y})")


# ==========================================
# 2. FLYWEIGHT FACTORY (Caching Mechanism)
# ==========================================
class TreeFactory:
    """
    The Factory manages flyweight instances. It creates a new flyweight only
    if one with matching intrinsic state doesn't already exist.
    """
    _tree_types: dict[tuple, TreeType] = {}

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        key = (name, color, texture)
        if key not in cls._tree_types:
            print(f"[Factory] Creating NEW TreeType: '{name}' ({color})")
            cls._tree_types[key] = TreeType(name, color, texture)
        else:
            print(f"[Factory] Reusing EXISTING TreeType: '{name}' ({color})")
        return cls._tree_types[key]


# ==========================================
# 3. CONTEXT (Unique Extrinsic State)
# ==========================================
class Tree:
    """
    The Context stores extrinsic state (unique per instance) and holds
    a reference to the shared Flyweight object.
    """
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type  # Shared reference

    def draw(self) -> None:
        self.tree_type.draw(self.x, self.y)


# ==========================================
# 4. FOREST (Container / Client)
# ==========================================
class Forest:
    def __init__(self):
        self._trees: list[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str) -> None:
        # Get shared Flyweight from Factory
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        # Create lightweight Context object
        tree = Tree(x, y, tree_type)
        self._trees.append(tree)

    def draw_forest(self) -> None:
        for tree in self._trees:
            tree.draw()


# ==========================================
# 5. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    forest = Forest()

    # Planting Oak trees (Factory creates 1 Flyweight)
    forest.plant_tree(10, 20, "Oak", "Green", "OakTexture.png")
    forest.plant_tree(15, 25, "Oak", "Green", "OakTexture.png")
    forest.plant_tree(30, 40, "Oak", "Green", "OakTexture.png")

    print()

    # Planting Pine trees (Factory creates another 1 Flyweight)
    forest.plant_tree(50, 60, "Pine", "Dark Green", "PineTexture.png")
    forest.plant_tree(55, 65, "Pine", "Dark Green", "PineTexture.png")

    print("\n--- Drawing All Trees ---")
    forest.draw_forest()

    # Memory Check Proof:
    print("\n--- Memory Verification ---")
    oak1_type_id = id(forest._trees[0].tree_type)
    oak2_type_id = id(forest._trees[1].tree_type)
    print(f"Oak 1 TreeType Memory ID: {oak1_type_id}")
    print(f"Oak 2 TreeType Memory ID: {oak2_type_id}")
    print(f"Are they sharing the EXACT same Flyweight object? {oak1_type_id == oak2_type_id}")