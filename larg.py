num = [9,3,5,2,6,22,55,764,2]
largfar=-1
nums=0
print('before',largfar)
def larg():
     global largfar
     for nums in num:
        if nums > largfar:
            largfar= nums
     print(num)
larg()
print('After', largfar)
print("rev array",num[::-1])
sortednum= sorted(num)
num.sort(reverse=True)
print("sorted",sortednum)
print("des sort", num)