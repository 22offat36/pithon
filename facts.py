def fact():
#added comment
    number=input("Enter a number to get the factorial: ")
    initialvalue=0
    factorial=1
    run=1
    for run in range(1,number):
            print(run, number, initialvalue, factorial)
            factorial=factorial * (number - initialvalue)
            initialvalue = initialvalue + 1
            print(run, number, initialvalue, factorial)
fact()
