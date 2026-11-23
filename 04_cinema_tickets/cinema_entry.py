def can_watch(age):
    """Determine whether a customer meets the screening age requirement."""
    if type(age) is not int:
        raise TypeError("invalid argument type")
        
    if age < 0:
        raise ValueError("argument outside permitted range")

    return age > 16
