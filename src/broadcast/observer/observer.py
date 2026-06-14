# src/broadcast/observer/observer.py

"""
Module: broadcast.observer.observer
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations
from abc import ABC, abstractmethod


from broadcast import Notifier
from model import Notification
from result import DeletionResult, InsertionResult, Result


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
        
    