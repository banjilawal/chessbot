# src/operation/priming/assembly/team/operation.py

"""
Module: operation.priming.assembly.team.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from controller import WorkerRegistryController
from err import PrimingTeamAssemblyException
from model import Board, Team, TeamBlueprint
from operation import AssemblyPrimer
from result import ValidationResult
from toolkit import TeamToolkit
from util import LoggingLevelRouter


class TeamAssemblyPrimer(AssemblyPrimer[Team]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Assembly Process Owner
    
    Responsibilities:
        1.  Ensure a new Team instance is born safe and reliable.
    
    Attributes:
    
    Provides:
        -   def execute(
                blueprint: TeamBlueprint,
                toolkit: TeamToolkit,
        ) -> ValidationResult[TeamBlueprint]:
    
    Super Class:
        AssemblyPrimer
    """
    NAME  = "team_assembly_primer"
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def execute(
            cls,
            blueprint: TeamBlueprint,
            toolkit: TeamToolkit | None = None,
    ) -> ValidationResult[TeamBlueprint]:
        """
        Verify the integrity of the blueprint.
        
        Action:
            1.  Send an exception in the ValidationResult if any of these conditions occur:
                    -   Any component in the blueprint is flagged.
        Attributes:
            blueprint: TeamBlueprint
            toolkit: TeamToolkit
        Returns:
            ValidationResult[Team]
        Raises:
            PrimingTeamAssemblyException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TeamToolkit()
        
        # Handle the case that, a assembly param does not pass a validation check.
        blueprint_validation_result = cls._run_validations(
            blueprint=blueprint,
            toolkit=toolkit,
        )
        if blueprint_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingTeamAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingTeamAssemblyException.MSG,
                    err_code=PrimingTeamAssemblyException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )
        return ValidationResult.success(blueprint_validation_result.payload)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_validations(cls,
            blueprint: TeamBlueprint,
            toolkit: TeamToolkit,
    ) -> ValidationResult[TeamBlueprint]:
        """
        """
        method = f"{cls.__name__}._run_validations"
        
        # Handle the case that, the id is not certified as safe.
        id_validation_result = toolkit.identity_service.verify_priming_id(
            id=blueprint.id,
            class_name="Team",
        )
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingTeamAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingTeamAssemblyException.MSG,
                    err_code=PrimingTeamAssemblyException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the schema does not pass a validation check.
        schema_validation_result = toolkit.schema_service.validator.execute(
            candidate=blueprint.schema
        )
        if schema_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingTeamAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingTeamAssemblyException.MSG,
                    err_code=PrimingTeamAssemblyException.ERR_CODE,
                    ex=schema_validation_result.exception,
                )
            )
        # Handle the case that, the owner does not pass a validation check.
        owner_validation_result = toolkit.player_service.validator.execute(
            candidate=blueprint.owner
        )
        if owner_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingTeamAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingTeamAssemblyException.MSG,
                    err_code=PrimingTeamAssemblyException.ERR_CODE,
                    ex=owner_validation_result.exception,
                )
            )
        # Handle the case that, the board does not pass a validation check.
        board_validation_result = cls._verify_board(
            blueprint=blueprint,
            toolkit=toolkit,
        )
        if board_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingTeamAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingTeamAssemblyException.MSG,
                    err_code=PrimingTeamAssemblyException.ERR_CODE,
                    ex=board_validation_result.exception,
                )
            )
        return ValidationResult.success(
            TeamBlueprint(
                id=id_validation_result.payload,
                schema=blueprint.schema,
                owner=blueprint.owner,
                board=blueprint.board,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _verify_board(
            cls,
            blueprint: TeamBlueprint,
            toolkit: TeamToolkit,
    ) -> ValidationResult[Board]:
        """
        Verify the id if it already exists or create a new one.

        Action:
            1.  Send an exception chain in the ValidationResult if an existing id
                is not certified as safe.
            2.  Otherwise, send the success result.
        Args:
            blueprint: TeamBlueprint
            toolkit: TeamToolkit
        Returns:
            ValidationResult[int]
        Raises:
            PrimingTeamAssemblyException
        """
        method = f"{cls.__name__}._verify_board"
        
        # Handle the case that, the board is flagged unsafe.
        board_validation_result = toolkit.board_service.validator.execute(
            candidate=blueprint.board
        )
        if board_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingTeamAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingTeamAssemblyException.MSG,
                    err_code=PrimingTeamAssemblyException.ERR_CODE,
                    ex=board_validation_result.exception,
                )
            )
        # Handle the case that, the schema's binding slot is already occupied.
        slot_search_result = toolkit.team_binder_service.slot_occupant(
            schema=blueprint.schema,
            id=blueprint.board.team_binder
        )
        if slot_search_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingTeamAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingTeamAssemblyException.MSG,
                    err_code=PrimingTeamAssemblyException.ERR_CODE,
                    ex=slot_search_result.exception,
                )
            )
        if not slot_search_result.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingTeamAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingTeamAssemblyException.MSG,
                    err_code=PrimingTeamAssemblyException.ERR_CODE,
                    ex=slot_search_result.exception,
                )
            )
        # --- Return the work product. ---#
        return ValidationResult.success(blueprint.board)


# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register_worker(worker=TeamAssemblyPrimer)

        