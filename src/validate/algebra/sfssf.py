
entity = cast(Union[Vector, Coord], candidate)
# Handle the case that, the entity is an unsafe vector.

    # Handle the case that, the entity is an unsafe coord.

    # --- Forward the work product to the caller. ---#
    return ValidationResult.success(entity)

"""

"""


@classmethod
@LoggingLevelRouter.monitor
def validate(

) -> ValidationResult[Union[Vector, Coord]:
                      
                      method =