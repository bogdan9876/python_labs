import logging


def logged(exception, mode):

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as current_exception:
                if mode == "console":
                    logging.basicConfig(level=logging.INFO)
                else:
                    logging.basicConfig(filename='exceptions.txt',
                                        filemode='a', level=logging.INFO)
                logging.exception(current_exception)

        return wrapper

    return decorator
