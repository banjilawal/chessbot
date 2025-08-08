from abc import ABC

from engine.explorer import Explorer


class Engine(ABC):
    _explorer: Explorer
