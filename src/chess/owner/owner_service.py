from typing import Optional, List

from chess.owner.model.owner import Owner
from chess.owner.owner_repo import OwnerRepo


class OwnerService:
    _repo: OwnerRepo

    def __init__(self, repo: OwnerRepo):
        self._repo = repo


    def size(self) -> int:
        return self._repo.__len__()


    def find_owner_by_id(self, owener_id: int) -> Optional[Owner]:
        return self._repo.owner_by_id(owener_id)


    def filter_owners_by_name(self, name: str) -> List[Owner]:
        return self._repo.owners_by_name(name)


    def find_human_owners(self) -> List[Owner]:
        return self._repo.human_owners()


    def find_cybernetic_owners(self) -> List[Owner]:
        return self._repo.cybernetic_owners()

