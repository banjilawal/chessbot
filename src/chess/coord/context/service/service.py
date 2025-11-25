# src/chess/coord/context/service/service.py

"""
Module: chess.coord.context.service.service
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import Service, id_emitter
from chess.coord import CoordContext, CoordContextBuilder, CoordContextValidator

class CoordContextService(Service[CoordContext]):
    """
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single entry point for CoordContextBuilder and CoordContextValidator objects.
    2.  Passing its self._validator to the self._builder simplifies the SearchContext lifecycle.
    3.  Protects SearchContext from direct, unprotected access.
    4.  Public facing API.

    # PROVIDES:
        *   Direct access tp CoordContextValidator
        *   Interface to CoordContextBuilder

    # ATTRIBUTES:
        *   _builder (CoordContextBuilder):
        *   _validator (CoordContextValidator):
    """
    DEFAULT_NAME = "CoordContextService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: CoordContextBuilder = CoordContextBuilder(),
            validator: CoordContextValidator = CoordContextValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)