from django.core.cache import cache

from config.utils import execute_sql

from dbsetter.diseases.request_diseases import (
    SHOW_ALL_DISEASES,
    SHOW_DISEASES_BY_ALL_TAG,
    SHOW_DISEASES_BY_PART_CODE,
    
    SHOW_DISEASES_BY_PART_NAME,
    SHOW_DISEASES_BY_ALL_NAME,
)


# Get all diseases list with description
def get_all_diseases():
    return execute_sql(SHOW_ALL_DISEASES)


# Get all diseases list with description by tag
def get_diseases_by_tag(tag):
    return execute_sql(SHOW_DISEASES_BY_ALL_TAG, [tag])


# Get all diseases list with description by part of code
def get_diseases_by_part_of_tag(part_of_tag):
    return execute_sql(SHOW_DISEASES_BY_PART_CODE, [f'%{part_of_tag}%'])


# Get all diseases list with description by name
def get_diseases_by_name(name):
    return execute_sql(SHOW_DISEASES_BY_ALL_NAME, [name])


# Get all diseases list with description by part of name
def get_diseases_by_part_of_name(part_of_name):
    return execute_sql(SHOW_DISEASES_BY_PART_NAME, [f'%{part_of_name}%'])


# Peel result of functions above
def peel_diseases(data, num):
    parsed_data = {}

    for item in data[0]:
        dis_name = item[num + 1]

        if dis_name not in parsed_data:
            parsed_data[dis_name] = {}

        parsed_data[dis_name]['tag'] = item[num]

        parsed_data[dis_name]['description'] = item[num + 2]

        parsed_data[dis_name]['period'] = item[num + 3]

        if 'symptomps' not in parsed_data[dis_name]:
            parsed_data[dis_name]['symptomps'] = {item[num + 4]}
        else:
            parsed_data[dis_name]['symptomps'].add(item[num + 4])

        if 'forms' not in parsed_data[dis_name]:
            parsed_data[dis_name]['forms'] = {item[num + 5]}
        else:
            parsed_data[dis_name]['forms'].add(item[num + 5])

        if 'form descriptions' not in parsed_data[dis_name]:
            parsed_data[dis_name]['form descriptions'] = {item[num + 6]}
        else:
            parsed_data[dis_name]['form descriptions'].add(item[num + 6])

        if 'form symptomps' not in parsed_data[dis_name]:
            parsed_data[dis_name]['form symptomps'] = {item[num + 7]}
        else:
            parsed_data[dis_name]['form symptomps'].add(item[num + 7])

    # Save all to cache with full tag
    for item in parsed_data:
        current_disease = parsed_data[item]
        tag_w_space = current_disease['tag'].replace(' ', '_')
        cache_result = cache.get(f'diseases_by_tag_{tag_w_space}')
        if cache_result is None:
            cache.set(f'diseases_by_tag_{tag_w_space}', {
                item: current_disease})
        else:
            cache.set(f'diseases_by_tag_{tag_w_space}', {
                **cache_result,
                item: current_disease})

    return parsed_data


# Peel result of function which is working with part of tag
def peel_diseases_names(data, num):
    return {item[num] for item in data[0]}


# Save to cache all diseases and returns them
def cache_all_diseases():
    result = peel_diseases(get_all_diseases(), 3)
    cache.set('diseases_all', result, None)
    return result


# Returns cached diseases otherwise gets all diseases then cache it and return
def get_cached_diseases():
    get_all = cache.get('diseases_all')
    if get_all is None:
        get_all = cache_all_diseases()
    return get_all
