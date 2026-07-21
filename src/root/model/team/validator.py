# src/certifier/team/validator.py

"""
Module: certifier.team.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from model import Team
from root import RootCertifier
from toolkit import TeamToolkit


class TeamRootCertifier(RootCertifier[Team]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance

    Responsibilities:
        1.  Ensure a TeamBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: TeamToolkit

    Provides:
        -   execute(candidate) -> ValidationResult

    Super Class:
        Certifier
    """
    
    def __init__(self, toolkit: TeamToolkit | None = TeamToolkit()):
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> TeamToolkit:
        return cast(TeamToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Certify a candidate is a TeamBlueprint that is safe to use.

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
            TeamCertifierException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the validator is not primed.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            blueprint_model=self.toolkit.blueprint_model,
            blueprint_null_exception=self.toolkit.blueprint_null_exception,
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamCertifierException.MSG,
                    err_code=TeamCertifierException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into TeamBlueprint for routing attribute testing ---#
        blueprint = cast(TeamBlueprint, candidate)
        
        # Handle the case that, the blueprint's id does not pass.
        id_validation_result = self.toolkit.blueprint_id_validator.execute(
            candidate=blueprint.id,
        )
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamCertifierException.MSG,
                    err_code=TeamCertifierException.ERR_CODE,
                    ex=id_validation_result.exception
                )
            )
        # Handle the case that, the owner gets flagged.
        owner_validation_result = self.toolkit.player_validator.execute(blueprint.owner)
        if owner_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamCertifierException.MSG,
                    err_code=TeamCertifierException.ERR_CODE,
                    ex=owner_validation_result.exception
                )
            )
        # Handle the case that, the board is not safe.
        board_validation_result = self.toolkit.board_validator.excute(blueprint.board)
        if board_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamCertifierException.MSG,
                    err_code=TeamCertifierException.ERR_CODE,
                    ex=owner_validation_result.exception
                )
            )
        # Handle the case that, the schema is not safe.
        schema_validation_result = self.toolkit.priming_validator.execute(
            candidate=blueprint.schema,
            target_model=type[Archetype],
            null_exception=SchemaNullException(),
        )
        if schema_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamCertifierException.MSG,
                    err_code=TeamCertifierException.ERR_CODE,
                    ex=owner_validation_result.exception
                )
            )
        id = cast(int, id_validation_result.payload)
        board = cast(Board, board_validation_result.payload)
        owner = cast(type(blueprint.id), owner_validation_result.payload)
        schema = cast(Archetype, schema_validation_result.payload)
        
        # On validation success forward the work product to the caller.
        return ValidationResult.success(
            TeamBlueprint(
                id=id,
                board=board,
                owner=owner,
                schema=schema
            )
        )
