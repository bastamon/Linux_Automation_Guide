# -*- coding:utf-8 -*-
# 常用数据整理效率代码



# 2. Lambda表达式
* lambda arguments: expression
* lambda后面相当于一个function
> 函数名 = lambda 输入变量: 函数体

```
double = lambda x: x * 2
print(double(5)) # 打印10
```


# 3. Map和Fiter
* map通过对列表中每个元素执行某种操作并将其转换为新列表。
```angular2html
# Map
seq = [1, 2, 3, 4, 5]
result = list(map(lambda var: var*2, seq)) # map()函数的返回结果是list类型
print(result) # [2, 4, 6, 8, 10]
```

* Filter函数接受一个列表和一条规则，就像map一样，但它通过比较每个元素和布尔过滤规则来返回原始列表的一个子集。
```angular2html
# Filter
seq = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x > 2, seq)) # filter()返回结果与调用的seq变量类型一致
print(result) # [3, 4, 5]
```

# 4. Arange和Linspace
Arange返回给定步长的等差列表。 它的三个参数start、stop、step分别表示起始值，结束值和步长，返回NumPy数组

请注意，stop点是一个“截止”值，因此它不会包含在数组输出中。
```angular2html
# np.arange(start, stop, step)
np.arange(3, 7, 2) #返回array([3, 5])
```

Linspace以指定数目num均匀分割区间[start,end]。linspace将返回一个NumPy数组。
```angular2html
# np.linspace(start, stop, num)
np.linspace(2.0, 3.0, num=5) # 返回array([ 2.0,  2.25,  2.5,  2.75, 3.0])
```

# 5. pandas中的axis轴
在Pandas中，删除一列或在NumPy矩阵中求和值时，可能会遇到Axis。 删除一列（行）的例子：
```angular2html
df.drop('Column A', axis=1) # 按列删除有'Column A'的列标签
df.drop('Row A', axis=0) # 按行删除有'Row A'的行标签
```
同样的在NumPy中的蹋缩也是通过axis实现的
```angular2html
a = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]], [[1, 2, 3, 4], [5, 6, 7, 8]]])
b = a.sum(axis=0)# 返回[[1,3,5,7],[9,11,13,15]]
c = a.sum(axis=1) # 返回[[4,6,8,10],[6,8,10,12]]
d = a.sum(axis=2) #返回[[6,22],[10,26]]


```





如果你想处理列，将Axis设置为1，如果你想要处理行，将其设置为0。 但为什么呢？ 回想一下Pandas中的shape


    df.shape
    (# of Rows, # of Columns)


