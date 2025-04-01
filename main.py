import settings
from generator.html_file import save, get_filename
from generator.replace_variables import replace_variables
from generator.background_image import generate_background_image
import toronado


def main():
    signature_template = open("signature_template.html", "r", encoding="utf-8").read()

    for user_variable in settings.user_variables:
        generate_background_image(user_variable["filename"])

        signature = signature_template

        signature = replace_variables(signature, settings.header_variables, "header")
        signature = replace_variables(signature, settings.body_variables, "body")
        signature = replace_variables(signature, user_variable, "user")

        signature = toronado.from_string(signature).decode("utf-8")

        filename = get_filename(user_variable)
        save(filename, signature)


if __name__ == "__main__":
    main()
