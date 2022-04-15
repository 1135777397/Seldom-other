def first_decorator(func):
    def name_wrapper():
        print(f"被装饰的函数 {func.__name__} 即将执行")
        func()
        print(f"被装饰的函数 {func.__name__} 执行完毕")

    return name_wrapper

@first_decorator
def add():
    print("函数 add 正在执行 ")

# add = first_decorator(add)
add()

