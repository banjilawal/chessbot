from abc import abstractmethod
from enum import auto

from chess.flow.base import Flow
from chess.system.request import Request


class Choice:
    OK = auto()
    CANCEL = auto()


class Action:
    _choice: Choice


    def request(self) -> Request:
        pass


    @abstractmethod
    def flow(self) -> Flow:
        pass