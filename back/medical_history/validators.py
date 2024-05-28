def validate_name(value):
    if "invalid" in value:
        raise ValueError("Name contains invalid content")


def validate_added_by_is_positive_integer(value):
    if value not in "0123456789" and int(value) < 0:
        raise ValueError("Added bye contains wrong values")
