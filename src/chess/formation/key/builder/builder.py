# src/chess/formation/builder/builder.py

"""
Module: chess.formation.lookup/map.builder.builder
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional

from chess.formation import (
    FormationContext, FormationContextBuildFailedException, NoFormationContextFlagException, ExcessiveFormationContextFlagsException
)
from chess.system import (
    BuildResult, Builder, UnhandledRouteException, GameColor, GameColorValidator,
    IdentityService, LoggingLevelRouter
)


class FormationContextBuilder(Builder[FormationContext]):
    """
    # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce FormationContext instances whose integrity is guaranteed at creation.
    2.  Manage construction of FormationContext instances that can be used safely by the client.
    3.  Ensure params for FormationContext creation have met the application's safety contract.
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
            name: Optional[str] = None,
            square: Optional[str] = None,
            color: Optional[GameColor] = None,
            designation: Optional[str] = None,
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> BuildResult[FormationContext]:
        """
        # Action:
            1.  Confirm that only one in the (square_name, color, name, designation) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a FormationContext and send in a BuildResult. Else, return an exception
                in the BuildResult.

        # Parameters:
            Only one these must be provided:
                *   name (Optional[str])
                *   square_name (Optional[str])
                *   designation (Optional[str])
                *   color (Optional[GameColor])
    
            These Parameters must be provided:
                *   color_validator (GameColorValidator)
                *   identity_service (IdentityService)

        # Returns:
        BuildResult[FormationContext] containing either:
            - On success: FormationContext in the payload.
            - On failure: Exception.

        # Raises:
            *   ZeroFormationContextFlagsException
            *   FormationContextBuildFailedException
            *   ExcessiveFormationContextFlagsException
        """
        method = "FormationContextBuilder.build"
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
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [designation, square, color]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to look up a piece's battle_order.
            if param_count == 0:
                return BuildResult.failure(
                    NoFormationContextFlagException(f"{method}: {NoFormationContextFlagException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveFormationContextFlagsException(f"{method}: {ExcessiveFormationContextFlagsException}")
                )
            # After verifying only one Formation attribute-value-tuple is enabled, validate it.
            
            # Build the name FormationContext if its flag is enabled.
            if name is not None:
                validation = identity_service.validate_name(candidate=name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a designation_FormationContext in the BuildResult.
                return BuildResult.success(FormationContext(name=name))
            
            # Build the designation FormationContext if its flag is enabled.
            if designation is not None:
                validation = identity_service.validate_name(candidate=designation)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a designation_FormationContext in the BuildResult.
                return BuildResult.success(FormationContext(designation=designation))
            
            # Build the square_name FormationContext if its flag is enabled.
            if square is not None:
                validation = identity_service.validate_name(candidate=square)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a square_FormationContext in the BuildResult.
                return BuildResult.success(FormationContext(square=square))
            
            # Build the color FormationContext if its flag is enabled.
            if color is not None:
                validation = color_validator.validate(candidate=GameColor)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a color_FormationContext in the BuildResult.
                return BuildResult.success(FormationContext(color=color))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
            BuildResult.failure(
                UnhandledRouteException(f"{method}: {UnhandledRouteException.DEFAULT_MESSAGE}")
            )
        # Finally, catch any missed exception, wrap an FormationContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                FormationContextBuildFailedException(
                    ex=ex, message=f"{method}: {FormationContextBuildFailedException.DEFAULT_MESSAGE}"
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
                    ex=TypeError(f"{method} Expected a Schema, got {type(candidate).__name__} instead.")
                )
            )
        # On certification success return the schema instance in a ValidationResult.
        return ValidationResult.success(payload=cast(Schema, candidate))
