from typing import Any


def get_filename(user_variable: dict[str, Any]):
    return user_variable.get(
        "filename", user_variable.get("user_name", "undefined_filename")
    )
