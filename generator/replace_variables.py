from typing import Any
import re


def replace_variables(
    signature_template: str, variable_dict: dict[str, Any], prefix: str
) -> str:
    for variable_key in variable_dict:
        signature_template = key_loop(
            [prefix, variable_key], variable_dict, signature_template
        )

    return signature_template


def key_loop(key: list[str], dictionary: dict[str, Any], signature: str):
    variable = get_variable(key, dictionary)

    if isinstance(variable, dict):
        for variable_dict_key in variable:
            signature = key_loop([*key, variable_dict_key], variable, signature)
    else:
        variable_text = r".".join(key)
        regex = r"(?=\{%text%).*?(?<=\})".replace("%text%", variable_text)
        signature = re.sub(regex, variable, signature)

    return signature


def get_variable(key: str, dictionary: dict[str, Any]):
    join_key = ".".join(key)
    variable = dictionary.get(key[-1], f"undefined: {join_key}")

    return variable
