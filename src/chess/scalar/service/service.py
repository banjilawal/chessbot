# src/chess/scalar/service/service.py

"""
Module: chess.scalar.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""
from typing import cast

from chess.system import BuildResult, EntityService
from chess.scalar import Scalar, ScalarBuilder, ScalarValidator


class ScalarService(EntityService[Scalar]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Scalar microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Scalar state by providing single entry and exit points to Scalar
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   ScalarService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    DEFAULT_NAME = "ScalarService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: ScalarBuilder = ScalarBuilder(),
            validator: ScalarValidator = ScalarValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (ScalarFactory)
            *   validator (ScalarValidator)

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> ScalarBuilder:
        """get ScalarBuilder"""
        return cast(ScalarBuilder, self.entity_builder)
    
    @property
    def validator(self) -> ScalarValidator:
        """get ScalarValidator"""
        return cast(ScalarValidator, self.entity_validator)
