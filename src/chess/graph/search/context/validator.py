# src/chess/graph/search/context/validator.py

"""
Module: chess.graph.search.context.validator
Author: Banji Lawal
Created: 2025-10-31
version: 1.0.0
"""

from typing import cast


from chess.system import Validator
from chess.graph import GraphSearchContext

class GraphSearchContextValidator(Validator[GraphSearchContext]):
  """
  # ROLE: Validation, Data Integrity

  # RESPONSIBILITIES:
  1. Process and validate parameters for creating `GraphSearchContext` instances.
  2. Create new `GraphSearchContext` objects if parameters meet specifications.
  2. Report errors and return `BuildResult` with error details.

  # PROVIDES:
  `BuildResult`: Return type containing the built `GraphSearchContext` or error information.

  # ATTRIBUTES:
  None
  """

  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, candidate: T) -> ValidationResult[GraphSearchContext]:
    """"""
    method = "GraphSearchContextValidator.validate"

    try:
      if candidate is None:
        return ValidationResult(exception=NullGraphSearchContextException(
          f"{method} {NullGraphSearchContextException.DEFAULT_MESSAGE}"
        ))

      if not isinstance(candidate, GraphSearchContext):
        return ValidationResult(exception=TypeError(
          f"{method} Expected graphSearchContext GraphSearchContext, got {type(candidate).__name__}"
        ))

      search_context = cast(GraphSearchContext, candidate)

      if len(search_context.to_dict()) == 0:
        return ValidationResult(exception=ZeroGraphSearchParamsException(
          f"{method} {ZeroGraphSearchParamsException.DEFAULT_MESSAGE}"
        ))

      if len(search_context.to_dict()) > 1:
        return ValidationResult(exception=TooManyGraphSearchParamsException(
          f"{method} {InvalidGraphSearchContextException.DEFAULT_MESSAGE}"
        ))

      if search_context.piece_id is not None:
        piece_id_validation = IdValidator.validate(search_context.piece_id)
        if piece_id_validation.is_failure():
          return ValidationResult(exception=piece_id_validation.exception)

      if search_context.name is not None:
        piece_name_validation = NameValidator.validate(search_context.name)
        if piece_name_validation.is_failure():
          return ValidationResult(exception=piece_name_validation.exception)

      if search_context.team_id is not None:
        team_id_validation = IdValidator.validate(search_context.team_id)
        if team_id_validation.is_failure():
          return ValidationResult(exception=team_id_validation.exception)

      if search_context.team_name is not None:
        team_name_validation = NameValidator.validate(search_context.team_name)
        if team_name_validation.is_failure():
          return ValidationResult(exception=team_name_validation.exception)

      if (search_context.rank_name is not None and
          search_context.rank_name not in [King.name, Queen.name, Rook.name, Bishop.name, Knight.name, Pawn.name]
      ):
          return ValidationResult(exception=GraphInvalidRankNameParamException(
            f"{method}: {GraphInvalidRankNameParamException.DEFAULT_MESSAGE}"
        ))

      if search_context.ransom not in range[Queen.ransom]:
        return ValidationResult(exception=GraphInvalidRankNameParamException(
          f"{method}: {GraphInvalidRankNameParamException.DEFAULT_MESSAGE}"
        ))

      if search_context.position is not None:
        position_validation = CoordValidator.validate(search_context.position)
        if position_validation.is_failure():
          return ValidationResult(exception=position_validation.exception)

      return ValidationResult(payload=search_context)

    except Exception as e:
      return ValidationResult(exception=e)