from typing import List

from chess.piece import Encounter, NullEncounterException


class EncounterLog:
    _items: List[Encounter]

    def __init__(self):
        self._items = []


    @property
    def items(self) -> List[Encounter]:
        return self._items


    def add_encounter(self, record:Encounter):
        method = "RecordList.add_record"

        if record is None:
            raise NullEncounterException(f"{method}:{NullEncounterException.DEFAULT_MESSAGE}")

        if record not in self._items:
            self._items.append(record)


    def reset(self):
        self._items.clear()








