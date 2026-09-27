# src/assurance/validator/model/token/validator.py

"""
Module: assurance.validator.model.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import (
    CombatantTokenValidator, KingTokenValidator, ModelValidator, PawnTokenValidator,
    TokenValidatorToolkit
)
from domain import (
    Formation, HomeSquare, KingTokenBlueprint, Team, Token, TokenBlueprint, TokenDeployment,
    TokenPrimeExtract
)
from err import (
    FormationNullException, TokenDeploymentNullException, TokenValidationRouteException,
    TokenValidatorException
)
from exchange import TeamValidationRequest
from transit import CombatantCarrier, KingTokenCarrier, PawnTokenCarrier, TeamCarrier, TokenCarrier
from util import IdFactory, LoggingLevelRouter


class TokenValidator(ModelValidator[Token]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TokenCarrier is safe to use.

    Attributes:
        toolkit: TokenValidatorToolkit
        king_validator: KingTokenValidator
        pawn_validator: PawnTokenValidator
        combatant_validator: CombatantTokenValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[TokenCarrier]:

    Super Class:
        ModelValidator
    """
    _king_validator: KingTokenValidator
    _pawn_validator: PawnTokenValidator
    _combatant_validator: CombatantTokenValidator
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
            king_validator: Optional[KingTokenValidator] | None = None,
            pawn_validator: Optional[PawnTokenValidator] | None = None,
            combatant_validator: Optional[CombatantTokenValidator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidatorToolkit]
            king_validator: Optional[KingTokenValidator]
            pawn_validator: Optional[PawnTokenValidator]
            combatant_validator: Optional[CombatantTokenValidator]
        """
        super().__init__(toolkit=toolkit or TokenValidatorToolkit())
        self._king_validator = king_validator or KingTokenValidator()
        self._pawn_validator = pawn_validator or PawnTokenValidator()
        self._combatant_validator = combatant_validator or CombatantTokenValidator()
    
    @property
    def toolkit(self) -> TokenValidatorToolkit:
        return cast(TokenValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[TokenCarrier]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   The TokenCarrier subclass does not have a validation route.
                    -   Any of the following sub-validators fail.
                        -   KingTokenValidator
                        -   PawnTokenValidator
                        -   CombatantTokenValidator
            2.  Otherwise, send a TokenCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TokenCarrier]
        Raises:
            TokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        load_result = self.toolkit.loader.execute(candidate)
        if load_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=load_result.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(TokenPrimeExtract, load_result.payload)
        token_blueprint = cast(TokenBlueprint, prime_extract.blueprint)
        
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self.toolkit.blueprint_id_extractor.execute(
            candidate=token_blueprint,
            blueprint_owner_name=token_blueprint.domain_class_name,
            blueprint_type=self.toolkit.types.blueprint,
            blueprint_null_exception=self._toolkit.nulls.blueprint,
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # Handle the case that the formation is flagged.
        formation_validation = self.toolkit.priming_validator.execute(
            candidate=token_blueprint.formation,
            target_model=Formation,
            null_exception=FormationNullException(),
        )
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # Handle the case that the deployment is flagged..
        deployment_validation = self.toolkit.priming_validator.execute(
            candidate=token_blueprint.deployment,
            target_model=TokenDeployment,
            null_exception=TokenDeploymentNullException(),
        )
        if deployment_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=deployment_validation.exception,
                )
            )
        # Handle the case that the team is flagged.
        team_validation = self.toolkit.wrapper.team.extract_model(
            request=TeamValidationRequest(
                item=TeamCarrier(model=token_blueprint.team),
                id=IdFactory.next_id(class_name="TeamValidationRequest"),
            )
        )
        if team_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # Handle the case that the home_square gets flagged.
        home_detection = self.toolkit.home_square_extractor.execute(
            blueprint=token_blueprint,
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
        # --- Extract common Token validation payloads. ---#
        id = cast(int, id_validation.payload)
        team = cast(Team, team_validation.payload)
        home_square = cast(HomeSquare, home_detection.payload)
        formation = cast(Formation, formation_validation.payload)
        deployment = cast(TokenDeployment, deployment_validation.payload)

        # --- Select the appropriate validation route. ---#
        original_carrier = prime_extract.carrier
        
        # KingToken validation route.
        if carrier.is_king_token_carrier:
            raw = cast(KingTokenBlueprint, token_blueprint)
            king_blueprint = KingTokenBlueprint(
                id=id,
                team=team,
                formation=formation,
                deployment=deployment,
                position=raw.position,
                previous_position=raw.previous_position,
                readiness=raw.readiness,
                checkmate=raw.checkmate,
                check_warning=raw.check_warning,
            )
            king_prime_extractor = TokenPrimeExtract(
                carrier=original_carrier,
                blueprint=king_blueprint
            )
            return self._king_validator.execute(
                carrier=cast(KingTokenCarrier, carrier)
            )

        # PawnToken validation route.
        if carrier.is_pawn_token_carrier:
            return self._pawn_validator.execute(
                carrier=cast(PawnTokenCarrier, carrier)
            )
        # CombatantToken validation route.
        if carrier.is_combatant_token_carrier:
            return self._combatant_validator.execute(
                carrier=cast(CombatantCarrier, carrier)
            )
        # Handle the case that the carrier is not consistent.
        return ValidationResult.failure(
            TokenValidatorException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=TokenValidatorException.MSG,
                err_code=TokenValidatorException.ERR_CODE,
                ex=TokenValidationRouteException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidationRouteException.MSG,
                    err_code=TokenValidationRouteException.ERR_CODE,
                )
            )
        )
    