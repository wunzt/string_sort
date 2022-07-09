# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/08/2022
# Description: Sorts a list of string alphabetically, ingoring case.

def string_sort(string_list):
    """Uses insertion sort to sort a list of strings alphabetically, ignoring case."""
    for index in range(1, len(string_list)):
        value = string_list[index]
        pos = index - 1

        while pos >= 0 and string_list[pos].lower() > value.lower():
            string_list[pos + 1] = string_list[pos]
            pos -= 1

        string_list[pos + 1] = value

    return string_list