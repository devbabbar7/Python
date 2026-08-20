from __future__ import annotations
from dataclasses import dataclass
import time


# ==========================================
# 1. MEMENTO (Immutable Snapshot)
# ==========================================
@dataclass(frozen=True)
class EditorMemento:
    """
    The Memento is a passive, immutable data carrier that stores the
    internal state of the Originator.
    Using `frozen=True` ensures the snapshot cannot be altered after creation.
    """
    text: str
    cursor_position: int
    timestamp: str


# ==========================================
# 2. ORIGINATOR (The Object Being Saved)
# ==========================================
class TextEditor:
    """
    The Originator holds the state that needs to be preserved.
    It knows how to generate a Memento of itself and how to restore
    its state from a Memento.
    """
    def __init__(self):
        self._text: str = ""
        self._cursor_position: int = 0

    def write(self, text: str) -> None:
        self._text += text
        self._cursor_position = len(self._text)
        print(f"[Editor] Content: '{self._text}' (Cursor at {self._cursor_position})")

    # Creates a snapshot of current internal state
    def save(self) -> EditorMemento:
        current_time = time.strftime("%H:%M:%S")
        print(f"[Editor] --> Saving snapshot at {current_time}...")
        return EditorMemento(self._text, self._cursor_position, current_time)

    # Restores state from a snapshot
    def restore(self, memento: EditorMemento) -> None:
        self._text = memento.text
        self._cursor_position = memento.cursor_position
        print(f"[Editor] <-- Restored snapshot from {memento.timestamp}: '{self._text}' (Cursor at {self._cursor_position})")


# ==========================================
# 3. CARETAKER (History Manager)
# ==========================================
class HistoryManager:
    """
    The Caretaker keeps track of multiple Mementos (Undo stack).
    It never inspects or modifies the contents of a Memento.
    """
    def __init__(self, editor: TextEditor):
        self._editor = editor
        self._history: list[EditorMemento] = []

    def backup(self) -> None:
        self._history.append(self._editor.save())

    def undo(self) -> None:
        if not self._history:
            print("[History] Nothing to undo.")
            return

        last_memento = self._history.pop()
        self._editor.restore(last_memento)


# ==========================================
# 4. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    editor = TextEditor()
    history = HistoryManager(editor)

    print("--- 1. Writing Text & Creating Backups ---")
    editor.write("Hello")
    history.backup()  # State 1 saved: "Hello"

    time.sleep(1)
    editor.write(" World")
    history.backup()  # State 2 saved: "Hello World"

    time.sleep(1)
    editor.write(" - this is a mistake!")  # Unsaved change

    print("\n--- 2. Performing Undo Operations ---")
    history.undo()  # Rollback to: "Hello World"
    history.undo()  # Rollback to: "Hello"
    history.undo()  # Stack is now empty