from enum import Enum



class MotionServiceConfig(Enum):
    def __new__(
        cls,
        rank_name: str,
        reachable_name: str,
        search_pattern_name: str,
        motion_service_name: str
    ):
        obj = object.__new__(cls)
        obj._value = rank_name
        obj._reachable_name: reachable_name
        obj._search_pattern_name: search_pattern_name
        obj._motion_service_name: motion_service_name
        return obj

