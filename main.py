from dudaiev_operations import add, subtract, multiply, divide, and_func, or_func, xor_func, not_func

def test():
    print(f"Додавання: {add(1, 1)}")
    print(f"Віднімання: {subtract(1, 1)}")
    print(f"Множення: {multiply(2, 2)}")
    print(f"Ділення: {divide(6, 2)}")
    print(f"Логічне і: {and_func(True, False)}")
    print(f"Логічне або: {or_func(False, True)}")
    print(f"Виключне або: {xor_func(6, 2)}")
    print(f"Логічне ні: {not_func(1, 1)}")

test()