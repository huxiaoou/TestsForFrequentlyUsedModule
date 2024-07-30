import sys
import logging
import rich.logging as rlog
from loguru import logger as rlogger


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


def get_rich_logger() -> logging.Logger:
    formatter = logging.Formatter(
        fmt="[%(levelname)-8s][%(asctime)s.%(msecs)03d] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    rich_handler = rlog.RichHandler(
        show_time=True, show_level=True, show_path=False,
        markup=True,
        # log_time_format="%Y-%m-%d %H:%M:%S.%f"
    )
    rich_handler.setFormatter(formatter)

    logger = logging.getLogger('huxo.richlog')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(rich_handler)

    return logger


def test_rich_logger(logger: logging.Logger) -> None:
    logger.debug("This is log for [red]DEBUG[/red] aaa")
    logger.info("This is log for [yellow]INFO bbb")
    logger.warning("This is log for [green]WARNING[/green] ccc")
    logger.error("This is log for [blue]ERROR[/blue] ddd")
    logger.critical("This is log for [cyan]CRITICAL[/cyan] eee")

    a = "abc"
    try:
        int(a)
    except ValueError as e:
        # logger.error(e)
        logger.exception(e)


class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    # format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    format = "[%(levelname)-8s][%(asctime)s.%(msecs)03d] %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record: logging.LogRecord):
        log_fmt = self.FORMATS.get(record.levelno)
        # self._fmt = log_fmt
        # return super().format(record)

        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)


def get_custom_colorful_logger() -> logging.Logger:
    logger = logging.getLogger("myColorfulApp")
    logger.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    ch.setFormatter(CustomFormatter(datefmt="%Y-%m-%d %H:%M:%S"))

    logger.addHandler(ch)
    return logger


def test_for_loguru() -> None:
    rlogger.remove(0)
    fmt_datetime = "[<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>]"
    fmt_level = "[<level>{level:<8}</level>]"
    fmt_name = "<cyan>{name}</cyan>"
    fmt_func = "<cyan>{function}</cyan>"
    fmt_line = "<cyan>{line}</cyan>"
    fmt_location = f"[{fmt_name}:{fmt_func}:{fmt_line}]"
    # fmt_msg = "[<level>{message}</level>]"
    fmt_msg = "[{message}]"

    rlogger.add(
        sys.stdout,
        level="TRACE",
        format=fmt_datetime + fmt_level + fmt_location + fmt_msg,
    )

    rlogger.trace("Executing program")
    rlogger.debug("Processing data...")
    rlogger.info("Server started successfully.")
    rlogger.success("Data processing completed successfully.")
    rlogger.warning("Invalid configuration detected.")
    rlogger.error("Failed to connect to the database.")
    rlogger.critical("Unexpected system error occurred. Shutting down.")
