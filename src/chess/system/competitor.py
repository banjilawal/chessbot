from abc import abstractmethod
from enum import auto

from chess.flow.base import Flow
from chess.system.command import Command


class Choice:
    OK = auto()
    CANCEL = auto()


class Action:
    _choice: Choice


    def request(self) -> Command:
        pass


    @abstractmethod
    def flow(self) -> Flow:
        pass