# src/broadcast/notifier/notifier.py

"""
Module: broadcast.notifier.notifier
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations
from typing import List

from model import Notification
from result import DeletionResult, InsertionResult


class Notifier:
    _notifications: List[Notification]
    _subscribers: []
    
    def __init__(self):
        self._notifications = []
        self._subscribers = []
        
    def add_subscriber(self, subscriber) -> InsertionResult:
        self._subscribers.append(subscriber)
        return InsertionResult.success()
        
    def remove_subscriber(self, subscriber) -> DeletionResult:
        self._subscribers.remove(subscriber)
        return DeletionResult.success(subscriber)
        
    def notify_all(self, notification: Notification):
        for subscriber in self._subscribers:
            subscriber.recieve(notification)
        
    