def generate_db_where(queries:dict) -> str:

    def __quote_if_str__(value):
        if type(value) == str:
            return '\'' + value + '\''
        else:
            return value
    filters:str = 'where '
    for key in queries:
        value = __quote_if_str__(queries[key])
        filters += str(key) + '=' + str(value) + ' and '

    return filters.removesuffix(' and ')