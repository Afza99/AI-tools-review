# calculator.py (edited)

def Add(a, b):  # bad naming
    """
    Returns the sum of two numbers.
    
    Args:
        a: The first number.
        b: The second number.
    
    Returns:
        The sum of a and b.
    """
    return a+b  # no spacing

def subtract(a, b):
    """
    Calculates the difference between two numbers.
    
    Args:
        a: The number from which to subtract.
        b: The number to subtract.
    
    Returns:
        The result of a minus b.
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of two numbers.
    
    Args:
        a: The first number.
        b: The second number.
    
    Returns:
        The result of multiplying a by b.
    """
    return a * b

def divide(a, b):  # missing zero-division check
    """
    Returns the quotient of a divided by b.
    
    Note:
        This function does not check for division by zero and will raise a ZeroDivisionError if b is zero.
        
    Args:
        a: The dividend.
        b: The divisor.
    
    Returns:
        The result of dividing a by b.
    """
    return a / b

def double(x):
    """
    Returns the value of x multiplied by 2.
    
    Args:
        x: The number to double.
    
    Returns:
        The result of x times 2.
    """
    return x * 2
