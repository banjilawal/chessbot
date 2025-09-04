from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class Request(Generic[T]):
    _id: int
    _client: T
    _resource: Optional[T]


    def __init__(self, req_id: int, client: T, resource: Optional[T]=None):
        self._id = req_id
        self._client = client
        self._resource = resource


    @property
    def id(self) -> int:
        return self._id


    @property
    def client(self) -> T:
        return self._client


    @property
    def resource(self) -> Optional[T]:
        return self._resource


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Request):
            return False
        return self._id == other.id


