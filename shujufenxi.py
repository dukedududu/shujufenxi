from matplotlib import pyplot
import numpy as np
f=open('datingTestSet2.txt')
filelist=f.readlines()#一行为一个列表 

miles=[]
timepercents=[]
litres=[]
tag =[]

for line in filelist:               #依次读取每行
    line=line.strip()             #去掉每行头尾空白 
    listline=line.split('\t')       #按换行符分割数据
    miles.append(float(listline[0]))
    timepercents.append(float(listline[1]))
    litres.append(float(listline[2]))
    tag.append(int(listline[3])) #第四列以整型存入标签向量，append()函数用于向列表中添加元素
'''
print(classLabelVector)
print(miles)
print(litres)
print(tag)
'''

# 关闭文件
f.close()
x='litres'
y='miles'
pyplot.xlabel('litres')
pyplot.ylabel('miles')
pyplot.title('Relationship of litres and miles')
pyplot.scatter(litres,miles,s=10,c='black',marker='o')

#设置纵坐标刻度
pyplot.yticks([0,20000,40000,60000,80000])
#设置横坐标刻度
pyplot.xticks([0.2,0.4,0.6,0.8,1.0,2.0])

pyplot.show()

