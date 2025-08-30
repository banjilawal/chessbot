from itertools import filterfalse
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class Request(Generic[T]):
    _id: int
    _client: Generic[T]
    _resource: Generic[T]


    def __init__(self, request_id: int, client: Generic[T], resource: Optional[Generic[T]]=None):
        self._id = request_id
        self._client = client
        self._resource = resource


    @property
    def id(self) -> int:
        return self._id


    @property
    def client(self) -> Generic[T]:
        return self._client


    @property
    def resource(self) -> Optional[Generic[T]]:
        return self._resource


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Request):
            return False
        return self._id == other.id


