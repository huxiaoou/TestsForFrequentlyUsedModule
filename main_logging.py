if __name__ == "__main__":
    import logging
    from module_logging import test_logging, gen_custom_logger, test_custom_logger
    from module_logging import get_rich_logger, test_rich_logger
    from module_logging import get_custom_colorful_logger
    from module_logging import test_for_loguru

    # test_logging(
    #     filename=None,
    #     filemode=None,
    #     level=logging.INFO
    # )

    logger = gen_custom_logger(filename="custom.log", filemode="a")
    test_custom_logger(logger)

    rich_logger = get_rich_logger()
    test_rich_logger(rich_logger)

    logger = get_custom_colorful_logger()
    test_custom_logger(logger)

    test_for_loguru()