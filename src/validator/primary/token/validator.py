# src/certifier/token/validator.py

"""
Module: certifier.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from blueprint import TokenBlueprint
from context import TokenHomeContext
from err import FormationNullException, TokenCertifierException
from model import HomeSquare
from result import ValidationResult
from schema.formation.schema import Formation
from toolkit import TokenToolkit
from util import LoggingLevelRouter
from validator import Certifier


class TokenCertifier(Certifier[TokenBlueprint]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a TokenBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: TokenToolkit

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        Certifier
    """
    
    def __init__(self, toolkit: TokenToolkit | None = TokenToolkit()):
        """
        Args:
            toolkit: TokenToolkit
        """
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> TokenToolkit:
        return cast(TokenToolkit, super().toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Certify a candidate is a TokenBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The validation_priming fails.
                    -   Either the board, owner or id get flagged unsafe.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
        Returns:
            ValidationResult
        Raises:
            TokenCertifierException
        """
        method = f"{self.__class__.__name__}.execute"
    
        
        # Handle the case that, the validator is not primed.
        validator_priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_=self.toolkit.blueprint_model,
            null_exception=self.toolkit.blueprint_null_exception,
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenCertifierException.MSG,
                    err_code=TokenCertifierException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast the candidate into a TokenBlueprint for additional tests. ---#
        blueprint = cast(self.toolkit.blueprint_model, candidate)
        
        # Handle the case that, any id in the blueprint is flagged.
        id_validation_result = self.toolkit.identity_service.validate_blueprint_id(
            owner_blueprint=blueprint,
            owner_name=blueprint.owner_name,
        )
        if id_validation_result.is_failure:
        # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenCertifierException.MSG,
                    err_code=TokenCertifierException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the team does not pass a validation check.
        team_validation = self.toolkit.team_validator.execute(
            candidate=blueprint.team
        )
        if team_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenCertifierException.MSG,
                    err_code=TokenCertifierException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # Handle the case that, the formation does not pass a validation check.
        formation_validation = self.toolkit.priming_validator.execute(
            candidate=blueprint.formation,
            target_model=Type[Formation],
            null_exception=FormationNullException(),
        )
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenCertifierException.MSG,
                    err_code=TokenCertifierException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # Handle the case that, the home_square gets flagged.
        home_detection_result = self.toolkit.home_detector.execute(
            context=TokenHomeContext(
                board=blueprint.team.board,
                square_name=blueprint.formation.home_square_name,
            ),
        )
        if home_detection_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenCertifierException.MSG,
                    err_code=TokenCertifierException.ERR_CODE,
                    ex=home_detection_result.exception,
                )
            )
        # Handle the case that, the rank is not safe to use.
        rank_validation_result = self.toolkit.blueprint_rank_processor.execute(
            blueprint=blueprint,
            toolkit=self.toolkit,
        )
        if rank_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenCertifierException.MSG,
                    err_code=TokenCertifierException.ERR_CODE,
                    ex=rank_validation_result.exception,
                )
            )
        # --- Completed validations successfully. Extract the payloads to build a new blueprint. ---#
        rank = cast(type(rank_validation_result.payload)
        id = cast(int, id_validation_result.payload)
        home_square = cast(HomeSquare, home_detection_result.payload)
        
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            TokenBlueprint(
                id=id,
                rank=rank,
                team=blueprint.team,
                formation=blueprint.formation,
                home_square=home_square,
            )
        )