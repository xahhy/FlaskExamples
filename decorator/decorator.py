# from functools import wraps

def decorate(name):
    def wrapper(func):
        def sub_wrapper(*args, **kwargs):
            print("定义一个装饰器", name)
            val = func(*args, **kwargs)
            return val

        return sub_wrapper

    return wrapper


@decorate('hhy')
def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add(1, 2))
