from typing import List, Optional

from chess.owner.cybernetic import CyberneticOwner
from chess.owner.human import HumanOwner
from chess.owner.base import Owner


class OwnerRepo:
    _owners: List[Owner]

    def __init__(self):
        self._owners = []


    def __len__(self):
        return len(self._owners)


    def add_owner(self, owner: Owner):
        if owner not in self._owners:
            self._owners.append(owner)


    def owner_by_id(self, owner_id: int) -> Optional[Owner]:
        for owner in self._owners:
            if owner.id == owner_id:
                return owner
        return None


    def owners_by_name(self, name: str) -> List[Owner]:
        matches: List[Owner] = []

        for owner in self._owners:
            if owner.name.upper() == name.upper() and owner not in matches:
                matches.append(owner)
        return matches


    def human_owners(self) -> List[HumanOwner]:
        matches: List[HumanOwner] = []

        for owner in self._owners:
            if isinstance(owner, HumanOwner) and owner not in matches:
                matches.append(owner)
        return matches


    def cybernetic_owners(self) -> List[CyberneticOwner]:
        matches: List[CyberneticOwner] = []

        for owner in self._owners:
            if isinstance(owner, CyberneticOwner) and owner not in matches:
                matches.append(owner)
        return matches