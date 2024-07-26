import logging


def test_logging(filename: str | None, filemode: str | None, level: int = logging.INFO) -> None:
    logging.basicConfig(
        filename=filename,
        filemode=filemode,
        level=level,
        format="[%(levelname)-8s][%(asctime)s.%(msecs)03d] %(message)s",
        datefmt="%Y%m%d %H:%M:%S"
    )

    logging.debug("This is log for DEBUG")
    logging.info("This is log for INFO")
    logging.warning("This is log for WARNING")
    logging.error("This is log for ERROR")
    logging.critical("This is log for CRITICAL")


def gen_custom_logger(filename: str | None, filemode: str | None) -> logging.Logger:
    # logger = logging.getLogger()
    # print(logger)

    logger = logging.getLogger('huxo.applog')
    # this overwrites handlers' level
    # if this level is too high, then handlers' level won't work
    # set logger's level to be lowest, a.k.a, logging.DEBUG, then handlers' level settings won't be affected
    logger.setLevel(logging.DEBUG)
    print(logger)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(filename=filename, mode=filemode)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="[%(levelname)-8s][%(asctime)s.%(msecs)03d] %(message)s",
        datefmt="%Y%m%d %H:%M:%S",
    )

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    flt = logging.Filter("huxo")  # can be added to handler
    logger.addFilter(flt)  # logger will work only when logger.name start with "huxo"

    return logger


def test_custom_logger(logger: logging.Logger) -> None:
    logger.debug("This is log for DEBUG")
    logger.info("This is log for INFO")
    logger.warning("This is log for WARNING")
    logger.error("This is log for ERROR")
    logger.critical("This is log for CRITICAL")

    a = "abc"
    try:
        int(a)
    except ValueError as e:
        # logger.error(e)
        logger.exception(e)
