from typing import List, Optional

from chess.competitor.model import CyberneticCompetitor
from chess.competitor.model import HumanCompetitor
from chess.competitor.model import Competitor


class OwnerRepo:
    _owners: List[Competitor]

    def __init__(self):
        self._owners = []


    def __len__(self):
        return len(self._owners)


    def add_owner(self, owner: Competitor):
        if owner not in self._owners:
            self._owners.append(owner)


    def owner_by_id(self, owner_id: int) -> Optional[Competitor]:
        for owner in self._owners:
            if owner.id == owner_id:
                return owner
        return None


    def owners_by_name(self, name: str) -> List[Competitor]:
        matches: List[Competitor] = []

        for owner in self._owners:
            if owner.name.upper() == name.upper() and owner not in matches:
                matches.append(owner)
        return matches


    def human_owners(self) -> List[HumanCompetitor]:
        matches: List[HumanCompetitor] = []

        for owner in self._owners:
            if isinstance(owner, HumanCompetitor) and owner not in matches:
                matches.append(owner)
        return matches


    def cybernetic_owners(self) -> List[CyberneticCompetitor]:
        matches: List[CyberneticCompetitor] = []

        for owner in self._owners:
            if isinstance(owner, CyberneticCompetitor) and owner not in matches:
                matches.append(owner)
        return matches