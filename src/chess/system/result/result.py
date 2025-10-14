# src/chess/system/result/result.py

"""
Module: `chess.system.old_search.result`
Author: Banji Lawal
Created: 2025-09-28
Updated: 2025-10-10
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` reliability requirement.
  2. A satisfaction of the performance requirement.
  3. A satisfaction of the availability requirement.

# SECTION 2 - Scope:
The module covers `Result` object in `ChessBot``.

# SECTION 3 - Limitations:
  1. The module is limited to presenting the answer from a `Search` service provider to the client delivering a query.
  2. The module does not guarantee the accuracy or precision of data in the result.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. A consistent interface aiding discoverability, understanding and simplicity.

# SECTION 5 - Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.


# 6 Feature Delivery Mechanism:
  1. A data structure accessors and data generators can use to send either a data or an exception to the caller.
      this prevents the application crashing when an error occurs but preservers the exception for safe handling.

# SECTION 7 - Dependencies:

* From Python `typing` Library:
    `Generic`, `TypeVar`, `Optional`

# SECTION 8 - Contains:
1. `Result`
"""


from typing import Optional, TypeVar, Generic

T = TypeVar('T')


class Result(Generic[T]):
  """
  # ROLE: Message passing, Data Transfer Object

  # RESPONSIBILITIES:
  1. Carry the outcome of a data access or data generation operation to the caller.
  2. Transporting errors from the data source to the requester for handling that preserves reliability and availability.

  # PROVIDES:
  1.

  # Attributes:
    `_payload` (`Optional`[`T`]): Data from the accessor or data generator if their operations were successful.
    `_exception` (`Optional`[`Exception`]): The error raised if the operation called failed.
  """
  _payload: Optional[T]
  _exception: Optional[Exception]


  def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
    self._payload = payload
    self._exception = exception


  @property
  def payload(self) -> Optional[T]:
    return self._payload


  @property
  def exception(self) -> Optional[Exception]:
    return self._exception

  def is_success(self) -> bool:
    """
    # ACTION:
    Confirm the data access or data  generation was successful.

    # PARAMETERS:
      No parameters

    # RETURNS:
      `bool`

    RAISES:
      No exception raised.
    """
    return self._exception is None and self._payload is not None



