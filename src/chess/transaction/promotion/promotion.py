from typing import cast

from chess.rank.rank_spec import RankSpec
from chess.transaction.orchestrator import TransactionOrchestrator
from chess.rank.queen import Queen, PromotedQueen

from chess.transaction.promotion.promote import PromotionRequestValidator
from chess.piece.piece import Piece

class PromotionException(RankException):
  ERROR_CODE = "RANK_PROMOTION_ERROR"
  DEFAULT_MESSAGE = "Rank promotion team_exception"

  def __init__(self, message=None):
    self.message = message or self.DEFAULT_MESSAGE
    super().__init__(self.message)

  def __str__(self):
    return f"[{self.ERROR_CODE}] {self.message}"

class PromotionTransaction(TransactionOrchestrator):

  @staticmethod
  def enter(request: PromotionRequest, boar=None):
    permission_result = PromotionRequestValidator.validate(request)
    if not permission_result.is_success():
      raise permission_result.exception

    client = cast(Piece, permission_result.request.actor)
    rank = cast(Queen, permission_result.request.resource)


    promoted_queen = PromotedQueen(
      old_rank=client.rank.name,
      name=RankSpec.QUEEN.name,
      letter=RankSpec.QUEEN.letter,
      value=RankSpec.QUEEN.ransom,
      per_side=RankSpec.QUEEN.quota,
      quadrants=RankSpec.QUEEN.quadrants,
    )

    piece = Piece(piece_id=client.id, name=client.name, team=client.team, rank=promoted_queen)
