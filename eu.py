#def - определение
#def say_hi(name):
    #print(f"Hello {name }")
#say_hi - название функции
#(name) - аргемент
#say_hi("Bob")
#say_hi("Sara")
#def summ(num_1, num_2):
    #print(num_1+num_2)
#summ(3,4)
#def sub(num_1,num_2):
    #print(num_1-num_2)
#sub(8,6)
#def mul(num_1,num_2):
    #print(num_1*num_2)
#mul(5,9)

def division(num_1,num_2):
    if num_2==0:
        print("Ты тупой?")
    else:
        print(num_1/num_2)
division(8,0)

def division_1(num_1,num_2):
    try:
        print(num_1/num_2)
    except ZeroDivisionError:
        print("Сходи к доктору!")
num_1=int(input())
num_2=int(input())

division_1(num_1,num_2)