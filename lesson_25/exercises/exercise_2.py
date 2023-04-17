# write a function that accepts an encoded string as a parameter. This string will contain a first name, last name, and an id.
# Values in the string can be separated by any number of zeros. The id is a numeric value but will contain no zeros.
# The function should parse the string and return a Python dictionary that contains the first name, last name, and id values.
# An example input would be “Robert000Smith000123”. The function should return the following using that input:
# { “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }

from typing import Dict


def get_person_info(info_string: str) -> Dict[str, str]:
    id_parameters_names = ["first_name", "last_name", "id"]
    info_list = info_string.split("0")
    print(info_list)
    info_list = " ".join(info_list).split()
    print(info_list)
    person_info = dict(zip(id_parameters_names, info_list))
    return person_info


info_string = "Robert00Smith000000123"

print(get_person_info(info_string))
