from chess.owner.owner_repo import OwnerRepo


class OwnerService:
    _repo: OwnerRepo

    def __init__(self, repo: OwnerRepo):
        self._repo = repo

    @property
    def repo(self) -> OwnerRepo:
        return self._repo