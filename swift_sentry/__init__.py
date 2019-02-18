# -*- coding: utf-8 -*-
from sentry_sdk import init
from sentry_sdk.integrations.logging import ignore_logger


# init initializes the Sentry SDK with the default integrations (logging,
# etc.). Data is captured automatically from within the application's runtime.
init()


def sentry_logger(conf, name, log_to_console, log_route, fmt, logger, adapted_logger):
    """
    sentry_logger sets up a custom log handler hook for Swift. Its parameters
    are the same as Swift’s get_logger function (as well as the getLogger and
    LogAdapter object).

    The log handler hook is essenitially a no-op, it is called in order to
    initialise Sentry using the init() at the module level.

    We could, of course, set things up by manually adding the Handlers to the
    specific logger (as stated in the Swift docs) but that would result in code
    duplication from the SDK.
    This approach is better since it allows Sentry to capture all events
    instead of just capturing the events from the loggers that Swift gives us
    control over.
    """

    sentry_ignore_loggers = conf.get("sentry_ignore_loggers", None)
    if sentry_ignore_loggers:
        ignore_loggers_list = [
            s.strip() for s in sentry_ignore_loggers.split(",") if s.strip()
        ]
        for lgr in ignore_loggers_list:
            ignore_logger(lgr)
