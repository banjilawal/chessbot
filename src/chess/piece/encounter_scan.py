from typing import List

from chess.piece import Encounter, NullEncounterException


class EncounterScan:
    _items: List[Encounter]

    def __init__(self):
        self._items = []


    @property
    def items(self) -> List[Encounter]:
        return self._items.copy()


    def find_by_piece_id(self, piece_id: int) -> Encounter | None:
        for encounter in self._items:
            if encounter.id == piece_id:
                return encounter
        return None


    def add_encounter(self, record: Encounter):
        method = "RecordList.add_record"

        if record is None:
            raise NullEncounterException(f"{method}:{NullEncounterException.DEFAULT_MESSAGE}")

        if record not in self._items:
            self._items.append(record)


    def reset(self):
        self._items.clear()



