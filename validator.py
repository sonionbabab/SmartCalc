def safe_float(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError("Please enter a valid number.")
