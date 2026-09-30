
    """Simple greeting function."""
    return f"Hello, {name}!"


def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def get_user_info(name, age):
    """Get formatted user information."""
    return f"{name} is {age} years old"


if __name__ == "__main__":
    message = greet("World")
    print(message)
    
    result_add = add(5, 3)
    print(f"5 + 3 = {result_add}")
    
    result_multiply = multiply(4, 7)
    print(f"4 * 7 = {result_multiply}")
    
    user_info = get_user_info("Alice", 25)
    print(user_info)
