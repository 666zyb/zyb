'''
列表 :由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0~9或所有家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素之间可以没有
任何关系。
访问列表中的元素用索引（下标），从0开始，依次增加,也可以从后往前，从-1开始，依次递减
'''
list_1 = ['China', 'Chinese', 'people', '1', 'b']  # 用方括号[]来表示列表，并用逗号来分隔其中的元素。
print(list_1)
### ['China','Chinese','people','1','b']
print(list_1[0])  # [0]是列表第一个元素的索引，[1]是第二个的，后面类推
### China
print(list_1[-1])  # [-1]是列表最后一个元素的索引，[-2]是倒数第二个，前面类推
### b
'''
修改，添加和删除列表元素
'''
list_1[0] = '中国'  # 修改
list_1.append('happy')  # 在列表末尾添加元素
del list_1[1]  # 删除
list_1.insert(2, 'Hi')  # 插入,在索引为2的地方插入元素’Hi‘
print(list_1)
### ['China', 'Chinese', 'people', '1', 'b']
### China
### b
### ['中国', 'people', 'Hi', '1', 'b', 'happy']
'''
方法pop() 可删除列表末尾的元素，并让你能够接着使用它。
实际上pop()可以删除列表中的任何元素，并且能够继续使用被删除的元素，只需要在括号里面填入要删除的元素的索引
del和pop()的区别就是使用del删除元素之后就不能在使用被删除的元素，而pop()可以继续使用
如果不知道元素的具体位置和索引，只知道元素是什么，可以用remove()方法,但是remove()只能删除一个，如果元素出现多次，则只删除
第一个出现的，可以用循环依次全部删除
'''
str1 = list_1.pop()
print(str1)
print(list_1)
### happy
### ['中国', 'people', 'Hi', '1', 'b']
str2 = list_1.pop(2)
print(str2)
print(list_1)
### Hi
### ['中国', 'people', '1', 'b']
list_1.remove('people')
print(list_1)
### ['中国', '1', 'b']
