# src/chess/square/service/service.py

"""
Module: chess.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from chess.system import Service, id_emitter
from chess.square import Square, SquareBuilder, SquareValidator

class SquareService(Service[Square]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Protects Square instance's internal state.
    3.  Masks implementation details and business logic making features easier to use.
    4.  Single entry point for managing Square lifecycles with SquareBuilder and SquareValidator.

    # PROVIDES:
        *   SquareBuilder
        *   SquareValidator

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   builder (SquareBuilder)
        *   validator (SquareValidator)
    """
    DEFAULT_NAME = "SquareService"

    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: SquareBuilder =  SquareBuilder(),
            validator: SquareValidator = SquareValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)