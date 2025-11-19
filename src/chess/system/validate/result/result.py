# src/chess/system/validate/old_transaction.py

"""
Module: chess.owner.system.validate.notification
Author: Banji Lawal
Created: 2025-09-28
Updated: 2025-10-10

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` integrity requirement.
  2. A satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module covers clients and servers in the `ChessBot` coord_stack_validator graph.

# SECTION 3 - Limitations:
  1. The module is limited to the reporting coord_stack_validator results to clients.
  2. The module does not provide any methods for dealing with the candidates which fail to meet correctness
      requirements.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. A consistent interface aiding discoverability, understanding and simplicity.

# SECTION 5- Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.
  2. Ensuring coord_stack_validator results are communicated are sent to clients is an integrity feature.

# 6 Feature Delivery Mechanism:
  1. The features are implemented by a communication mechanism between a coord_stack_validator service and its client.

# SECTION 7 - Dependencies:
* From `chess.system.coord_stack_validator`:
    `Validation`

* From `chess.system.err.rollback_exception`:
    `Result`

* From Python `abc` Library:
    `ABC`, `abstractmethod`

* From Python `typing` Library:
    `Generic`, `TypeVar`, `Optional`

# SECTION 8- Contains:
1. `ValidationResult`
"""

from typing import Optional, TypeVar, Generic
from chess.system import NotImplementedException, Result

T = TypeVar("T")


class ValidationResult(Result[Generic[T]]):
    """
    # ROLE: Message passing, Data Transfer Object
  
    # RESPONSIBILITIES:
    1. Carry the outcome a coord_stack_validator operation to originating client.
    2. Enforcing mutual exclusion. A `ValidationResult` can either carry `_payload` or _exception`. Not both.
  
    # PROVIDES:
    1. A correctness verification or denial for the `Validation` service provider.
  
    # ATTRIBUTES:
      * See `Result` superclass for attributes.
    """
    
    def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
        super().__init__(payload=payload, exception=exception)
    
    @classmethod
    def empty(cls) -> Result:
        method = "ValidationResult.empty"
        return Result(
            exception=NotImplementedException(
                f"{method}: {NotImplementedException.DEFAULT_MESSAGE}. ValidationResult cannot"
                f" be empty. It must have either a payload or an rollback_exception."
            )
        )
