"""
A module that defines the method_call decorator.
"""


def method_call(func):
    """
    A decorator that prints the name of the called method and then calls it.

    Args:
        func: The method to decorate.

    Returns:
        The decorated method.
    """
    def wrapper(*args, **kwargs):
        """
        The wrapper function that adds the behavior before calling the method.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The result of the method call.
        """
        print(f"Calling method: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
