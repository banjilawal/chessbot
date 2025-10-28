# src/chess/piece/travel/occupation/dto.py

"""
Module: `chess.piece.travel.occupation.dto`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import DTO
from chess.square import SquareDTO
from chess.piece import OccupationEvent, PieceDTO

class OccupationEventDTO(DTO[OccupationEvent]):
    _event_id: int
    _actor_dto: PieceDTO
    _actor_square_dto: SquareDTO
    _destination_square_DTO: SquareDTO
    
    def __init__(
        self,
        event_id: int,
        actor_dto: PieceDTO,
        actor_square_dto: SquareDTO,
        destination_square_dto: SquareDTO
    ):
        self._event_id = event_id
        self._actor_dto = actor_dto
        self._actor_square_dto = actor_square_dto
        self._destination_square_DTO = destination_square_dto
    
    def to_dict(self) -> dict:
        return {
            "event_id": self._event_id,
            "traveler": self._actor_dto.to_dict(),
            "actor_square": self._actor_square_dto.to_dict(),
            "enemy_square": self._destination_square_DTO.to_dict()
        }