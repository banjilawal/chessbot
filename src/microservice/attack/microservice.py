# src/microservice/attack/microservice.py

"""
Module: microservice.attack.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod

from event import AttackEvent
from microservice import Microservice
from util import IdFactory
from validation import Validator


class AttackEventService(Microservice[AttackEvent]):
    """
    Role:Microservice, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Attack microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Attack state.
    4.  Single entry and entry points to Attack lifecycle.

    Super Class:
        *   Microservice

    Provides:


    # INHERITED ATTRIBUTES:
        *   See Microservice for inherited attributes.
    """
    

    
    DEFAULT_NAME = "AttackService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int | None = IdFactory.next_id(class_name="AttackEventService"),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   schema (str)
            *   build (AttackFactory)
            *   validation (AttackValidator)
        # RETURNS:
            None
        Raises:
            None
        """
        super().__init__(id=id, name=name)
    
    @property
    @abstractmethod
    def validator(self) -> Validator[AttackEvent]:
        pass
    
    # @property
    # @abstractmethod
    # def builder(self) -> Builder[AttackEvent]:
    #     pass
    #
    
    