import logging


# Django logger standart
logging.basicConfig(level=logging.DEBUG,
                    filename="server_routines/logs/django.log",
                    format="%(name)s %(asctime)s %(levelname)s: %(message)s")

# Set debug logs
debug_logger = logging.getLogger('debug')
debug_logger.setLevel(logging.DEBUG)

debug_fh = logging.FileHandler('server_routines/logs/debug.log')
debug_fh.setLevel(logging.DEBUG)
debug_formatter = logging.Formatter(
    '%(asctime)s %(message)s'
)
debug_fh.setFormatter(debug_formatter)

debug_logger.addHandler(debug_fh)

# Set standart info logs
origin = logging.getLogger('mistakes')
origin.setLevel(logging.INFO)

origin_fh = logging.FileHandler('server_routines/logs/all.log')
origin_fh.setLevel(logging.INFO)
origin_formatter = logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s'
)
origin_fh.setFormatter(origin_formatter)

origin.addHandler(origin_fh)


def slog(msg: str, level: str = 'i'):
    '''
        Standart logger:
        msg - message of log
        level - level of log
            i: info (by default)
            w: warning
            e: error
            c: critical
    '''
    if level == 'i':
        origin.info(msg)
    elif level == 'c':
        origin.critical(msg)
    elif level == 'e':
        origin.error(msg)
    else:
        origin.warning(msg)


def debug_log(msg: str):
    debug_logger.debug(msg)
