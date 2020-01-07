# coding = UTF-8

str = "ASDF"
str1 = '''QWR
ZXC
'''
print('\n*'*2)
print(str+str1)
print('*\n'*3)

List = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(List[0])
List[0] = 'ilyoil'
print(List[0])
print(List[0:3])
Day = ['1', '2', '3', '4', '5']
Cal = [List, Day]
print(Cal)
print(Cal[1][0])
Day.append('Good Day!!')
print(Cal)
List.insert(1, '1')
print(List)
List.remove('1')
print(List)
List.sort()
print(List)
List.reverse()
print(List)
print(len(List))
print('\n')


