from abc import ABC

from chess.system import Context

class SearchContext(ABC, Context):
    pass

class FilterContext(ABC, SearchContext):
    pass