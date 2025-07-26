from chess.config.rank_config import RankConfig


class RankFactory:

    @staticmethod
    def build(self):
        for config in RankConfig:
            print(config.value, "\n")

def main ():
    RankFactory.build()

if __name__ == "__main__":
    main()