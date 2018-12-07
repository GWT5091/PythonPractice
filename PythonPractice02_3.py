#Python_Practice02(12/7/thu)
#I learn about "Exception handling"
def spam(divide_by, num):
    try:
        return num / divide_by
    except ZeroDivisionError:
        print('不正な引数です->',num,'/',divide_by)

print(spam(0,42))
