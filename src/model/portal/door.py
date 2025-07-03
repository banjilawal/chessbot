from abc import ABC
from dataclasses import dataclass

from model.occupant.occupant import Occupant
from model.portal.door_state import DoorState
from model.portal.portal import Portal


# Added model.occupant.EscapePortal which extends Occupant class. Added list of walls to the Board. Renamed
# model.occupant.Wall to model.occupant.Boulder. The Board has 4 walls so the old name was ambigous and not
# communicating the item's intent."

@dataclass
class Door(Occupant, Portal, ABC):
    state: DoorState = DoorState.CLOSED

    def open(self):
        if self.state == DoorState.CLOSED:
            self.state = DoorState.OPEN

    def close(self):
        if self.state == DoorState.OPEN:
            self.state = DoorState.CLOSED

    def is_open(self) -> bool:
        return self.state == DoorState.OPEN
