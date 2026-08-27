# src/transitbroadcast/observer/observer.py

"""
Module: transit.broadcast.observer.observer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod


from transit.broadcast import Notifier
from domain.model import Notification
from artifcat import DeletionResult, InsertionResult


class Observer(ABC):
    
    @abstractmethod
    def subscribe(self, notifier: Notifier) -> InsertionResult:
        pass
        
    @abstractmethod
    def unsubscribe(self, notifier: Notifier) -> DeletionResult:
        pass
        
    @abstractmethod
    def receive_notification(self, notification: Notification):
        pass
        
    