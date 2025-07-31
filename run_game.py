from config.logging_setup import init_logging



def main():
    """Your exact requested structure"""
    logger = init_logging()  # Explicit logging start

    try:
        logger.info("Starting game initialization")
        # game = build_game()
        # launch_game(game)

    except Exception as e:
        logger.critical(f"Game failed: {e}", exc_info=True)
        raise
    finally:
        logger.info("Game session ended")



if __name__ == "__main__":
    main()  # Clean entry point