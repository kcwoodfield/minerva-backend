from typing import List

from ninja import Router

from .models import LibraryEntry
from .schemas import LibraryEntryListSchema

router = Router()


@router.get("", response=List[LibraryEntryListSchema])
def list_library_entries(request):
    """
    Retrieve all library entries.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        QuerySet: A queryset containing all library entries.
    """
    qs = LibraryEntry.objects.all()
    return qs
