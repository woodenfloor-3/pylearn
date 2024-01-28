def rev_str(instr):
     rstr=""
     index= len(instr)-1
     while index >=0:
        rstr = rstr + instr[index]
        index = index -1
     return rstr

instr=input("\nenter string\n")
revs= rev_str(instr)
print("og string \n"+instr)
print("reversed string \n" +revs)

# def rev_str(instr):
#     rstr = ""
#     index = len(instr) - 1
#     while index >= 0:
#         rstr = rstr + instr[index]
#         index = index - 1
#     return rstr

# instr = input("Enter a string: ")
# reversed_str = rev_str(instr)

# print("Original string: " + instr)
# print("Reversed string: " + reversed_str)
