#vishnu sai reversestring 05/09/22
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
  
s = "145*999=144855"
  
print("The original string is : ", end="")
print(s)
  
print("The reversed string(using loops) is : ", end="")
print(reverse(s))
