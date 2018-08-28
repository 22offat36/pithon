def fact():
#added comment
#added second comment
    number=input("Enter a number to calculate the factorial: ")
    initialvalue=0
    factorial=1
    run=1
    for run in range(1,number):
            factorial=factorial * (number - initialvalue)
            initialvalue = initialvalue + 1
    print "The Factorial is =" , factorial
fact()
