def test_function():
#    global a
#    nonlocal a
    a = 'Я в области видимости функции test_function'
    def inner_function():
#        global a
#        nonlocal a
        a = 'Я в области видимости функции inner_function'
        return a
    inner_function()
    return a


a = 'Я в области видимости функции global'
#inner_function()
test_function()
print(a)