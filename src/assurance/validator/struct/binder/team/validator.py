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
from assurance import BinderValidator, TeamBinderLoader, TeamBinderValidatorToolkit
from domain import Archetype, Team, TeamBinder
from err import TeamBinderConsistencyException, TeamBinderValidatorException
from exchange import TeamBinderValidationRequest, TeamValidationRequest
from transit import TeamCarrier
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
    def toolkit(self) -> TeamBinderValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[TeamBinder]:
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
        load = self.loader.execute(candidate)
        if load.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderValidatorException.MSG,
                    err_code=TeamBinderValidatorException.ERR_CODE,
                    ex=load.exception,
                )
            )
        # --- Cast priming_result into a request for additional tests. ---#
        struct = cast(TeamBinder, load.payload)
        
        if struct.is_not_consistent:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderValidatorException.MSG,
                    err_code=TeamBinderValidatorException.ERR_CODE,
                    ex=TeamBinderConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamBinderConsistencyException.MSG,
                        err_code=TeamBinderConsistencyException.ERR_CODE,
                    )
                )
            )
        
        entry = struct.to_dict
        bindings: Dict[str, Team] = {}
        for key in struct.to_dict:
            team_validation = self.toolkit.wrapper.team.extract_model(
                request=TeamValidationRequest(
                    item=TeamCarrier(model=entry[key]),
                    id=IdFactory.next_id(class_name="TeamValidationRequest")
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
            bindings[key] = team
            
        # --- Forward the appropriate work product to the caller. ---#
        return ValidationResult.success(
            TeamBinder(
                white_team=bindings[Archetype.WHITE],
                black_team=bindings[Archetype.BLACK],
            )
        )

    
    
