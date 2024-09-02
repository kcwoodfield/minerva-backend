from ninja import Schema

"""
This module contains the schema definition for creating a library entry.

Attributes:
    id (int): The ID of the library entry (read-only).
    name (str): The name of the library entry (required).
    location (str): The location of the library entry (required).
    created_at (datetime): The timestamp of when the library entry was created (read-only).
    updated_at (datetime): The timestamp of when the library entry was last updated (read-only).
"""


class LibraryEntryCreateSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
