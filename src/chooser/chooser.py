# src/either/either.py

"""
Module: either.either
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from abc import ABC

from toggle import Toggle


class Chooser(Toggle, ABC):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1. Contains one of two types of entity.

    Attributes:
        entity: Any
        to_dict: Dict[str, Any]
        is_empty: bool
        is_full: bool
        has_overflow: bool
        size: int

    Provides:

    Super Class:
        Toggle
    """
    def __init__(self):
        super().__init__()
    
    # @property
    # @abstractmethod
    # def entity(self) -> Any:
    #     pass
    #
    # @property
    # @abstractmethod
    # def to_dict(self) -> Dict[str, Any]:
    #     pass
    #
    # @property
    # @abstractmethod
    # def is_empty(self) -> bool:
    #     pass
    #
    # @property
    # @abstractmethod
    # def is_full(self) -> bool:
    #     pass
    #
    # @property
    # @abstractmethod
    # def has_overflow(self) -> bool:
    #     pass
    #
    # @property
    # @abstractmethod
    # def size(self) -> int:
    #     pass
    