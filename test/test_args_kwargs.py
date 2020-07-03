def test(*args):
    print(type(args), args)


test()
test(1)
test(1, 2)
test(1, 2, 3, 'a', [1, 2, 3])
