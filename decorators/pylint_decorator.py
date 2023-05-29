"""
A module that defines the run_pylint decorator.
"""

import os
import subprocess


def run_pylint(file_name):
    """
    A decorator that runs pylint on the specified file.

    Args:
        file_name (str): The name of the file to run pylint on.

    Returns:
        The decorated function.
    """
    def decorator(func):
        """
        The decorator function that runs pylint and then calls the decorated function.

        Args:
            func: The function to decorate.

        Returns:
            The decorated function.
        """
        def wrapper(*args, **kwargs):
            """
            The wrapper function that runs pylint and then calls the decorated function.

            Args:
                *args: Variable length argument list.
                **kwargs: Arbitrary keyword arguments.

            Returns:
                The result of the decorated function call.
            """
            runner = f"py -m pylint {os.path.abspath(file_name)}"
            # pylint: disable=subprocess-run-check
            subprocess.run(runner, shell=True)
            return func(*args, **kwargs)
        return wrapper
    return decorator

