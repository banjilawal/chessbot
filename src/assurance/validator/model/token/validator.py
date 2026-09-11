# src/assurance/validator/model/token/validator.py

"""
Module: assurance.validator.model.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import ModelValidator, TokenValidatorToolkit
from domain import (
    Blueprint, CombatantBlueprint, Formation, HomeSquare, KingTokenBlueprint, PawnTokenBlueprint, Team, Token,
    TokenBlueprint,
    TokenValidationRequest
)
from err import FormationNullException, TokenValidationRequestNullException, TokenValidatorException
from transit import TokenCarrier
from util import LoggingLevelRouter


class TokenValidator(ModelValidator[Token]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TokenCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: TokenValidationToolkit

    Provides:
        - def execute(request: TokenValidationRequest) ->ValidationResult[TokenCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidationToolkit]
        """
        super().__init__(toolkit=toolkit or TokenValidatorToolkit())
    
    @property
    def toolkit(self) -> TokenValidatorToolkit:
        return cast(
            TokenValidatorToolkit,
            super().toolkit,
        )
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: TokenValidationRequest
    ) -> ValidationResult[TokenCarrier]:
        """
        Certify a candidate is a TokenCarrier whose payload is either a Token
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The candidate is not a TokenCarrier or its null.
                    - The candidate is an empty TokenCarrier.
                    - Any Token attribute is flagged.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate, Any
        Returns:
            ValidationResult[TokenCarrier]
        Raises:
            TokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is null or the wrong type.
        priming_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request,
            target_model=TokenValidationRequest,
            null_exception=TokenValidationRequestNullException(),
        )
        if priming_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=priming_validation.exception,
                )
            )
        # --- Cast the priming_validator payload for additional tests. ---#
        safe_request = cast(TokenValidationRequest, priming_validation.payload)
        
        # Handle the case that the request payload is null or the wrong type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=safe_request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast the carrier_validation payload for additional tests. ---#
        carrier = cast(
            TokenCarrier,
            carrier_validation.payload,
        )
        # --- Extract the blueprint to verify the attributes. ---#
        abstraction = carrier.extract_blueprint()
        
        # Handle the case that there is no blueprint.
        if abstraction is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=EmptyTokenCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyTokenCarrierException.MSG,
                        err_code=EmptyTokenCarrierException.ERR_CODE,
                    ),
                )
            )

        
        # Handle the case that any id in the blueprint is flagged.
        id_test = self.toolkit.helper.blueprint_id_extractor.execute(
            candidate=blueprint,
            blueprint_owner_name=blueprint.domain_class_name,
            blueprint_type=self.toolkit.metadata.types.blueprint,
            blueprint_null_exception=self.toolkit.metadata.nulls.blueprint,
        )
        if id_test.is_failure:
        # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=id_test.exception,
                )
            )
        # Handle the case that the team does not pass a validation check.
        team_test = self.toolkit.helper.team_validator.execute(
            candidate=blueprint.team
        )
        if team_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=team_test.exception,
                )
            )
        # Handle the case that the formation does not pass a validation check.
        formation_test = self.toolkit.helper.priming_validator.execute(
            candidate=blueprint.formation,
            target_model=Formation,
            null_exception=FormationNullException(),
        )
        if formation_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=formation_test.exception,
                )
            )
        # Handle the case that the home_square gets flagged.
        home_detection = self.toolkit.helper.home_extractor.execute(
            blueprint=blueprint,
        )
        if home_detection.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=home_detection.exception,
                )
            )
        

        if abstraction.is_king_token_blueprint:
            blueprint = cast(KingTokenBlueprint, abstraction)
        elif abstraction.is_pawn_token_blueprint:
            blueprint = cast(PawnTokenBlueprint, abstraction)
        else:
            blueprint = cast(CombatantBlueprint, abstraction)
        
        # Handle the case that the rank is not safe to use.
        rank = None
        if blueprint.is_pawn_token_blueprint:
            if blueprint.rank != blueprint.formation.rank:
                rank = blueprint.formation.rank
                rank_validation = self.toolkit.helper.rank_validator.execute(rank)
                if rank_validation.is_failure:
                    # Send the exception chain on failure.
                    return ValidationResult.failure(
                        TokenValidatorException(
                            cls_mthd=method,
                            cls_name=self.__class__.__name__,
                            msg=TokenValidatorException.MSG,
                            err_code=TokenValidatorException.ERR_CODE,
                            ex=rank_detection.exception,
                        )
                    )

        # --- Extract and cast payloads of the validation results. ---#
        id = cast(int, id_test.payload)
        team = cast(Team, team_test.payload)
        formation = cast(Formation, formation_test.payload)
        home_square = cast(HomeSquare, home_detection.payload)
        rank = formation.rank
        
        if carrier.is_carrying_model:
            return ValidationResult.success(
                TokenCarrier(
                    model=Token(
                        id=id,
                        team=team,
                        rank=formation.rank,
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
    
    