"""
Utility functions for greeting and saying goodbye.
These functions are exposed via fire_expose.py for CLI usage.
"""


def greet(name):
    """
    Greet a person by name.
    
    Args:
        name (str): Name of the person to greet
        
    Returns:
        str: Greeting message
    """
    message = f"Привіт, {name}! Радий тебе бачити!"
    print(message)
    return message


def goodbye(name):
    """
    Say goodbye to a person by name.
    
    Args:
        name (str): Name of the person to say goodbye to
        
    Returns:
        str: Goodbye message
    """
    message = f"До побачення, {name}! Гарного дня!"
    print(message)
    return message