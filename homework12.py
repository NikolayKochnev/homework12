def test(*args):
     print('test_')
     print('тип args:', type(args))
     print(args)
     for i, arg in enumerate(args):
         print('параметр', i, arg)
test('hi', 2, 5,5, True)



def factorial(n):
    if n == 1:
        return 1
    return factorial(n -1) * n
print(factorial(8))