from chess.config.rank_config import RankConfig


class RankFactory:

    @staticmethod
    def build():
        for config in RankConfig:
            print(config)
            # print(f"{config.name}, {config.value}, {config.symbol}, {config.capture_value}")

def main ():
    RankFactory.build()

if __name__ == "__main__":
    main()