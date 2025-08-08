from typing import List, Optional

from chess.owner.model.cybernetic_owner import CyberneticOwner
from chess.owner.model.human_owner import HumanOwner
from chess.owner.model.owner import Owner


class OwnerRepo:
    _owners: List[Owner]

    def __init__(self):
        self._owners = []

    def add_owner(self, owner: Owner):
        if owner not in self._owners:
            self._owners.append(owner)


    def find_owner_by_id(self, owner_id: int) -> Optional[Owner]:
        for owner in self._owners:
            if owner.id == owner_id:
                return owner
        return None


    def find_owner_by_name(self, name: str) -> Optional[Owner]:
        for owner in self._owners:
            if owner.name.upper() == name.upper():
                return owner
        return None


    def human_owners(self) -> List[HumanOwner]:
        matches: List[HumanOwner] = []

        for owner in self._owners:
            if isinstance(owner, HumanOwner) and owner not in matches:
                matches.append(owner)
        return matches


    def cybernetic_owners(self) -> List[Owner]:
        matches: List[Owner] = []

        for owner in self._owners:
            if isinstance(owner, CyberneticOwner) and owner not in matches:
                matches.append(owner)
        return matches