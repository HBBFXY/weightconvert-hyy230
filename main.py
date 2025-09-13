def main():
    s=input().strip()
    if s.endswith('kg'):
        kg=float(s[:-2])
        pd=kg*2.2046
        print(f"对应的英制重量为{pd:.3f}镑")
    elif s.endswith('pd'):
        pd=float(s[:-2])
        kg=pd/2.2046
        print(f"对应的公制重量为{kg:.3f}公斤")
    else:
        print("输入格式错误,请输入kg或pd结尾的字符串")
if __name__=='__main__':
    main()
