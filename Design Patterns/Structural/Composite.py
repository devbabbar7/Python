from abc import ABC, abstractmethod


# 1. Component Interface
class FileSystemItem(ABC):
    """
    The Component interface declares common operations for both simple (Leaf)
    and complex (Composite) objects of the tree.
    """
    @abstractmethod
    def get_size(self) -> int:
        pass


# 2. Leaf (Individual Object)
class File(FileSystemItem):
    """
    The Leaf represents end objects of a structure. A leaf can't have any children.
    It does the actual work directly.
    """
    def __init__(self, name: str, size_in_mb: int):
        self.name = name
        self._size = size_in_mb

    def get_size(self) -> int:
        return self._size


# 3. Composite (Container Object)
class Folder(FileSystemItem):
    """
    The Composite represents complex components that may have children.
    It delegates work to its sub-children and aggregates the result.
    """
    def __init__(self, name: str):
        self.name = name
        self._children: list[FileSystemItem] = []

    def add(self, item: FileSystemItem) -> None:
        self._children.append(item)

    def remove(self, item: FileSystemItem) -> None:
        self._children.remove(item)

    def get_size(self) -> int:
        # Delegates work to children recursively without needing to know
        # whether child is a File or another Folder.
        total_size = 0
        for child in self._children:
            total_size += child.get_size()
        return total_size


# --- Client Execution ---
if __name__ == "__main__":
    # 1. Create individual leaf files
    doc = File("resume.pdf", 2)
    img1 = File("vacation1.jpg", 4)
    img2 = File("vacation2.jpg", 6)

    # 2. Build nested folder structure
    holiday_photos = Folder("Holiday Photos")
    holiday_photos.add(img1)
    holiday_photos.add(img2)

    documents = Folder("My Documents")
    documents.add(doc)
    documents.add(holiday_photos)  # Adding a folder inside a folder!

    # 3. Treat leaves and composites uniformly
    print(f"File size ({doc.name}): {doc.get_size()} MB")
    print(f"Sub-folder size ({holiday_photos.name}): {holiday_photos.get_size()} MB")
    print(f"Total Documents size ({documents.name}): {documents.get_size()} MB")