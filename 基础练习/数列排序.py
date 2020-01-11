length = int(input())
# 这里的map函数是对后面的列表进行操作，将里面的字符转换为字符串，
# 但是由于map没有sort属性，所以要将他转换为list格式
array = list(map(int, input().split())) 
array.sort()
for i in range(len(array)):
    print(array[i], end=' ')


# map函数是python内置的高阶函数，对传入的list的每一个元素进行映射,
# 返回一个新的映射之后的list