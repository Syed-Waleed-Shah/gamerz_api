def generate_db_where(queries:dict) -> str:
    filters:str = 'where '
    for key in queries:
       
        filters += str(key) + '=:' + str(key) + ' and '

    return filters.removesuffix(' and ')


def generate_db_insert(data:dict) -> str:
    part1 = '('
    part2 = ' values('
    for key in data:
        part1 += str(key) + ', '
        part2 += ':' + str(key) + ', '
    part1 = part1.removesuffix(', ')
    part2 = part2.removesuffix(', ')
    part1 += ') '
    part2 += ')'

    return part1 + part2

def generate_db_update(data:dict) -> str:
    result = 'set '
    for key in data:
        result += str(key) + '=:' + str(key) + ', '
    return result.removesuffix(', ') + ' '
