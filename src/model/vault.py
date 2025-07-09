from dataclasses import dataclass, field
from typing import Optional, List, Union, Dict

from common.dimension import Dimension
from common.direction import Direction
from model.grid_coordinate import GridCoordinate, CoordinateRange
from model.grid_entity import GridEntity


@dataclass
class Vault(GridEntity):

    def __init__(self, vault_id: int, coordinate: Optional[GridCoordinate] = None):
        super().__init__(id=vault_id, dimension=Dimension(length=1, height=1), coordinate=coordinate)


@dataclass
class HorizontalVaults:
    id: int
    vaults: List[Vault] = field(default_factory=list)

    def coordinate_range(self) -> Optional[CoordinateRange]:
        positioned_vaults = [v for v in self.vaults if v.coordinate is not None]
        if not positioned_vaults:
            return None

        sorted_vaults = sorted(positioned_vaults, key=lambda v: v.coordinate.x)
        return CoordinateRange(
            first_coordinate=sorted_vaults[0].coordinate,
            last_coordinate=sorted_vaults[-1].coordinate
        )


@dataclass
class VerticalVaults:
    vaults: List[Vault] = field(default_factory=list)

    def coordinate_range(self) -> Optional[CoordinateRange]:
        positioned_vaults = [v for v in self.vaults if v.coordinate is not None]
        if not positioned_vaults:
            return None

        sorted_vaults = sorted(positioned_vaults, key=lambda v: v.coordinate.y)
        return CoordinateRange(
            first_coordinate=sorted_vaults[0].coordinate,
            last_coordinate=sorted_vaults[-1].coordinate
        )


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


class VerticalVaultsDictionary:
    def __init__(self):
        self._vaults: Dict[int, VerticalVaults] = {}

    def add(self, key: int, vaults: VerticalVaults) -> None:
        self._vaults[key] = vaults

    def get(self, key: int) -> Optional[VerticalVaults]:
        return self._vaults.get(key)

    def remove(self, key: int) -> None:
        if key in self._vaults:
            del self._vaults[key]

    @property
    def items(self) -> Dict[int, VerticalVaults]:
        return self._vaults.copy()


class HorizontalVaultsDictionary:
    def __init__(self):
        self._vaults: Dict[int, HorizontalVaults] = {}

    def add(self, key: int, vaults: HorizontalVaults) -> None:
        self._vaults[key] = vaults

    def get(self, key: int) -> Optional[HorizontalVaults]:
        return self._vaults.get(key)

    def remove(self, key: int) -> None:
        if key in self._vaults:
            del self._vaults[key]

    @property
    def items(self) -> Dict[int, HorizontalVaults]:
        return self._vaults.copy()


