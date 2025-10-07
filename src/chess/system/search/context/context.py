from abc import ABC

from chess.system import Context

__all__ = [
    'SearchContext',
    'FilterContext'
]

class SearchContext(ABC, Context):
    pass

class FilterContext(ABC, SearchContext):
    pass