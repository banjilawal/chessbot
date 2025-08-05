from config.logging_setup import init_logging



def main():
    """Your exact requested structure"""
    logger = init_logging()  # Explicit logging start

    try:
        logger.info("Starting field initialization")
        # field = build_game()
        # launch_game(field)

    except Exception as e:
        logger.critical(f"Game failed: {e}", exc_info=True)
        raise
    finally:
        logger.info("Game session ended")



if __name__ == "__main__":
    main()  # Clean entry point