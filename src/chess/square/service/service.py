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
    1.  A single entry point for managing Square object lifecycles with SquareBuilder and SquareValidator.
    2.  Masks implementation details and business logic making features easier to use.
    3.  Protects Square instance's internal state.
    4.  Public facing API.

    # PROVIDES:
        *   SquareBuilder
        *   SquareValidator

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   builder (SquareBuilder)
        *   validator (SquareValidator)
    """
    SERVICE_NAME = "SquareService"

    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: SquareBuilder =  SquareBuilder(),
            validator: SquareValidator = SquareValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)