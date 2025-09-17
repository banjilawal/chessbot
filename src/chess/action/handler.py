from abc import ABC, abstractmethod

from chess.action import Action, ActionOutcome

class ActionHandler(ABC):
    """Base class for action execution handlers"""

    @abstractmethod
    def execute(self, action: Action, context: dict = None) -> ActionOutcome:
        pass