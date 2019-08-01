# t = [1,5,8,2,5,9]
# aa = t.index(1)
# aaa = t.count(5)
#
#
# print('the data 1 index is %s,the number of 5 is %s'%(aa,aaa))
#
# aa = open('data.txt','w')
# aa.write('the word is wo have to go!\n')
# aa.write('the second word is AMD YES\n')
# aa.close()
# dd = open('data.txt','r')
#
# print(dd.readlines())
# dd.close()


# from sklearn.cluster import KMeans
#
import pandas as pd
#
# from datetime import  datetime
# data = ['abc','acd','bcd']
# data_index = ['1st','2nd','3rd']
# # data = pd.Series(data_index,data)
# data = pd.Series(data)
# print(data)
# print(type(data))
# print(data[2])

# data1 = pd.Series([1,3,3,4],['a','b','c','d'])
# data2 = pd.Series([4,2,3,5],['a','b','c','d'])
# data2['c'] = data2['c'] - data1['c']
# data3 = data1 / data2
# print(data3)

data1 = {'a':1,'b':2,'c':3,'d':4}
data2 = {'a':3,'b':5,'c':4,'d':6}


da = {'first':pd.Series(data1),'second':pd.Series(data2)}
da = pd.DataFrame(da)
print(da)
print(type(da))
# print(da['first','seond'])
data3 = pd.Series([1,4,7],['a','b','c'])
da['srd'] = data3
da['four'] = da['first'] + da['second']
aa = da.loc[['a','b'],['first','second']]
print(aa)





