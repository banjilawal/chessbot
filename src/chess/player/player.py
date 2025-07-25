class Player(ABC):
    _id: int
    _name: str
    def __init__(self, player_id: int, name: str):
        self._id = player_id
        self._name = name

    @property
    def id(self) -> int:
        return -