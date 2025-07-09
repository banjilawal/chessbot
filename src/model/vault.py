from dataclasses import dataclass
from typing import Optional

from common.dimension import Dimension
from model.grid_coordinate import GridCoordinate
from model.grid_entity import GridEntity


@dataclass
class Vault(GridEntity):

    def __init__(self, id: int, coordinate: Optional[GridCoordinate] = None):
        super().__init__(id=id, dimension=Dimension(length=1, height=1), coordinate=coordinate)