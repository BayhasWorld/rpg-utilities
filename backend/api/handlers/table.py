# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_

Returns:
    _type_: _description_
"""
from api.handlers import calculation  # pylint: disable=cyclic-import
from api.handlers import conditional  # pylint: disable=cyclic-import
from api.handlers import die_roll

def run_child(run_input, additional_input):
    # TODO: update docstring
    """_summary_

    Args:
        run_input (dict): The parameters used to run the
        additional_input (dict): _description_

    Returns:
        dict:
    """
    result = None
    if 'calculation' in run_input:
        result = \
            calculation.run(run_input['calculation']['input'],
                            additional_input)
    elif 'die_roll' in run_input:
        result = \
            die_roll.run(run_input['die_roll']['input'],
                         additional_input)
    elif 'conditional' in run_input:
        result = \
            conditional.run(run_input['conditional']['input'],
                additional_input)
    elif 'table' in run_input:
        result = \
            run(run_input['table']['input'],
                      additional_input)
    else:
        res = list(run_input.keys())[0]
        result = 'Invalid Method Option: "' + str(res) + '"!'
    return result

def get_choice(run_input, additional_input):
    # TODO: update docstring
    """_summary_

    Args:
        run_input (_type_): _description_
        additional_input (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = None
    choice = run_input['choice']
    if isinstance(choice, str):
        if additional_input:
            if choice in additional_input:
                choice = additional_input[choice]
    elif isinstance(choice, dict):
        choice = run_child(run_input['choice'], additional_input)

    if choice:
        result = choice
    else:
        result = run_input['choice']
    return result

def get_value(choice, run_input, additional_input):
    # TODO: update docstring
    """_summary_

    Args:
        choice (_type_): _description_
        run_input (_type_): _description_
        additional_input (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = None
    for row in run_input['choices']:
        low = row['low']
        high = row['high']
        if choice in range(low, high + 1):
            if isinstance(row['value'], dict):
                result = run_child(row['value'], additional_input)
            else:
                result = row['value']
    return result

def process_percentile(run_input, additional_input):
    # TODO: update docstring
    """_summary_

    Args:
        run_input (_type_): _description_
        additional_input (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = None
    choice = None
    if not isinstance(run_input['choice'], int):
        choice = get_choice(run_input, additional_input)
        if not choice:
            result = choice
    else:
        choice = run_input['choice']

    result = get_value(choice, run_input, additional_input)
    return result

def process_simple(run_input, additional_input):
    # TODO: update docstring
    """_summary_

    Args:
        run_input (_type_): _description_
        additional_input (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = None
    choice = None
    choice = get_choice(run_input, additional_input)
    if not choice:
        result = choice
    else:
        run_input['choice'] = str(choice)

    choice = str((run_input['choice']))
    table = run_input['choices']
    if choice in table:
        result = table[choice]
    else:
        result = 'no result matched'
    return result

def run(run_input, additional_input=None):
    # TODO: update docstring
    """_summary_

    Args:
        run_input (_type_): _description_
        additional_input (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    result = None
    if run_input['style'] == 'simple':
        result = process_simple(run_input, additional_input)
    elif run_input['style'] == 'percentile':
        result = process_percentile(run_input, additional_input)
    return result
