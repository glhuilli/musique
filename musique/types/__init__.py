from typing import NamedTuple


class Song(NamedTuple):
    """
    Immutable object that stores a Song title and artist
    """
    artist: str
    title: str
