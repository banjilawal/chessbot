
from enum import Enum


from chess.system import ContextService, ForwardLookup, HashService, ReverseLookup, Validator


class MetaHashService(HashService[Enum]):
    _lookup: ReverseLookup[Enum]
    
    def __init__(
            self,
            id: int,
            name: str,
            validator: Validator[Enum],
            lookup: Lookup[Enum],
            super_key_service: ContextService[Enum],
    ):
        super().__init__(
            id=id,
            name=name,
            validator=validator,
            lookup=lookup,
            super_key_service=super_key_service
        )
        self.__hash_reverse_lookup = reverse_lookup
        
    @property
    def hash_reverse_lookup(self) -> ReverseLookup[Enum]:
        return self.__hash_reverse_lookup