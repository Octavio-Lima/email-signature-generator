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


