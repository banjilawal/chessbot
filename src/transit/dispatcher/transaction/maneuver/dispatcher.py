# src/transit/dispatcher/maneuver/dispatcher.py

"""
Module: transit.dispatcher.maneuver.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod

from exchange import ManeuverRequest
from transit import Dispatcher
from util import LoggingLevelRouter

class ManeuverDispatcher(Dispatcher[ManeuverRequest]):
    """
    Role
        -   Permission Maneuver Manager

    Responsibilities:
        1.  Grant

    Attributes:
        mover: Mover

    Provides:
        -   def  execute(self, request: ManeuverRequest) -> ManeuverResponse

    Super Class:
        Dispatcher
    """
    
    _mover: Mover
    
    def __init__(self, mover: Mover):
        """
        Args:
            mover: Mover
        """
        self._mover = mover
        
    @property
    def mover(self) -> Mover:
        return self._mover
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverResponse:
        """
        Decide if an activity can be performed.
        Args:
            request: T
        Returns:
            ManeuverResponse
        Raises:
            ManeuverDispatcherException
        """
        pass