def fibonacci(n):
    
    
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        

n = int(input())
print(fibonacci(n))




# def fibo(n):
#     a=b=1
#     if n < 0 :
#         print('Enter correct input')
#     elif n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         for i in range(3,n+1):
#             result = a+b
#             a=b
#             b=result
#         return result
            
# # for i in fibo(10):
# #     print(i,end=' ')
# print(fibo(9))
