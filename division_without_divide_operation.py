def divide(numerator, denominator, num_decimal_places):
    """Divides one integer by another without directly using division.

    Args:
        numerator: integer value of numerator
        denominator: integer value of denominator
        num_decimal_places: number of decimal places desired in result

    Returns:
        - Type 'float' containing result of division to specified number of
          decimal places; final digit not rounded

    Raises:
        ValueError: if 'denominator' is zero or 'num_decimal_places' is not
                    positive integer
    """
    
    if denominator == 0 or num_decimal_places < 0:
        raise ValueError

    pieces = []

    # determine sign of final number, then make both numerator and denominator
    # positive for simplicity
    sign = 1
    if numerator < 0:
        sign = -sign
        numerator = -numerator
    if denominator < 0:
        sign = -sign
        denominator = -denominator
    if sign < 0:
        pieces.append('-')

    # determine integral part
    num_units = 0
    while numerator >= denominator:
        numerator -= denominator
        num_units += 1
    pieces.append(str(num_units))

    pieces.append('.')

    # determine fractional part
    for i in range(num_decimal_places):
        numerator *= 10
        num_units = 0
        while numerator >= denominator:
            numerator -= denominator
            num_units += 1
        pieces.append(str(num_units))

    return float(''.join(pieces))
