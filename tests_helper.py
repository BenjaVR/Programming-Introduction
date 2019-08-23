import os
import sys
import unittest
from subprocess import check_output, CalledProcessError
from typing import List


def call_module(test: unittest.TestCase, output_size: int, *args: str, filter_empty: bool = True) -> List[str]:
    """
    :param output_size: The exact allowed number of items in the output result list.
    :param test: The context of the current test case.
    :param args: The parameters to pass to the imported module.
    :param filter_empty: Filter empty strings out of the output list. Defaults to 'True'.
    :return: The output of the imported module (print()).
    """
    try:
        script_path = os.path.join(os.getcwd(), '..', 'task.py')
        output = check_output([sys.executable, script_path], input='\n'.join(args), universal_newlines=True)
        output_list = output.split("\n")

        if filter_empty:
            filtered_output_list = list(filter(lambda x: x != '', output_list))
        else:
            filtered_output_list = output_list

        number_of_filtered_outputs = len(filtered_output_list)
        if number_of_filtered_outputs != output_size:
            test.fail(
                f'The number of outputs are not correct ({output_size} expected, but got {number_of_filtered_outputs}).')
        else:
            return filtered_output_list
    except CalledProcessError:
        test.fail('Could not execute the code, please fix any errors!')
