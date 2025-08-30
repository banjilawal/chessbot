from abc import ABC
from typing import Optional

from chess.common.permission import Permission
from chess.request.attack import AttackRequest
from chess.request.base import Request
from chess.request.occupy import OccupationRequest
from chess.request.promote import PromotionRequest


class PermissionResult(ABC):
    _request: Request
    _permission: Optional[Permission]
    _exception: Optional[Exception]

    def __init__(
        self,
        request: Request,
        permission: Optional[Permission] = None,
        exception: Optional[Exception] = None
    ):
        self._request = request
        self._permission = permission
        self._exception = exception


    @property
    def id(self) -> id:
        return self._id


    @property
    def request(self) -> Optional[Request]:
        return self._request


    @property
    def permission(self) -> Optional[Permission]:
        return self._permisison


    @property
    def exception(self) -> Optional[Exception]:
        return self._exception


    def is_success(self) -> bool:
        return self._exception is None




