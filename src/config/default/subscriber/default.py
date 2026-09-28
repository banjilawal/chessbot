# src/config/setting/subscriber/default.py

"""
Module: config.setting.subscriber.default
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from software import Subscriber

class Default:
    _subscriber = Subscriber(
            id=1,
            first_name="Chimanda",
            last_name="Ngozi",
            email="chimanda.ngozi@mail.com"
        )
    
    @classmethod
    def subscriber(cls) -> Subscriber:
        return cls._subscriber
        