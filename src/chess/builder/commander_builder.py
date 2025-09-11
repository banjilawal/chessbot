from enum import Enum

from chess.common import Result
from chess.common.emit import IdEmitter
from chess.builder import CommanderBuilderException

from chess.commander import (
    Commander, HumanCommander, CyberneticCommander,
    CommanderType, CommanderValidator, CommanderValidationException
)



class CommanderBuilder(Enum):

    @staticmethod
    def build(
        commander_id: int = IdEmitter.person_id,
        name: str = "Commander",
        commander_type: CommanderType = CommanderType.HUMAN
    ) -> Result[Commander]:
        method = "CommanderBuilder.build"

        try:
            if CommanderType not in [CommanderType.HUMAN, CommanderType.CYBERNAUT]:
                raise CommanderBuilderException(f"{method}: {CommanderBuilderException.DEFAULT_MESSAGE}")

            candidate = None

            if commander_type == CommanderType.HUMAN:
                candidate = HumanCommander(competitor_id=commander_id, name=name)

            if commander_type == CommanderType.CYBERNAUT:
                candidate = CyberneticCommander(commander_id=commander_id, name=name)


            validation = CommanderValidator.validate(candidate)

            ThrowHelper.throw_if_invalid(CommanderBuilder, validation)
            return validation
        except Exception as e:
            return Result(payload=None, exception=e)


def main():
    build_result = CommanderBuilder.build(commander_id=id_emitter.person_id, name=RandomName.person())
    if build_result.is_success():
        competitor = build_result.payload
        print(f"Successfully built competitor: {competitor}")
    else:
        print(f"Failed to build competitor: {build_result.exception}")

    build_result = CommanderBuilder.build(-1, 4)
    if build_result.is_success():
        competitor = build_result.payload
        print(f"Successfully built competitor: {competitor}")
    else:
        print(f"Failed to build competitor: {build_result.exception}")

if __name__ == "__main__":
    main()