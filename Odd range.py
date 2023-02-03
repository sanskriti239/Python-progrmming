def odd(num1,num2):
    if num1>num2:
        return
    if num1&1:
      print(num1,end=" ")
      return odd(num1+2,num2)
    else:
      return odd(num1+1,num2)
num1=1;num2=100
odd(num1,num2)