def SubExpressionEle(Code):
    print('___SUBEXPRESSION ELIMINATION___')

    print('Code Befor Optimization.........')
    for i in Code:
        print(i)
    
    LeftExpression = []
    RightExpression = []
    CommonExpression = []
    CommonExpressionDict = { }
    Ans = []

    for i in Code:
        SplitExpression = i.split('=')
        if SplitExpression[1] not in RightExpression:
            LeftExpression.append(SplitExpression[0])
            RightExpression.append(SplitExpression[1])
        else:
            CommonExpression.append(SplitExpression[0])
            Index = RightExpression.index(SplitExpression[1])
            CommonExpressionDict[SplitExpression[0]] = LeftExpression[Index]
    for i in RightExpression:
        for j in CommonExpression:
            if j in i.split(" "):
                i = i.replace(j, CommonExpressionDict[j])
        Ans.append(i)
    ZipCode = zip(LeftExpression, Ans)

    print('Code After Optimization.....')
    for x, y in ZipCode:
        print(str(x) + "=" + str(y))


if __name__ == '__main__':
    Code = []
    for i in range(int(input('Enter Number Of Lines: '))):
        Code.append(input('Enter Code Expression: '))
    SubExpressionEle(Code)

# I/O:
# Enter Number Of Lines: 4
# Enter Code Expression: s1=4 * i
# Enter Code Expression: s2=3 + j
# Enter Code Expression: s3=4 * i
# Enter Code Expression: s4=s1 + s3 * 4
# ___SUBEXPRESSION ELIMINATION___
# Code Befor Optimization.........
# s1=4 * i
# s2=3 + j
# s3=4 * i
# s4=s1 + s3 * 4
# Code After Optimization.....
# s1=4 * i
# s2=3 + j
# s4=s1 + s1 * 4