import logging


def test_logging(filename: str | None, filemode: str | None, level: int = logging.INFO) -> None:
    logging.basicConfig(
        filename=filename,
        filemode=filemode,
        level=level,
        format="[%(levelname)8s][%(asctime)s.%(msecs)03d] %(message)s",
        datefmt="%Y%m%d %H:%M:%S"
    )

    logging.debug("This is log for DEBUG")
    logging.info("This is log for INFO")
    logging.warning("This is log for WARNING")
    logging.error("This is log for ERROR")
    logging.critical("This is log for CRITICAL")
