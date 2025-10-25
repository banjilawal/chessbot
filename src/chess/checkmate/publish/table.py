from chess.checkmate.publish.posting import KingCheckRecordPosting


class CheckRecordPostingTable:
    postings: list[KingCheckRecordPosting]
    
    def __init__(self):
        self.postings = []
        
    def add(self, posting: KingCheckRecordPosting):
        self.postings.append(posting)
        
    def remove_posting(selfself, post_id: int):
        pass