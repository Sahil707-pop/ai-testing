def calculate_average(numbers):
    """Returns the average of a list of numbers."""
    total = sum(numbers)
    # BUG: If numbers is empty, len(numbers) is 0, causing a ZeroDivisionError
    return total / len(numbers)
def calculate_total(numbers):
    """Returns the sum of a list of numbers."""
    return sum(numbers)
