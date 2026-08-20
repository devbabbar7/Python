from __future__ import annotations
from abc import ABC, abstractmethod


# ==========================================
# 1. THE DATA ITEM
# ==========================================
class Song:
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    def __str__(self) -> str:
        return f"'{self.title}' by {self.artist}"


# ==========================================
# 2. ITERATOR INTERFACE
# ==========================================
class SongIterator(ABC):
    """
    The Iterator interface declares the operations required for traversing
    a collection: fetching the next element and checking if elements remain.
    """
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Song:
        pass

    # Pythonic dunder methods so it works with native `for ... in` loops
    def __iter__(self) -> SongIterator:
        return self

    def __next__(self) -> Song:
        if not self.has_next():
            raise StopIteration
        return self.next()


# ==========================================
# 3. CONCRETE ITERATORS
# ==========================================
class ForwardPlaylistIterator(SongIterator):
    """Iterates through the playlist from start to finish."""
    def __init__(self, playlist: SongPlaylist):
        self._playlist = playlist
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._playlist.get_songs())

    def next(self) -> Song:
        if not self.has_next():
            raise IndexError("No more songs in forward playlist!")
        song = self._playlist.get_songs()[self._index]
        self._index += 1
        return song


class ReversePlaylistIterator(SongIterator):
    """Iterates through the playlist from end to beginning."""
    def __init__(self, playlist: SongPlaylist):
        self._playlist = playlist
        self._index = len(playlist.get_songs()) - 1

    def has_next(self) -> bool:
        return self._index >= 0

    def next(self) -> Song:
        if not self.has_next():
            raise IndexError("No more songs in reverse playlist!")
        song = self._playlist.get_songs()[self._index]
        self._index -= 1
        return song


# ==========================================
# 4. ITERABLE COLLECTION (Aggregate)
# ==========================================
class SongPlaylist:
    """
    The Concrete Collection holds internal storage (private list)
    and provides factory methods to create iterators.
    """
    def __init__(self):
        self._songs: list[Song] = []

    def add_song(self, song: Song) -> None:
        self._songs.append(song)

    def get_songs(self) -> list[Song]:
        return self._songs

    # Factory methods returning different traversal strategies
    def create_forward_iterator(self) -> SongIterator:
        return ForwardPlaylistIterator(self)

    def create_reverse_iterator(self) -> SongIterator:
        return ReversePlaylistIterator(self)

    # Default iterator for Python `for song in playlist:`
    def __iter__(self) -> SongIterator:
        return self.create_forward_iterator()


# ==========================================
# 5. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    playlist = SongPlaylist()
    playlist.add_song(Song("Bohemian Rhapsody", "Queen"))
    playlist.add_song(Song("Hotel California", "Eagles"))
    playlist.add_song(Song("Imagine", "John Lennon"))

    # --- 1. Standard Forward Traversal (Classic while loop) ---
    print("--- Forward Playlist (Classic has_next / next) ---")
    forward_iterator = playlist.create_forward_iterator()
    while forward_iterator.has_next():
        song = forward_iterator.next()
        print(f"Playing: {song}")

    # --- 2. Reverse Traversal ---
    print("\n--- Reverse Playlist ---")
    reverse_iterator = playlist.create_reverse_iterator()
    for song in reverse_iterator:
        print(f"Playing: {song}")

    # --- 3. Native Python Loop ---
    print("\n--- Default Python `for` Loop ---")
    for song in playlist:
        print(f"Playing: {song}")