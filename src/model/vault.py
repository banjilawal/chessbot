from dataclasses import dataclass, field
from typing import Optional, List

from common.dimension import Dimension
from common.direction import Direction
from model.grid_coordinate import GridCoordinate
from model.grid_entity import GridEntity


@dataclass
class Vault(GridEntity):

    def __init__(self, vault_id: int, coordinate: Optional[GridCoordinate] = None):
        super().__init__(id=vault_id, dimension=Dimension(length=1, height=1), coordinate=coordinate)

@dataclass
class VaultGroup:
    id: int
    growth_direction: Direction
    vaults: List[Vault] = field(default_factory=list)

    def __init__(self, vault_group_id: int, growth_direction: Direction):
        self.id = vault_group_id
        self.growth_direction = growth_direction
