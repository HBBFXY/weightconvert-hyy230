Weight_str = input()
if Weight_str in ["kg"]:
    pd = (eval(Weight_str[1]))*2.2046
    print("pd")
elif Weight_str in ["pd"]:
    pd = (eval(Weight_str[1]))/2.2046
    print("kg")
else:
    print("输入格式错误")
