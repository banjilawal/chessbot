from typing import Generic, TypeVar

from chess.request.base import Request

T = TypeVar('T')


class AttackRequest(Request):

    @staticmethod
    def enter(request_id:int , client: Generic[T], resource: Generic[T]):

