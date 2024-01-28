temp = "5 degrees"
cel = 0
try:
    fah = float(temp)
except:
    fah = -1
    print("something wrong")
cel = (fah - 32.0) * 5.0 / 9.0
print(cel)