if __name__ == "__main__":
    import logging
    from module_logging import test_logging, gen_custom_logger, test_custom_logger

    # test_logging(
    #     filename=None,
    #     filemode=None,
    #     level=logging.INFO
    # )

    logger = gen_custom_logger(filename="custom.log", filemode="a")
    test_custom_logger(logger)