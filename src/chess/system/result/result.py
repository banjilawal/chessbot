# src/chess/system/result.py

"""
Module: `chess.system.result.result`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

 Provides:
 Interface for operation results that can have either a data payload or an exception only.

Contains:
 * `Result`
"""


from typing import Optional, TypeVar, Generic

from chess.system import EmptyResultConstructorException, ErrorContradictsPayloadException

T = TypeVar('T')

__all__ = ['Result']


class Result(Generic[T]):
  """
  Abstract super class for data-holding objects which represent outcome of
  operations that produce one of two results only.
    * Success: A payload is returned
    * Failure: An exception is raised

  Attributes:
    `_payload` (`Optional`[`T`]): The payload of the result, if the operation called.
    `_exception` (`Optional`[`Exception`]): The error raised if the operation called failed.
  """

  _payload: Optional[T]
  _exception: Optional[Exception]

  def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
    method = "Result.__init_"

    # Raise an error if neither payload nor error is provided
    if payload is None and exception is None:
      raise EmptyResultConstructorException(
        f"{method}: {EmptyResultConstructorException.DEFAULT_MESSAGE}"
      )

    # Raise an error if both payload and error are provided
    if not (payload is None and exception is None):
      raise ErrorContradictsPayloadException(
        f"{method}: {ErrorContradictsPayloadException.DEFAULT_MESSAGE}"
      )

    self._payload = payload
    self._exception = exception

  @property
  def payload(self) -> Optional[T]:
    return self._payload

  @property
  def exception(self) -> Optional[Exception]:
    return self._exception

  def is_success(self) -> bool:
    return self._exception is None and self._payload is not None



