from enum import Enum

from assurance import ThrowHelper
from chess.common import BuildResult, IdValidator, NameValidator


from chess.commander import Commander, Human, Bot, CommanderBuilderException
from chess.engine import DecisionEngine


class CommanderBuilder(Enum):

    @staticmethod
    def build(
        commander_id: int,
        name: str, 
        engine: DecisionEngine = None
    ) -> BuildResult[Commander]:
        method = "CommanderBuilder.build"

        try:
            id_validation = IdValidator.validate(commander_id)
            if not id_validation.is_success():
                ThrowHelper.throw_if_invalid(CommanderBuilder, id_validation.exception)

            name_validation = NameValidator.validate(name)
            if not name_validation.is_success():
                ThrowHelper.throw_if_invalid(CommanderBuilder, name_validation.exception)

            if engine is not None and not isinstance(engine, DecisionEngine):
                ThrowHelper.throw_if_invalid(
                    CommanderBuilder,
                    TypeError(f"Expected a Decision, but got {type(engine).__name__}.")
                )

            if engine is not None and isinstance(engine, DecisionEngine):
                return BuildResult(
                    payload=Bot(
                        commander_id=commander_id,
                        name=name,
                        engine=engine
                    )
                )

            if engine is None:
                return BuildResult(
                    payload=Human(competitor_id=commander_id, name=name)
                )


        except Exception as e:
            return BuildResult(payload=None, exception=e)
#
#
# def main():
#     build_result = CommanderBuilder.build(commander_id=id_emitter.person_id, name=RandomName.person())
#     if build_result.is_success():
#         competitor = build_result.payload
#         print(f"Successfully built competitor: {competitor}")
#     else:
#         print(f"Failed to build competitor: {build_result.exception}")
#
#     build_result = CommanderBuilder.build(-1, 4)
#     if build_result.is_success():
#         competitor = build_result.payload
#         print(f"Successfully built competitor: {competitor}")
#     else:
#         print(f"Failed to build competitor: {build_result.exception}")
#
# if __name__ == "__main__":
#     main()