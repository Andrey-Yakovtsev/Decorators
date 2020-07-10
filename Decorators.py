from datetime import datetime


def upper_case(old_foo):
    def new_foo(*args, **kwargs):
        result = old_foo(*args, **kwargs)
        return result.upper()
    return new_foo




# def logger(oldfoo):
#     date = datetime.now()
#
#     def newfoo(*args, **kwargs):
#         # nonlocal date
#         # nonlocal time
#         result = oldfoo(*args, **kwargs)
#         with open('logs/trace.log', 'a', encoding='utf-8') as fi:
#             fi.write(f'Вызвали функцию с именем "{oldfoo.__name__}"\n'
#                   f'c аргументами "{args}" и "{kwargs}"\n'
#                   f'Время старта: {date}\n'
#                   f'Возвращаемое значение: "{result}"\n'
#                      f'________________________________\n')
#             return result
#
#     return newfoo

# @logger
# def hello_world(a, b):
#     return 'hello world'
#
# hello_world(1, 2)

def parametrized_logger(parameter):

    def logger(oldfoo):
        date = datetime.now()

        def newfoo(*args, **kwargs):
            # nonlocal date
            # nonlocal time
            result = oldfoo(*args, **kwargs)
            with open(parameter, 'a', encoding='utf-8') as fi:
                fi.write(f'Вызвали функцию с именем "{oldfoo.__name__}"\n'
                         f'c аргументами "{args}" и "{kwargs}"\n'
                         f'Время старта: {date}\n'
                         f'Возвращаемое значение: "{result}"\n'
                         f'________________________________\n')
                return result

        return newfoo

    return logger


@parametrized_decor(parameter=None)
def foo():
    pass
