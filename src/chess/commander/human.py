class HumanCompetitor(Competitor):

    def __init__(self, competitor_id: int, name: str):
        super().__init__(competitor_id, name)


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, HumanCompetitor):
            return self.id == other.id
        return False