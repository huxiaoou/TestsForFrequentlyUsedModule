import logging


def test_logging() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
    )

    logging.debug("This is log for DEBUG")
    logging.info("This is log for INFO")
    logging.warning("This is log for WARNING")
    logging.error("This is log for ERROR")
    logging.critical("This is log for CRITICAL")
