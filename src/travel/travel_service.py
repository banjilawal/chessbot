from dataclasses import dataclass
from typing import List

from model.board.board import Board
from travel.travel_request import TravelRequest


@dataclass
class TravelService:
    board: Board
    queries: List['TravelRequest'] = tuple()
