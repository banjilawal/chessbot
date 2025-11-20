# src/chess/discoverySearchContext/discoverySearchContext.py
"""
Module: chess.discoverySearchContext.discoverySearchContext
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0`
"""

from typing import cast, TypeVar

from chess.coord import CoordValidator
from chess.rank import Bishop, King, Knight, Pawn, Queen, Rank, Rook
from chess.system import IdValidator, LoggingLevelRouter, NameValidator, Validator, ValidationResult
from chess.piece import (
  DiscoverySearchContext, InvalidDiscoverySearchContextException, NullDiscoverySearchContextException,
  TooManyDiscoverySearchParamsException, ZeroDiscoverySearchParamsException,  DiscoveryInvalidRankNameParamException
)

T = TypeVar('V')

class DiscoverySearchContextValidator(Validator[DiscoverySearchContext]):
  """
  # ROLE: Validation, Data Integrity

  # RESPONSIBILITIES:
  1. Process and validate parameters for creating `DiscoverySearchContext` instances.
  2. Create new `DiscoverySearchContext` objects if parameters meet specifications.
  2. Report errors and return `BuildResult` with error details.

  # PROVIDES:
  `BuildResult`: Return type containing the built `DiscoverySearchContext` or error information.

  # ATTRIBUTES:
  None
  """

  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, candidate: T) -> ValidationResult[DiscoverySearchContext]:
    """"""
    method = "DiscoverySearchContextValidator.validate"

    try:
      if candidate is None:
        return ValidationResult(exception=NullDiscoverySearchContextException(
          f"{method} {NullDiscoverySearchContextException.DEFAULT_MESSAGE}"
        ))

      if not isinstance(candidate, DiscoverySearchContext):
        return ValidationResult(exception=TypeError(
          f"{method} Expected discoverySearchContext DiscoverySearchContext, got {type(candidate).__name__}"
        ))

      search_context = cast(DiscoverySearchContext, candidate)

      if len(search_context.to_dict()) == 0:
        return ValidationResult(exception=ZeroDiscoverySearchParamsException(
          f"{method} {ZeroDiscoverySearchParamsException.DEFAULT_MESSAGE}"
        ))

      if len(search_context.to_dict()) > 1:
        return ValidationResult(exception=TooManyDiscoverySearchParamsException(
          f"{method} {InvalidDiscoverySearchContextException.DEFAULT_MESSAGE}"
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
          return ValidationResult(exception=DiscoveryInvalidRankNameParamException(
            f"{method}: {DiscoveryInvalidRankNameParamException.DEFAULT_MESSAGE}"
        ))

      if search_context.ransom not in range[Queen.ransom]:
        return ValidationResult(exception=DiscoveryInvalidRankNameParamException(
          f"{method}: {DiscoveryInvalidRankNameParamException.DEFAULT_MESSAGE}"
        ))

      if search_context.position is not None:
        position_validation = CoordValidator.validate(search_context.position)
        if position_validation.is_failure():
          return ValidationResult(exception=position_validation.exception)

      return ValidationResult(payload=search_context)

    except Exception as e:
      return ValidationResult(exception=e)