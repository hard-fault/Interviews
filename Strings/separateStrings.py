str = "\"America\", is a \"land of opportunities\" as well"
print(str)
found = False
stack = []
result = []

for i in range(len(str)):
    if str[i] == "\"":
        found = True if not found else False
    elif not found and str[i] == " ":
        result.append("".join(stack))
        stack = []
    else:
        stack.append(str[i])

result.append("".join(stack))
print (result)
