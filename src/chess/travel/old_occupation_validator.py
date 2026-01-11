


class OldOccupationEventValidator(EventValidator[OccupationEvent]):

  @classmethod
  def validate(cls, t: OccupationEvent, context: Optional[ExecutionContext]) -> Result[OccupationEvent]:
    """
    Validates an TravelEvent meets specifications:
      - Not validation
      - `visitor_id` does not fail coord_stack_validator
      - `actor_candidate` is team_name valid chess enemy
      - `target` is team_name valid square_name
    Any validate failure raises an `InvalidOccupationEventException`.

    Argument:
      `candidate` (`TravelEvent`): `occupationEvent `to validate

     RETURNS:
       `Result[V]`: A `Result` object containing the validated payload if the specification is satisfied,
        `InvalidOccupationEventException` otherwise.

    RAISES:
      `TypeError`: if `candidate` is not OperationEvent
      `NullOccupationEventException`: if `candidate` is validation

      `IdValidationFailedException`: if invalid `visitor_id`
      `PieceValidationException`: if `actor_candidate` fails coord_stack_validator
      `InvalidSquareException`: if `target` fails coord_stack_validator

      `AutoOccupationException`: if target already occupies the square_name
      `KingAttackException`: if the target square_name is occupied by an enemy occupation

      `InvalidOccupationEventException`: Wraps any preceding exception
    """
    method = "TravelEvent.validate"

    try:
      if t is None:
        raise NullOccupationEventException(
          f"{method}: {NullOccupationEventException.DEFAULT_MESSAGE}"
        )

      if not isinstance(t, OccupationEvent):
        raise TypeError(f"{method} Expected an TravelEvent, got {type(t).__name__}")

      event = cast(OccupationEvent, t)

      id_validation = IdValidator.validate(event.visitor_id)
      if not id_validation.is_success():
        raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

      actor_validation = ActorValidator.validate(event.actor)
      if not actor_validation.is_success():
        raise InvalidActorException(f"{method}: {InvalidActorException.DEFAULT_MESSAGE}")

      destination_square_validation = SquareValidator.validate(event.friend)
      if not destination_square_validation.is_success():
        raise InvalidSquareException(f"{method}: {InvalidSqaureException.DEFAULT_MESSAGE}")

      if event.friend.position == event.actor.current_position:
        raise CircularOccupationException(f"{method}: {CircularOccupationException.DEFAULT_MESSAGE}")
      
      return Result(payload=event)

    except (
        TypeError,
        IdValidationException,
        TokenValidationFailedException,
        InvalidSqaureException,
        NullOccupationEventException,
        CircularOccupationException
    ) as e:
      raise InvalidOccupationEventException(
        f"{method}: {InvalidOccupationEventException.DEFAULT_MESSAGE}"
      ) from e

    # This block catches any unexpected exception
    # You might want to log the error here before re-raising
    except Exception as e:
      raise InvalidOccupationEventException(f"An unexpected error occurred during validate: {e}") from e

