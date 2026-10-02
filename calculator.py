def calculate_average(numbers):
    """Returns the average of a list of numbers."""
    if not numbers:
        return 0.0
    total = sum(numbers)
    return total / len(numbers)

def calculate_total(numbers):
    """Returns the sum of a list of numbers."""
    return sum(numbers)