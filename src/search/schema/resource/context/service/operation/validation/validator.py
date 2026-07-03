# src/logic/schema/database/search/context/service/operation/validation/validator.py

"""
Module: logic.schema.database.search.context.service.operation.validation.validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, cast


from system import LoggingLevelRouter, Validator, ValidationResult
from model.catalog import (
    ExcessSchemaContextFlagsException, NullSchemaContextException, SchemaContext, SchemaContextIntegrityWorkers,
    SchemaContextValidationException, SchemaContextValidationRouteException, ZeroSchemaContextFlagsException
)

class SchemaContextValidator(Validator[SchemaContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a SchemaContext instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    rank: Any,
                    workers: SchemaContextIntegrityWorkers,
            ) -> BuildResult[SchemaContext]:

    Super Class:
        Validator
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            workers: SchemaContextIntegrityWorkers,
    ) -> ValidationResult[SchemaContext]:
        """
        Certify a rank is a SchemaContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The rank is null.
                    -   The rank is not a SchemaContext.
                    -   It has no attributes enabled.
                    -   It has more than one attribute enabled.
                    -   The enabled attribute fails a safety check.
                    -   There is no validation path for the attribute.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
            workers: SchemaContextIntegrityWorkers
        Returns:
            ValiationResult[SchemaContext]
        Raises:
            TypeError
            NullSchemaContextException
            ZeroSchemaContextFlagsException
            SchemaContextValidationException
            ExcessSchemaContextFlagsException
            TeamContextValidationRouteException
        """
        method = f"{cls.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=SchemaContextValidationException.OP,
                    msg=SchemaContextValidationException.MSG,
                    err_code=SchemaContextValidationException.ERR_CODE,
                    mthd_rslt_type=SchemaContextValidationException.MTHD_RSLT,
                    ex=NullSchemaContextException(
                        msg=SchemaContextValidationException.MSG,
                        err_code=SchemaContextValidationException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, SchemaContext):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=SchemaContextValidationException.OP,
                    msg=SchemaContextValidationException.MSG,
                    err_code=SchemaContextValidationException.ERR_CODE,
                    mthd_rslt_type=SchemaContextValidationException.MTHD_RSLT,
                    ex=TypeError(
                        f"Expected SchemaContext, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the candidate into SchemaContext for additional tests. ---#
        context = cast(SchemaContext, candidate)
        
        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=SchemaContextValidationException.OP,
                    msg=SchemaContextValidationException.MSG,
                    err_code=SchemaContextValidationException.ERR_CODE,
                    mthd_rslt_type=SchemaContextValidationException.MTHD_RSLT,
                    ex=ZeroSchemaContextFlagsException(
                        msg=ZeroSchemaContextFlagsException.MSG,
                        err_code=ZeroSchemaContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=SchemaContextValidationException.OP,
                    msg=SchemaContextValidationException.MSG,
                    err_code=SchemaContextValidationException.ERR_CODE,
                    mthd_rslt_type=SchemaContextValidationException.MTHD_RSLT,
                    ex=ExcessSchemaContextFlagsException(
                        msg=ExcessSchemaContextFlagsException.MSG,
                        err_code=ExcessSchemaContextFlagsException.ERR_CODE,
                    )
                )
            )
        # --- Route to the appropriate validation branch. ---#
        
        # Certification for the search-by-id target.
        if context.id is not None:
            validation_result = workers.identity_service.validate_id(
                candidate=context.id
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SchemaContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=SchemaContextValidationException.OP,
                        msg=SchemaContextValidationException.MSG,
                        err_code=SchemaContextValidationException.ERR_CODE,
                        mthd_rslt_type=SchemaContextValidationException.MTHD_RSLT,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-designation target.
        if context.designation is not None:
            validation_result = workers.identity_service.validate_name(
                candidate=context.designation
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SchemaContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=SchemaContextValidationException.OP,
                        msg=SchemaContextValidationException.MSG,
                        err_code=SchemaContextValidationException.ERR_CODE,
                        mthd_rslt_type=SchemaContextValidationException.MTHD_RSLT,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-opening_square_name target.
        if context.opening_square_name is not None:
            validation_result = workers.identity_service.validate_name(
                candidate=context.opening_square_name
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SchemaContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=SchemaContextValidationException.OP,
                        msg=SchemaContextValidationException.MSG,
                        err_code=SchemaContextValidationException.ERR_CODE,
                        mthd_rslt_type=SchemaContextValidationException.MTHD_RSLT,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-coord target.
        if context.current_position is not None:
            validation_result = workers.coord_service.validate.build(
                rank=context.current_position
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SchemaContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=SchemaContextValidationException.OP,
                        msg=SchemaContextValidationException.MSG,
                        err_code=SchemaContextValidationException.ERR_CODE,
                        mthd_rslt_type=SchemaContextValidationException.MTHD_RSLT,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller..
            return ValidationResult.success(context)
        
        # Certification for the search-by-team target.
        if context.team is not None:
            validation_result = workers.team_service.validate.build(
                rank=context.team
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SchemaContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=SchemaContextValidationException.OP,
                        msg=SchemaContextValidationException.MSG,
                        err_code=SchemaContextValidationException.ERR_CODE,
                        mthd_rslt_type=SchemaContextValidationException.MTHD_RSLT,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-rank target.
        if context.rank is not None:
            validation_result = workers.rank_service.validate.build(
                rank=context.rank
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SchemaContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=SchemaContextValidationException.OP,
                        msg=SchemaContextValidationException.MSG,
                        err_code=SchemaContextValidationException.ERR_CODE,
                        mthd_rslt_type=SchemaContextValidationException.MTHD_RSLT,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-color target.
        if context.color is not None:
            validation_result = workers.color_validator.build(
                candidate=context.color
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SchemaContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=SchemaContextValidationException.OP,
                        msg=SchemaContextValidationException.MSG,
                        err_code=SchemaContextValidationException.ERR_CODE,
                        mthd_rslt_type=SchemaContextValidationException.MTHD_RSLT,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Certification for the search-by-ransom target.
        if context.ransom is not None:
            validation_result = workers.number_validator.build(
                rank=context.ransom,
                floor=workers.persona_service.min_ransom,
                ceiling=workers.persona_service.max_ransom,
            )
            # Send the exception chain on failure.
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SchemaContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=SchemaContextValidationException.OP,
                        msg=SchemaContextValidationException.MSG,
                        err_code=SchemaContextValidationException.ERR_CODE,
                        mthd_rslt_type=SchemaContextValidationException.MTHD_RSLT,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(context)
        
        # Handle the case that, there is no validation logic for the attribute.
        return ValidationResult.failure(
            SchemaContextValidationException(
                cls_mthd=method,
                cls_name=cls.__name__,
                op=SchemaContextValidationException.OP,
                msg=SchemaContextValidationException.MSG,
                err_code=SchemaContextValidationException.ERR_CODE,
                mthd_rslt_type=SchemaContextValidationException.MTHD_RSLT,
                ex=SchemaContextValidationRouteException(
                    msg=SchemaContextValidationRouteException.MSG,
                    err_code=SchemaContextValidationRouteException.ERR_CODE,
                )
            )
        )
        
    
