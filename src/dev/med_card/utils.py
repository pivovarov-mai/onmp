from datetime import datetime

from config.utils import execute_sql_dict
from config.loggers_conf import slog, debug_log

from dbsetter.requests_other import (
    CREATE_NEW_CARD,
    READ_CARD,
    DELETE_CARD,
    UPDATE_CARD,
    SHOW_ALL_CARDS,
)


CARD_NULL_FIELDS = {'comment'}


def peeler(data):
    description = [descr.name for descr in data[1]]
    result = [dict(zip(description, item)) for item in data[0]]
    return result


def card_create(params: dict[str, any]):
    try:
        params.setdefault('comment')
        params.setdefault('status', 'draft')
        params.setdefault('date', datetime.now().strftime('%Y-%m-%d'))

        id = peeler(execute_sql_dict(
            CREATE_NEW_CARD,
            params)
        )

        debug_log(id)

        return id
    except KeyError as e:
        slog('Create card keyerror: ' + str(e), 'e')
        return 'Не хватает параметра: ' + str(e)
    except Exception as e:
        slog('Create card error: ' + str(e), 'e')
        return 'Неизвестная ошибка, смотри логи'


def show_all_cards(account_user_id):
    try:
        debug_log(account_user_id)
        r = execute_sql_dict(
            SHOW_ALL_CARDS,
            {'account_user_id': account_user_id}
        )
        slog(peeler(r))
        return peeler(r)
    except KeyError as e:
        slog('Show cards error: ' + str(e), 'e')
        return str(e)
    except Exception as e:
        slog('Show cards error: ' + str(e), 'e')
        return 'Неизвестная ошибка, смотри логи'


def retrieve_card(id):
    card = peeler(
        execute_sql_dict(READ_CARD, {'id': id})
    )
    if len(card) > 0:
        return card[0]
    return None


def update_card(params: dict[str, any]):
    execute_sql_dict(UPDATE_CARD, params)


def delete_card(id):
    execute_sql_dict(DELETE_CARD, {'id': id})
