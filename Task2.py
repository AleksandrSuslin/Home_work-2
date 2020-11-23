el_count = list(input("Введите количество элементов списка:  "))
for el in range( 1,len(el_count),2):
    el_count[el], el_count[el-1] = el_count[el-1], el_count[el]
print(el_count)



