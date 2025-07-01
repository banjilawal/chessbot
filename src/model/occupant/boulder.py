from dataclasses import dataclass

from model.occupant.occupant import Occupant


# Added model.occupant.EscapePortal which extends Occupant class. Added list of walls to the Board. Renamed
# model.occupant.Wall to model.occupant.Boulder. The Board has 4 walls so the old name was ambigous and not
# communicating the item's intent."

@dataclass
class Boulder(Occupant):
    pass