# src/assurance/validator/struct/binder/team/validator.py

"""
Module: assurance.validator.struct.binder.team.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, cast

from artifcat import ValidationResult
from assurance import BinderValidator, TeamBinderLoader, TeamBinderLayerToolkit
from domain import (
    Archetype, Team, TeamBinder, TeamBinderBlueprint,
    TeamBinderPrimeExtract
)
from err import TeamBinderCarrierEmptyException, TeamBinderValidatorException
from exchange import TeamValidationRequest
from transit import TeamBinderCarrier, TeamCarrier
from util import IdFactory, LoggingLevelRouter


class TeamBinderValidator(BinderValidator[TeamBinder]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null Entity.
        2.  Run safety checks on structs and blueprints inside an Entity's payload.

    Attributes:
        loader: TeamBinderLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[TeamBinder]:

    Super Class:
        BinderValidator
    """
    
    def __init__(
            self,
            loader: Optional[TeamBinderLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[TeamBinderLoader]
        """
        super().__init__(loader=loader or TeamBinderLoader())
        
    @property
    def loader(self) -> TeamBinderLoader:
        return cast(TeamBinderLoader, super().loader)
    
    @property
    def toolkit(self) -> TeamBinderLayerToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[TeamBinderCarrier]:
        """
        Certify a TeamBinder's payload is either a TeamBinder or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The request is either null or not a TeamBinderValidatorRequest.
                    -   The request's payload is either,
                            null
                            not a TeamBinder
                            an empty TeamBinder.
                    -   Either the team, row, or column attributes are flagged unsafe.
            2.  Otherwise, Send a  with the correct type of payload in the success
                result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TeamBinder]
        Raises:
            TeamBinderValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
                
        # Handle the case that loader fails.
        loader = self.loader.execute(candidate)
        if loader.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderValidatorException.MSG,
                    err_code=TeamBinderValidatorException.ERR_CODE,
                    ex=loader.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        extract = cast(TeamBinderPrimeExtract, loader.authorization_applicant)
        carrier = extract.reference
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderValidatorException.MSG,
                    err_code=TeamBinderValidatorException.ERR_CODE,
                    ex=TeamBinderCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamBinderCarrierEmptyException.MSG,
                        err_code=TeamBinderCarrierEmptyException.ERR_CODE,
                    )
                )
            )
        # --- Cast priming_result into a request for additional tests. ---#
        entry: Dict[Archetype, Team] = {}
        for key in blueprint.bindings:
            team_validation = self.toolkit.dependency.team.extract_model(
                request=TeamValidationRequest(
                    item=TeamCarrier(model=entry[key]),
                    id=IdFactory.next_id(class_name="TeamBinderRequest")
                )
            )
            if team_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamBinderValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamBinderValidatorException.MSG,
                        err_code=TeamBinderValidatorException.ERR_CODE,
                        ex=team_validation.exception
                    )
                )
            team = cast(Team, team_validation.payload)
            entry[key] = team
        
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe TeamBinder.
        if extract.recipient_wants_model:
            model = TeamBinder(
                white_team=entry[Archetype.WHITE],
                black_team=entry[Archetype.BLACK],
            )
            payload = TeamBinderCarrier(model=model)
            return ValidationResult.success(payload)
        # Otherwise, the client is a TeamBinderBuilder that needs a Blueprint.
        payload = TeamBinderCarrier(
            blueprint=TeamBinderBlueprint(
                white_team=entry[Archetype.WHITE],
                black_team=entry[Archetype.BLACK],
            )
        )
        return ValidationResult.success(payload)

    
    
