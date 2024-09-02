from datetime import datetime
from ninja import Schema


class LibraryEntryCreateSchema(Schema):
    # Create -> Data
    # LibraryEntryIn
    title: str
    author: str
    isbn: str


class LibraryEntryDetailCreateSchema(Schema):
    # Get -> Data
    # LibraryEntryDetailOut
    title: str
    author: str
    pages: int
    rating: int
    review: str
    isbn: str
    completed: bool
    timestamp: datetime


class LibraryEntryListSchema(Schema):
    # List -> Data
    # LibraryEntryOut
    title: str
    author: str
    pages: int
    rating: int
    review: str
    isbn: str
    completed: bool
    timestamp: datetime
