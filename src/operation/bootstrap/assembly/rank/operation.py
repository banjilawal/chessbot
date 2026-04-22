# src/operation/bootstrap/assembly/rank/operation.py

"""
Module: operation.bootstrap.assembly.rank.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from err import BootstrapRankAssemblyException
from model import Rank, RankBlueprint

from operation import AssemblyBootstrapper
from result import ValidationResult
from system import LoggingLevelRouter
from toolkit import RankToolkit


class RankAssemblyBootstrapper(AssemblyBootstrapper[Rank]):
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
        AssemblyBootstrapper
    """
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
            BootstrapRankAssemblyException
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
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapRankAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapRankAssemblyException.MSG,
                    err_code=BootstrapRankAssemblyException.ERR_CODE,
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
        id_validation_result = toolkit.identity_service.verify_bootstrap_id(
            id=blueprint.id,
            class_name="Rank",
        )
        if id_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapRankAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapRankAssemblyException.MSG,
                    err_code=BootstrapRankAssemblyException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the persona does not pass a validation check.
        persona_validator_result = toolkit.persona_validator.validate(
            candidate=blueprint.persona
        )
        if persona_validator_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapRankAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapRankAssemblyException.MSG,
                    err_code=BootstrapRankAssemblyException.ERR_CODE,
                    ex=persona_validator_result.exception,
                )
            )
        return ValidationResult.success(
            RankBlueprint(
                id=id_validation_result.payload,
                persona=blueprint.persona,
            )
        )

        