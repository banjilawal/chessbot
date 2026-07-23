# src/certifier/token/validator.py

"""
Module: certifier.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import TokenBlueprint
from carrier import TokenCarrier
from context import TokenHomeContext
from err import FormationNullException, TokenRootCertifierException
from model import HomeSquare, Team, Token
from root import ModelRootCertifier
from result import ValidationResult
from schema import Formation
from toolkit import TokenToolkit
from util import LoggingLevelRouter


class TokenRootCertifier(ModelRootCertifier[Token]):
    """
    Role
        -   Integrity Maintenance
        -   Consistency Assurance


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
    def execute(self, candidate, Any) -> ValidationResult:
        """
        Certify a candidate is a TokenBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The candidate is not a TokenDtoCarrier.
                    -   The candidate is an empty TokenDtoCarrier.
                    -   Either the board, team, formation, rank or id get flagged unsafe.
            2.  For a model_carrier send a Token in the success result. Otherwise, send a TokeBlueprint.
        Args:
            candidate, Any
        Returns:
            ValidationResult
        Raises:
            TokenCertifierException
            TokenDtoCarrierNullException
        """
        method = f"{self.__class__.__name__}.execute"
        
        carrier_validation = self.carrier_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.carrier_model,
            model_null_exception=self.toolkit.carrier_null_exception,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenRootCertifierException.MSG,
                    err_code=TokenRootCertifierException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(self.toolkit.carrier_model, carrier_validation.payload)

        # --- Cast the candidate into a TokenBlueprint for additional tests. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that, any id in the blueprint is flagged.
        id_test = self.toolkit.identity_service.validate_blueprint_id(
            owner_blueprint=blueprint,
            owner_name=blueprint.model_class_name,
        )
        if id_test.is_failure:
        # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenRootCertifierException.MSG,
                    err_code=TokenRootCertifierException.ERR_CODE,
                    ex=id_test.exception,
                )
            )
        # Handle the case that, the team does not pass a validation check.
        team_test = self.toolkit.team_validator.execute(
            candidate=blueprint.team
        )
        if team_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenRootCertifierException.MSG,
                    err_code=TokenRootCertifierException.ERR_CODE,
                    ex=team_test.exception,
                )
            )
        # Handle the case that, the formation does not pass a validation check.
        formation_test = self.toolkit.priming_validator.execute(
            candidate=blueprint.formation,
            target_model=Type[Formation],
            null_exception=FormationNullException(),
        )
        if formation_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenRootCertifierException.MSG,
                    err_code=TokenRootCertifierException.ERR_CODE,
                    ex=formation_test.exception,
                )
            )
        # Handle the case that, the home_square gets flagged.
        home_detection = self.toolkit.home_detector.execute(
            context=TokenHomeContext(
                board=blueprint.team.board,
                square_name=blueprint.formation.home_square_name,
            ),
        )
        if home_detection.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenRootCertifierException.MSG,
                    err_code=TokenRootCertifierException.ERR_CODE,
                    ex=home_detection.exception,
                )
            )
        # Handle the case that, the rank is not safe to use.
        rank_test = self.toolkit.rank_extractor.execute(
            blueprint=blueprint,
            toolkit=self.toolkit,
        )
        if rank_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenRootCertifierException.MSG,
                    err_code=TokenRootCertifierException.ERR_CODE,
                    ex=rank_test.exception,
                )
            )
        # --- Extract and cast payloads of the validation results. ---#
        id = cast(int, id_test.payload)
        team = cast(Team, team_test.payload)
        formation = cast(Formation, formation_test.payload)
        home_square = cast(HomeSquare, home_detection.payload)
        rank = cast(type(rank_test.payload), rank_test.payload)
        
        if carrier.is_carrying_model:
            return ValidationResult.success(
                TokenCarrier(
                    model=Token(
                        id=id,
                        team=team,
                        rank=rank,
                        formation=formation,
                        home_square=home_square,
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            TokenCarrier(
                blueprint=TokenBlueprint(
                    id=id,
                    rank=rank,
                    team=team,
                    formation=formation,
                    home_square=home_square,
                )
            )
        )