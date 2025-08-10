from chess.config.team_config import TeamConfig
from chess.creator.emit import id_emitter
from chess.creator.entity.builder.team_builder import TeamBuilder
from chess.owner.human_owner import HumanOwner
from chess.owner.owner import Owner


class OwnerBuilder:

    @staticmethod
    def build() -> Owner:
        return HumanOwner(
            owner_id=id_emitter.owner_id,
            name="Human",
            team=TeamBuilder.build(TeamConfig.WHITE)
        )

def main():
    owner = OwnerBuilder.build()
    print(owner)

if __name__ == "__main__":
    main()