from typing import List, Optional

from chess.competitor.commander import CyberneticCommander
from chess.competitor.commander import HumanCommander
from chess.competitor.commander import Commander


class OwnerRepo:
    _owners: List[Commander]

    def __init__(self):
        self._owners = []


    def __len__(self):
        return len(self._owners)


    def add_owner(self, owner: Commander):
        if owner not in self._owners:
            self._owners.append(owner)


    def owner_by_id(self, owner_id: int) -> Optional[Commander]:
        for owner in self._owners:
            if owner.id == owner_id:
                return owner
        return None


    def owners_by_name(self, name: str) -> List[Commander]:
        matches: List[Commander] = []

        for owner in self._owners:
            if owner.name.upper() == name.upper() and owner not in matches:
                matches.append(owner)
        return matches


    def human_owners(self) -> List[HumanCommander]:
        matches: List[HumanCommander] = []

        for owner in self._owners:
            if isinstance(owner, HumanCommander) and owner not in matches:
                matches.append(owner)
        return matches


    def cybernetic_owners(self) -> List[CyberneticCommander]:
        matches: List[CyberneticCommander] = []

        for owner in self._owners:
            if isinstance(owner, CyberneticCommander) and owner not in matches:
                matches.append(owner)
        return matches