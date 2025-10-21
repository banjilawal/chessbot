from chess.piece import PieceDTO


class OccupationEventDTO:
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