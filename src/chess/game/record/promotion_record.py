from chess.common.piece import Label


class PromotionRecord:
    _id: int
    _location_id: int
    _label: Label
    _rank_name: str
