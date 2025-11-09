# src/chess/domain/search/context/factory.py

"""
Module: chess.domain.search.context.validator
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Any, cast

from chess.domain import VisitorSearchContext
from chess.system import Validator, IdValidator, NameValidator, ValidationResult, LoggingLevelRouter


class VisitorSearchContextValidator(Validator[VisitorSearchContext]):
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
  def validate(cls, candidate: Any) -> ValidationResult[VisitorSearchContext]:
    """"""
    method = "VisitorSearchContextValidator.validate"

    try:
      if candidate is None:
        return ValidationResult.failure(
          NullVisitorSearchContextException(f"{method} {NullVisitorSearchContextException.DEFAULT_MESSAGE}")
        )

      if not isinstance(candidate, VisitorSearchContext):
        return ValidationResult.failure(
          TypeError(f"{method} Expected VisitorSearchContext, got {type(candidate).__name__} instead.")
        )

      search_context = cast(VisitorSearchContext, candidate)

      if len(search_context.to_dict()) == 0:
        return ValidationResult.failure(
          ZeroVisitorSearchParamsException(f"{method} {ZeroVisitorSearchParamsException.DEFAULT_MESSAGE}")
        )

      if len(search_context.to_dict()) > 1:
        return ValidationResult.failure(
          TooManyGraphSearchParamsException(f"{method} {InvalidGraphSearchContextException.DEFAULT_MESSAGE}")
        )

      if search_context.id is not None:
        id_validation = IdValidator.validate(search_context.id)
        if id_validation.is_failure():
          return ValidationResult.failure(id_validation.exception)

      if search_context.name is not None:
        name_validation = NameValidator.validate(search_context.name)
        if name_validation.is_failure():
          return ValidationResult.failure(name_validation.exception)

      if search_context.team_id is not None:
        team_id_validation = IdValidator.validate(search_context.team_id)
        if team_id_validation.is_failure():
          return ValidationResult.failure(team_id_validation.exception)

      if search_context.team_name is not None:
        team_name_validation = NameValidator.validate(search_context.team_name)
        if team_name_validation.is_failure():
          return ValidationResult.failure(team_name_validation.exception)

      if search_context.rank_name is not None and search_context.rank_name not in RankSpec._name_:
          return ValidationResult.failure(
            InvalidRankNameParamException(
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