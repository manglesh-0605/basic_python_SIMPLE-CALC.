while True:

    def sum(a,b):
        sum=a+b
        print(f'the sum is {sum}')

    def sub(a,b):
        sub=a-b
        print(f'the Difference is {sub}')

    def mul(a,b):
        mul=a*b
        print(f'the Multiplication is {mul}')

    def div(a,b):
        div=a/b
        print(f'the Division is {div}')

    def fdiv(a,b):
        fdiv=a//b
        print(f'the Floor division is {fdiv}')

    def modulus(a,b):
        mod=a%b
        print(f'the Modulus  is {mod}')


    print('simple calculator')

    a=int(input('Enter 1st number\n'))
    b=int(input('Enter 2st number\n'))
    print('select operators from (+,-,/,*,//,%)')
    operator=input('Enter operator to apply on numbers\n')
    if operator=="+":
        sum(a,b)
    elif operator=="-":
        sub(a,b)
    elif operator=="*":
        mul(a,b)
    elif operator=="/":
        div(a,b)
    elif operator=="//":
        fdiv(a,b)
    elif operator=="%":
        modulus(a,b)
    else:
        print('Invalod input')
    
    print('if you want to continue press y else n')
    choise=input('Enter youe choise\n Y/n:')
    if choise=="Y" or choise=='y':
        continue
    elif choise=="N" or choise=='n':
        break
    else:
        print('You are dumb cicking out')
        break

