from typing import Any


def get_filename(user_variable: dict[str, Any]):
    return user_variable.get(
        "filename", user_variable.get("user_name", "undefined_filename")
    )


def save(filename: str, content: str):
    with open(f"results/{filename}.html", "w", encoding="utf-8") as update_file:
        update_file.write(content)
