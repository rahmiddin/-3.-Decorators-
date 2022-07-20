import datetime
from functools import wraps

'''
1
    '''


def loger(functions):
    
    @wraps(functions)
    def time_log(*args, **kwargs):
        
        with open('file.text', 'w') as file:
            file.write(f'Была запушена функция {functions.__name__}' + '\n')
            file.write(f'Время и дата: {datetime.datetime.now()}' + '\n')
            file.write(f'Аргументы: {*args, *kwargs}' + '\n')
            file.write(f'Возврашаемое значение: {functions(*args,**kwargs)}')
    return time_log


'''
2
    '''


def multiply(url):
    
    def loger_with_url(functions):
        @wraps(functions)
        def time_log(*args, **kwargs):
            with open(f'{url}/file.text', 'w') as file:
                file.write(f'Была запушена функция {functions.__name__}' + '\n')
                file.write(f'Время и дата: {datetime.datetime.now()}' + '\n')
                file.write(f'Аргументы: {*args, *kwargs}' + '\n')
                file.write(f'Возврашаемое значение: {functions(*args, **kwargs)}')
        
        return time_log

    return loger_with_url