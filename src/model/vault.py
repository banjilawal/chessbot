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
class , :
    id: int
    growth_direction: Direction
    vaults: List[Vault] = field(default_factory=list)

    def __init__(self, vault_group_id: int, growth_direction: Direction):
        self.id = vault_group_id
        self.growth_direction = growth_direction

@dataclass
class HorizontalVaults:
    id: int
    vaults: List[Vault] = field(default_factory=list)

@dataclass
class VerticalVaults:
    vaults: List[Vault] = field(default_factory=list)


class VaultArrayBuilder:
    @staticmethod
    def build(vault: Vault, direction: Direction, size: int) -> Union[HorizontalVaults, VerticalVaults]:
        vaults = []
        for i in range(size):
            # Create a new vault with incremented ID for each position
            new_vault = Vault(vault_id=vault.id + i)
            vaults.append(new_vault)

        if direction == Direction.HORIZONTAL:
            return HorizontalVaults(id=vault.id, vaults=vaults)
        else:
            return VerticalVaults(vaults=vaults)

