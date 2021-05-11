def calculate(no1,no2):
    sum=no1+no2
    sub=no1=no2
    mul=no1*no2
    div=no1/no2
    return sum,sub,mul,div
    
result=calculate(100,50)
for x in result:
    print(x)
