from enum import Enum
from typing import Optional

from assurance import ThrowHelper
from chess.system import BuildResult, IdValidator, NameValidator

from chess.commander import Commander, Human, Bot, CommanderBuildFailedException
from chess.engine import DecisionEngine


class CommanderBuilder(Enum):
    """
    Builder class responsible for safely constructing `Commander` instances.
    
    `CommanderBuilder` ensures that `Commander` objects are always created successfully by performing comprehensive validate
    checks during construction. This separates the responsibility of building from validating `CommanderBuilder` focuses on
    creating while `CommanderValidator` is used for validating existing `Commander` instances that are passed around the system.
    
    The build runs through all validate checks individually to guarantee that any `Commander` instance it produces meets
    all required specifications before construction completes.

    `Commander` is an abstract class. `CommanderBuilder` instantiates either `Human` or `Bot` objects.
    
    Usage:
        ```python
        from typing import cast
        from chess.commander Bot, Human, CommanderBuilder

        # Safe creation of a human commander
        build_outcome = CommanderBuilder.build(commander=id_emitter.human_id, name="Tunji")
        if not build_outcome.is_success():
            raise build_outcome.err
        person = cast(Human, build_outcome.payload) # <-- Always cast to the concrete type of the commander

        # Safe creation of an automated commander. An automated commander must be given an engine for deciding
        # how to play
        from chess.engine GreedyDecisionEngine,
        greedy_decision_engine = GreedyDecisionEngine()

        build_outcome = CommanderBuilder(commander=id_emitter.bot_id, name="cyb-a73", engine=greedy_decision_engine)
        if not build_outcome.is_success():
            raise build_outcome.err
        cybernaut = cast(Bot, build_outcome.payload)
        ```
    
    See Also:
        `Commander`: Fundamental data structure for representing commanderinates on a chessboard.
        `CommanderValidator`: Used for validating existing `Commander` instances
        `BuildResult`: Return type containing the built `Commander` or err information
    """
    
    @staticmethod
    def build( name: str,  engine: Optional[DecisionEngine] = None) -> BuildResult[Commander]:
        """
        Constructs a new `Commander` instance with comprehensive checks on the parameters and states during the
        build process.

        Performs individual validate checks on each component to ensure the resulting `Commander` meets all
        specifications. If all checks are passed, a `Commander` instance will be returned. It is not necessary to perform
        any additional validate checks on the returned `Commander` instance. This method guarantees if a `BuildResult`
        with a successful status is returned, the contained `Commander` is valid and ready for use.

        By default, `CommanderBuilder` will create a `Human` instance. If an `engine` is provided, a `Bot`
        instance will be created. `CommanderBuilder.build` returns a `Commander` instance that needs casting to either
        a `Human` or `Bot` class before use.

        Args:
            `commander_id` (int): The unique id for the commander. Must pass `IdValidator` checks.
            `name` (`Name`): Must pass `NameValidator` checks.
            `engine` (DecisionEngine): The engine used to determine how to play.`

        Returns:
            BuildResult[Commander]: A `BuildResult` containing either:
                - On success: A valid `Commander` instance in the payload
                - On failure: Error information and err details

        Raises:
            `CommanderBuildFailedException`: Wraps any underlying validate failures that occur during the construction process.
            This includes:
                * `InvalidIdException`: if `commander_id` fails validate checks.
                * `InvalidNameException`: if `name` fails validate checks.
                * `EngineValidationException`: If `engine` is not null and fails validate checks.

        Note:
            The build runs through all the checks on parameters and state to guarantee only a valid `Commander` is
            created, while `CommanderValidator` is used for validating `Commander` instances that are passed around after
            creation. This separation of concerns makes the validate and building independent of each other and
            simplifies maintenance.

        Example:
            ```python
            from typing import cast
            from chess.commander import Human, CommanderBuilder

            build_outcome = CommanderBuilder.build(commander_id=1, name="Richard")
            
            if not build_outcome.is_success():
                raise build_outcome.err # <--- Skips this because id and name are valid.

            person = cast(HUman, build_outcome.payload) # <-- executes this line
            ```
        """
        method = "CommanderBuilder.build"

        try:
            # id_validation = IdValidator.validate(commander_id)
            # if not id_validation.is_success():
            #     InstructionRecorder.throw_if_invalid(CommanderBuilder, id_validation.err)


            name_validation = NameValidator.validate(name)
            if not name_validation.is_success():
                ThrowHelper.throw_if_invalid(CommanderBuilder, name_validation.exception)
                raise name_validation.exception

            if engine is not None and not isinstance(engine, DecisionEngine):
                error  = TypeError(f"Expected a Decision, but got {type(engine).__name__}.")
                ThrowHelper.throw_if_invalid(CommanderBuilder, error)
                raise error

            if engine is not None and isinstance(engine, DecisionEngine):
                return BuildResult(payload=Bot( name=name, engine=engine))

            # If no engine is provided and all the checks are passed, a Human commander is returned
            return BuildResult(payload=Human(name=name))

        except (
            TypeError,
            InvalidNameException
        ) as e:
            raise (f"{method}: {e}") from e


            except Exception as e:
            raise AttackEventBuilderException(
                f"{method}: Unexpected err ({type(e).__name__}): {e}" ) from e
#
#
# def main():
#     build_result = CommanderBuilder.build(commander_id=id_emitter.person_id, name=RandomName.person())
#     if build_result.is_success():
#         competitor = build_result.payload
#         print(f"Successfully built competitor: {competitor}")
#     else:
#         print(f"Failed to build competitor: {build_result.err}")
#
#     build_result = CommanderBuilder.build(-1, 4)
#     if build_result.is_success():
#         competitor = build_result.payload
#         print(f"Successfully built competitor: {competitor}")
#     else:
#         print(f"Failed to build competitor: {build_result.err}")
#
# if __name__ == "__main__":
#     main()