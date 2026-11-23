def ticket_price(ticket_count):
    """Calculate the total price for a number of tickets at a fixed price."""
    if type(ticket_count) is not int:
        raise TypeError("invalid argument type")
        
    if ticket_count < 0:
        raise ValueError("argument outside permitted range")

    return max(ticket_count, 1) * 1200
