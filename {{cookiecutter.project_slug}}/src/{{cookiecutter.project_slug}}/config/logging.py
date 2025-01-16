import logging

def reset_logger(logger: logging.Logger) -> None:
    logger.setLevel(logging.NOTSET)
    logger.propagate = True
    logger.disabled = False
    logger.filters.clear()
    handlers = logger.handlers.copy()
    for handler in handlers:
        print(handler)
        handler.acquire()
        handler.flush()
        handler.close()
        handler.release()
        logger.removeHandler(handler)


def configure_logger(logger: logging.Logger):
    reset_logger(logger)
    handler = logging.StreamHandler()
    # Console level is configurable
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
