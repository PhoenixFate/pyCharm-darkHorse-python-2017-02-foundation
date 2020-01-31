def demo(num_list):
    print("函数内部")

    # 使用方法修改列表内部内容
    num_list.append(9)
    print(num_list)
    print("函数执行结束")


gl_list = [1, 2, 3]
print(gl_list)
demo(gl_list)
print(gl_list)

