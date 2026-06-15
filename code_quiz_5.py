s = "pythonprogramming"
a=0
b=""
for i in s:
    if(a%2==1):
        b+=(i.upper())
    else:
        b+=i
    a+=1
print(b)
print(b[::-1])