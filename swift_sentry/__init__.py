import logging
from sentry_sdk import init
from sentry_sdk.integrations.logging import EventHandler, ignore_logger


def sentry_logger(conf, name, log_to_console, log_route, fmt, logger, adapted_logger):
    sentry_dsn = conf.get("sentry_dsn", None)
    sentry_ignore_loggers = conf.get("sentry_ignore_loggers", None)
    sentry_log_level = getattr(
        logging, conf.get("sentry_log_level", "ERROR").upper(), logging.ERROR
    )

    if sentry_dsn:
        sentry_handler = EventHandler()
        sentry_handler.setLevel(sentry_log_level)
        logger.addHandler(sentry_handler)

        if sentry_ignore_loggers:
            ignore_loggers_list = [
                s.strip() for s in sentry_ignore_loggers.split(",") if s.strip()
            ]
            for lgr in ignore_loggers_list:
                ignore_logger(lgr)

        init(sentry_dsn)
