from config.utils import (
    execute_sql_dict,
    peeler,
)

from config.loggers_conf import slog

from dbsetter.requests_other import (
    READ_USER_PROFILE,
    UPDATE_USER_PROFILE,
    SHOW_ALL_USER_PROFILE,
    DELETE_USER_PROFILE,
    CREATE_NEW_USER_PROFILE,
)


USER_PROFILE_NULL_FIELDS = {'date_of_birth',
                            'phone_number',
                            'passport'}

USER_PROFILE_FIELDS = {'last_name', 'first_name',
                       'middle_name', 'date_of_birth',
                       'phone_number', 'passport',
                       'account_user_id', 'id'}


def user_profile_merge_fields(data, origin={}, fill_none=False):
    result = origin

    if fill_none is True:
        for field in USER_PROFILE_NULL_FIELDS:
            if field not in result:
                result[field] = None

    for [k, v] in data.items():
        if k in USER_PROFILE_FIELDS:
            result[k] = v

    return result


def user_profile_retrieve(params: dict[str, any]):
    '''
        Returns profile info

        Requires account_user_id
    '''
    try:
        return peeler(
                    execute_sql_dict(
                        READ_USER_PROFILE,
                        {'account_user_id': params['account_user_id']}
                    )
                )
    except KeyError as e:
        return 'Ключ ' + str(e) + ' необходим'
    except Exception as e:
        slog(str(e), 'e')
        return 'Возникла странная ошибка, пускай админ проверит логи'


def user_profile_update(params: dict[str, any]):
    try:
        current_user = user_profile_retrieve({
                'account_user_id': params['account_user_id']
            })[0]

        merged_data = user_profile_merge_fields(params, current_user)

        execute_sql_dict(
            UPDATE_USER_PROFILE,
            merged_data
        )
        return 'Данные обновлены'
    except KeyError as e:
        return 'Ключ ' + str(e) + ' необходим'
    except Exception as e:
        slog(str(e), 'e')
        return 'Возникла странная ошибка, пускай админ проверит логи'


def user_profile_create(params: dict[str, any]):
    try:
        validated_data = user_profile_merge_fields(params, {}, True)

        return peeler(execute_sql_dict(
            CREATE_NEW_USER_PROFILE,
            validated_data)
        )
    except KeyError as e:
        return 'Ключ ' + str(e) + ' необходим'
    except Exception as e:
        slog(str(e), 'e')
        return 'Возникла странная ошибка, пускай админ проверит логи'


def user_profile_delete(params: dict[str, any]):
    try:
        execute_sql_dict(
            DELETE_USER_PROFILE,
            {'account_user_id': params['account_user_id']}
        )
        return 'Профиль удален'
    except KeyError as e:
        return 'Ключ ' + str(e) + ' необходим'
    except Exception as e:
        slog(str(e), 'e')
        return 'Возникла странная ошибка, пускай админ проверит логи'


def user_profile_show():
    try:
        return peeler(execute_sql_dict(
                SHOW_ALL_USER_PROFILE
            )
        )
    except KeyError as e:
        return 'Ключ ' + str(e) + ' необходим'
    except Exception as e:
        slog(str(e), 'e')
        return 'Возникла странная ошибка, пускай админ проверит логи'
