# src/assurance/validator/domain/search/stack/team/checker.py

"""
Module: assurance.validator.domain.search.stack.team.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import StackContextValidator, TeamValidationBundle
from domain import Archetype, TeamSearchSearchContext
from err import (
    ExcessTeamContextFlagsException, GameColorNullException, TeamContextCheckerException,
    TeamContextValidationRouteException, ZeroTeamContextFlagsException
)
from util import LoggingLevelRouter


class TeamContextValidator(StackContextValidator[TeamSearchSearchContext]):
    """
    Role
        -  Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null TeamSearchContext.
        2.  Run safety checks on any TeamSearchContext attributes that are enabled.

    Attributes:
        bundle: TeamValidationBundle

    Provides:
        -  def execute(candidate: Any) -> ValidationResult[TeamSearchContext]:

    Super Class:
        StackSearchContextChecker
    """
    
    def __init__(self, bundle: Optional[TeamValidationBundle] | None = None, ):
        super().__init__(bundle=bundle or TeamValidationBundle())
    
    
    @property
    def bundle(self) -> TeamValidationBundle:
        return cast(TeamValidationBundle, super().bundle)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[TeamSearchSearchContext]:
        """
        Certify a candidate is a TeamSearchContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -  The candidate is not a TeamSearchContext.
                    -  The wrong number of search attributes is enabled.
                    -  An enabled search attribute fails a safety check.
            2.  Otherwise, send a TokeSearchContext in the success result.
        Args:
            candidate, Any
        Returns:
            ValidationResult[TeamSearchContext]
        Raises:
            TeamContextCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the validator is not primed.
        priming = self.bundle.priming_validator.execute(
            candidate=candidate,
            target_model=self.bundle.types.search_context,
            null_exception=self.bundle.nulls.search_context,
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamContextCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamContextCheckerException.MSG,
                    err_code=TeamContextCheckerException.ERR_CODE,
                    ex=priming.exception
                )
            )
        # --- Cast the candidate into TeamContext for routing attribute testing ---#
        context = cast(TeamSearchSearchContext, priming.payload)
        
        # Handle the case that, no flags are enabled.
        if context.has_no_active_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamContextCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamContextCheckerException.MSG,
                    err_code=TeamContextCheckerException.ERR_CODE,
                    ex=ZeroTeamContextFlagsException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ZeroTeamContextFlagsException.MSG,
                        err_code=ZeroTeamContextFlagsException.ERR_CODE
                    )
                )
            )
        # Handle the case that too many context flags are enabled.
        if context.has_excessive_active_contexts:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamContextCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamContextCheckerException.MSG,
                    err_code=TeamContextCheckerException.ERR_CODE,
                    ex=ExcessTeamContextFlagsException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ExcessTeamContextFlagsException.MSG,
                        err_code=ExcessTeamContextFlagsException.ERR_CODE
                    )
                )
            )
        # --- Route to the appropriate validation path. ---#
        
        # Certification for the search-by-id target.
        if context.id is not None:
            validation_result = self.bundle.identity_service.validate_id(
                candidate=context.id
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamContextCheckerException.MSG,
                        err_code=TeamContextCheckerException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-owner target.
        if context.owner is not None:
            validation_result = self.bundle.owner_validator.execute(
                candidate=context.owner
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamContextCheckerException.MSG,
                        err_code=TeamContextCheckerException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-board target.
        if context.board is not None:
            validation_result = self.bundle.board_validator.execute(
                candidate=context.board
            )
            if validation_result.is_failure:
                if validation_result.is_failure:
                    # Send the exception chain on failure.
                    return ValidationResult.failure(
                        TeamContextCheckerException(
                            cls_mthd=method,
                            cls_name=self.__class__.__name__,
                            msg=TeamContextCheckerException.MSG,
                            err_code=TeamContextCheckerException.ERR_CODE,
                            ex=validation_result.exception
                        )
                    )
                # On validation success forward the work product to the caller.
                return ValidationResult.success(context)
        
        # Certification for the search-by-color target.
        if context.color is not None:
            validation_result = self.bundle.priming_validator.execute(
                candidate=context.color,
                model_type=GameColor,
                null_exception=GameColorNullException,
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamContextCheckerException.MSG,
                        err_code=TeamContextCheckerException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-archetype target.
        if context.archetype is not None:
            validation_result = self.bundle.priming_validator.execute(
                candidate=context.archetype,
                model_type=Archetype,
                null_exception=ArchetypeNullException,
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TeamContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamContextCheckerException.MSG,
                        err_code=TeamContextCheckerException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
                # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Return the exception chain if there is no validation route for the context.
        return ValidationResult.failure(
            TeamContextCheckerException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=TeamContextCheckerException.MSG,
                err_code=TeamContextCheckerException.ERR_CODE,
                ex=TeamContextValidationRouteException(
                    msg=TeamContextValidationRouteException.MSG,
                    err_code=TeamContextValidationRouteException.ERR_CODE,
                )
            )
        )
