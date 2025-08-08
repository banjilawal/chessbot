from config.logging_setup import init_logging



def main():
    """Your exact requested structure"""
    logger = init_logging()  # Explicit logging start

    try:
        logger.info("Starting arena initialization")
        # arena = build_game()
        # launch_game(arena)

    except Exception as e:
        logger.critical(f"Match failed: {e}", exc_info=True)
        raise
    finally:
        logger.info("Match session ended")



if __name__ == "__main__":
    main()  # Clean entry point