# src/chess/formation/key/builder/builder.py

"""
Module: chess.formation.key.builder.builder
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional

from chess.formation import FormationSuperKey
from chess.formation.key.builder.exception.route import FormationSuperKeyBuildRouteException
from chess.formation.key.builder.exception.wrapper import FormationSuperKeyBuildFailedException
from chess.formation.key.validator.exception.debug.excess import ZeroFormationSuperKeysException
from chess.system import BuildResult, Builder, GameColor, GameColorValidator, IdentityService, LoggingLevelRouter


class FormationSuperKeyBuilder(Builder[FormationSuperKey]):
    """
    # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce FormationSuperKey instances whose integrity is guaranteed at creation.
    2.  Manage construction of FormationSuperKey instances that can be used safely by the client.
    3.  Ensure params for FormationSuperKey creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

    # PARENT:
        *   Builder

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            designation: Optional[str] = None,
            square: Optional[str] = None,
            color: Optional[GameColor] = None,
            designation: Optional[str] = None,
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> BuildResult[FormationSuperKey]:
        """
        # Action:
            1.  Confirm that only one in the (square_designation, color, designation, designation) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a FormationSuperKey and send in a BuildResult. Else, return an exception
                in the BuildResult.

        # Parameters:
            Only one these must be provided:
                *   designation (Optional[str])
                *   square_designation (Optional[str])
                *   designation (Optional[str])
                *   color (Optional[GameColor])
    
            These Parameters must be provided:
                *   color_validator (GameColorValidator)
                *   identity_service (IdentityService)

        # Returns:
        BuildResult[FormationSuperKey] containing either:
            - On success: FormationSuperKey in the payload.
            - On failure: Exception.

        # Raises:
            *   ZeroFormationSuperKeyFlagsException
            *   FormationSuperKeyBuildFailedException
            *   ExcessiveFormationSuperKeyFlagsException
        """
        method = "FormationSuperKeyBuilder.build"
        """
        # ACTION:.
            1.  If the candidate passes existence and type checks cast into a Schema instance and return
                in the ValidationResult. Else return an exception in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
        # RETURNS:
            *   ValidationResult[Schema] containing either:
                    - On failure: Exception.
                    - On success: Schema in the payload.
        # RAISES:
            *   TypeError
            *   NullSchemaException
            *   InvalidSchemaException
        """
        # Count how many optional parameters are not-null. One param needs to be not-null.
        params = [designation, square, color]
        param_count = sum(bool(p) for p in params)
        
        # Test if no params are set. Need an attribute-value pair to look up a piece's battle_order.
        if param_count == 0:
            return BuildResult.failure(
                FormationSuperKeyBuildFailedException(
                    message=f"{method}: {FormationSuperKeyBuildFailedException.ERROR_CODE}",
                    ex=ZeroFormationSuperKeysExceptionn(
                        f"{method}: {ZeroFormationSuperKeysExceptionn.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
        if param_count > 1:
            return BuildResult.failure(
                FormationSuperKeyBuildFailedException(
                    message=f"{method}: {FormationSuperKeyBuildFailedException.ERROR_CODE}",
                    ExcessiveFormationSuperKeyFlagsException(f"{method}: {ExcessiveFormationSuperKeyFlagsException}")
                )
            )
        # After verifying only one Formation attribute-value-tuple is enabled, validate it.
        
        # Build the designation FormationSuperKey if its flag is enabled.
        if designation is not None:
            validation = identity_service.validate_name(candidate=designation)
            if validation.is_failure:
                return BuildResult.failure(
                    FormationSuperKeyBuildFailedException(
                        ex=validation.exception,
                        message=f"{method}: {FormationSuperKeyBuildFailedException.ERROR_CODE}"
                    )
                )
            # On validation success return a designation_FormationSuperKey in the BuildResult.
            return BuildResult.success(FormationSuperKey(designation=designation))
        
        # Build the square_designation FormationSuperKey if its flag is enabled.
        if square is not None:
            validation = identity_service.validate_name(candidate=square)
            if validation.is_failure:
                return BuildResult.failure(
                    FormationSuperKeyBuildFailedException(
                        ex=validation.exception,
                        message=f"{method}: {FormationSuperKeyBuildFailedException.ERROR_CODE}"
                    )
                )
            # On validation success return a square_FormationSuperKey in the BuildResult.
            return BuildResult.success(FormationSuperKey(square=square))
        
        # Build the color FormationSuperKey if its flag is enabled.
        if color is not None:
            validation = color_validator.validate(candidate=GameColor)
            if validation.is_failure:
                return BuildResult.failure(
                    FormationSuperKeyBuildFailedException(
                        ex=validation.exception,
                        message=f"{method}: {FormationSuperKeyBuildFailedException.ERROR_CODE}"
                    )
                )
            # On validation success return a color_FormationSuperKey in the BuildResult.
            return BuildResult.success(FormationSuperKey(color=color))
        
        # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
        BuildResult.failure(
            FormationSuperKeyBuildFailedException(
                message=f"{method}: {FormationSuperKeyBuildFailedException.ERROR_CODE}",
                ex=FormationSuperKeyBuildRouteException(
                    f"{method}: {FormationSuperKeyBuildRouteException.DEFAULT_MESSAGE}"
                )
            )
        )
  
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Schema]:
        """
        # ACTION:.
            1.  If the candidate passes existence and type checks cast into a Schema instance and return
                in the ValidationResult. Else return an exception in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
        # RETURNS:
            *   ValidationResult[Schema] containing either:
                    - On failure: Exception.
                    - On success: Schema in the payload.
        # RAISES:
            *   TypeError
            *   NullSchemaException
            *   InvalidSchemaException
        """
        method = "SchemaValidator.validate"
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                InvalidSchemaException(
                    message=f"{method}: {InvalidSchemaException.ERROR_CODE}",
                    ex=NullSchemaException(f"{method} {NullSchemaException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Schema):
            # Return the exception chain on failure
            return ValidationResult.failure(
                InvalidSchemaException(
                    message=f"{method}: {InvalidSchemaException.ERROR_CODE}",
                    ex=TypeError(f"{method} Expected a Schema instance, got {type(candidate).__designation__} instead.")
                )
            )
        # On certification success return the schema instance in a ValidationResult.
        return ValidationResult.success(payload=cast(Schema, candidate))
