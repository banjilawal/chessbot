# src/chess/square/service/service.py

"""
Module: chess.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from typing import cast

from chess.system import EntityService, id_emitter
from chess.square import Square, SquareBuilder, SquareValidator

class SquareService(EntityService[Square]):
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
        """
        # Action
        1.  Use id_emitter to automatically generate a unique id for each SquareService instance.
        2.  Automatic dependency injection by providing working default instances of each attribute.
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
        
    @property
    def item_builder(self) -> SquareBuilder:
        return cast(SquareBuilder, self.item_builder)
    
    
    @property
    def item_validator(self) -> SquareValidator:
        return cast(SquareValidator, self.item_validator)