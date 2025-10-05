from enum import Flag, auto
from typing import Optional, TypeVar, Generic


T = TypeVar('T')


class OperationStatus(Flag):
  LOADING = auto()
  SUCCESS = auto()
  FAILURE = auto()
  EMPTY_SEARCH_RESULT = auto()
  FAILURE_REQUIRES_ROLLBACK = auto()


class Result(Generic[T]):
  def __init__(
    self,
    status: OperationStatus,
    payload: Optional[T] = None,
    message: Optional[str] = None,
    exception: Optional[Exception] = None,
  ):
    self._status = status
    self._payload = payload
    self._message = message
    self._exception = exception


  @property
  def status(self) -> OperationStatus:
    return self._status


  @property
  def payload(self) -> Optional[T]:
    return self._payload


  @property
  def message(self) -> Optional[str]:
    return self._message


  @property
  def exception(self) -> Optional[Exception]:
    return self._exception






