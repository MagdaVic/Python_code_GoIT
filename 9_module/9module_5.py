def format_phone_number(func):
    def inner(*args, **kwargs):
        if len(func(*args, **kwargs)) < 12:
            return '+38'+func(*args, **kwargs)
        elif len(func(*args, **kwargs)) == 12:
            return '+'+func(*args, **kwargs)
    return inner


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone
