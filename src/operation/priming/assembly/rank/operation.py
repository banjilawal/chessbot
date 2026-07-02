# src/operation/priming/assembly/rank/operation.py

"""
Module: operation.priming.assembly.rank.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from controller import WorkerRegistryController
from err import PrimingRankAssemblyException
from model import Rank, RankBlueprint

from operation import AssemblyPrimer
from result import ValidationResult
from toolkit import RankToolkit
from util import LoggingLevelRouter


class RankAssemblyPrimer(AssemblyPrimer[Rank]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Assembly Process Owner
    
    Responsibilities:
        1.  Ensure a new Rank instance is born safe and reliable.
    
    Attributes:
    
    Provides:
        -   def execute(
                blueprint: RankBlueprint,
                toolkit: RankToolkit,
        ) -> ValidationResult[RankBlueprint]:
    
    Super Class:
        AssemblyPrimer
    """
    NAME = "rank_assembly_primer"
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def execute(
            cls,
            blueprint: RankBlueprint,
            toolkit: RankToolkit | None = None,
    ) -> ValidationResult[RankBlueprint]:
        """
        Verify the integrity of the blueprint.
        
        Action:
            1.  Send an exception in the ValidationResult if any of these conditions occur:
                    -   Any component in the blueprint is flagged.
        Attributes:
            blueprint: RankBlueprint
            toolkit: RankToolkit
        Returns:
            ValidationResult[Rank]
        Raises:
            PrimingRankAssemblyException
        """
        method = f"{cls.__name__}.execute"
        
        if toolkit is None:
            toolkit = RankToolkit()
        
        # Handle the case that, a assembly param does not pass a validation check.
        blueprint_validation_result = cls._run_validations(
            blueprint=blueprint,
            toolkit=toolkit,
        )
        if blueprint_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingRankAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingRankAssemblyException.MSG,
                    err_code=PrimingRankAssemblyException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )
        return ValidationResult.success(blueprint_validation_result.payload)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_validations(cls,
            blueprint: RankBlueprint,
            toolkit: RankToolkit,
    ) -> ValidationResult[RankBlueprint]:
        """
        """
        method = f"{cls.__name__}._run_validations"
        
        # Handle the case that, the id is not certified as safe.
        id_validation_result = toolkit.identity_service.verify_priming_id(
            id=blueprint.id,
            class_name="Rank",
        )
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingRankAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingRankAssemblyException.MSG,
                    err_code=PrimingRankAssemblyException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the persona does not pass a validation check.
        persona_validator_result = toolkit.persona_validator.execute(
            candidate=blueprint.persona
        )
        if persona_validator_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingRankAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingRankAssemblyException.MSG,
                    err_code=PrimingRankAssemblyException.ERR_CODE,
                    ex=persona_validator_result.exception,
                )
            )
        return ValidationResult.success(
            RankBlueprint(
                id=id_validation_result.payload,
                persona=blueprint.persona,
            )
        )

# Register the operation.
WorkerRegistryController.register_worker(worker=RankAssemblyPrimer)
        