# Email header information
header_variables = {"email_title": "My Email Title"}

# Email body information
body_variables = {}

# User information, each variable in the array is a different person that will be generated separately
user_variables = [
    {
        "filename": "my_user_signature",
        "name": "My name",
        "role": "My role",
        "phone": {"href": "tel:31 90000-0000", "text": "31 90000-0000"},
        "website": {"href": "127.0.0.1", "text": "mywebsite.com"},
        "linkedin": {"href": "127.0.0.1", "text": "LinkedIn Username"},
        "email": {"href:": "mailto:my@email.com", "text": "my@email.com"},
    }
]
