def demo(num, num_list, tuple_list):
    print("num:%d" % num)
    print("函数内部")
    # 在函数内部 使用赋值语句, 不会修改到外部的实参变量
    num = 100
    num_list = [1, 2, 3]
    tuple_list = (4, 5, 6)
    print("赋值后的num:%d" % num)
    print(num_list)
    print(tuple_list)
    print("函数执行完成")


gl_num = 99
gl_list = [4, 5, 6]
gl_tuple_list = (1, 2, 3)
demo(gl_num, gl_list, gl_tuple_list)
print("gl_num: %d" % gl_num)
print(gl_list)
print(gl_tuple_list)
