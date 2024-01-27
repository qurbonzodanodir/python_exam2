# 1:
#     Explain the differences between tuples, lists, dictionaries, and sets in Python. Provide a use case for each data structure..
    
#     Объясните различия между кортежами, списками, словарями и множествами в Python. Предоставьте вариант использования для каждой структуры данных.

# tuples = baroi elemrntora da yakjo giriftan rangi list nake i sodda taray ham bo tez kor mekna 2 method dora count,index () -inamixe kor mekna immutible
# lists  = baroi elementora hamasha da ya jo giriftan va i biso metodo dora ba [] - inamixali qavso kati kor mekna  mutible
# dictianaries - 2 qimat megira key va value i rangi da value nom mondanay valuera ba key fayrod meknem  {} -inamixe qati kor mekna mutible
# set  elementoi 2 bor takror mewidagira namerora maqsad 1 tawon mekna mutiable
# farqi tuble list : tuble tez kor mekna nake ummutiblay  list biso method dora va mutiblay 




# 3:
#     Print all exact squares of natural numbers not exceeding a given number N.

#     Выведите все точные квадраты натуральных чисел, не превосходящие данного числа N.
#     Input data
#     15

#     Output
#     1 4 9


# n = int(input())
# i = 1
# while i < n:
#     sum = i * i 
#     if sum  < n:
#         power = sum
#         print(power,end= " ")

#     i +=1




# 2:
#     The sequence consists of natural numbers and ends with the number 0. Determine the value of the largest element of the sequence. Numbers following zero do not need to be read.

#     Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего элемента последовательности. Числа, следующие за нулем, считывать не нужно.
#     Input data
#     1
#     7
#     9
#     0

#     Output
#     9 



#a = input().split()
# maxx = -99999
# for i in a:
#      if a == '0':
#         break
#      elif int(i) > int(maxx):
#         maxx = i
   
# print(maxx)









# 4:
#     Given a list of numbers and the index of the element in the list k. Remove an element with index k.

#     Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k.
#     Input data
#     7 6 5 4 3 2 1
#     2

#     Output
#     7 6 4 3 2 1 


# n = input().split()
# index = int(input())
# n.pop(index)
# for j in n:
#     numbers = j
#     print(numbers,end=" ")










# 8:
#     Write a Python program to find the maximum and minimum product of pairs of tuples within a given list.

#     Напишите программу на Python, чтобы найти максимальное и минимальное произведение пар кортежей в заданном списке.

#     The original list, tuple : [(2, 7), (2, 6), (1, 8), (4, 9)]

#     Maximum and minimum product from the pairs of the said tuple of list: Максимальное и минимальное произведение пар   указанного кортежа списка:

#     (36, 8)



# list1 = [(2, 7), (2, 6), (1, 8), (4, 9)]
# n = 1
# m = 1
# maxx = max(list1)
# for i in maxx:
#     n *= i
# minn =min(list1)
# for j in minn:
#     m *= j    
# print(n,m)






# 6:
#     Cycle the elements of the list to the right (A[0] goes to place A[1], A[1] to place A[2], ..., last element goes to place A[0]).

#     Циклически сдвиньте элементы списка вправо (A[0] переходит на место A[1], A[1] на место A[2], ..., последний элемент переходит на место A[0]).
#     Input data
#     1 2 3 4 5

#     Output
#     5 1 2 3 4 

n = input().split()
index = n[0]
n[0]=n[4]
index1 = n[1]
n[1] = index
n[2] = index1
n[4] = index
for i in n:
    numbers = i
    print(i,end = " ")