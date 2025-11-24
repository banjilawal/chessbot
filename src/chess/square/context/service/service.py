# src/chess/square/context/service/service.py

"""
Module: chess.square.context.service.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import Service, id_emitter
from chess.square import SquareContext, SquareContextBuilder, SquareContextValidator

class SquareContextService(Service[SquareContext]):
    """"""
    DEFAULT_NAME = "SquareContextService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: SquareContextBuilder = SquareContextBuilder(),
            validator: SquareContextValidator = SquareContextValidator()
    ):
        """"""
        method = "SquareContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator)