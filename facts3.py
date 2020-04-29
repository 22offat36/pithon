def fact():
#added comment
#adde
#added second comment
    number=input("Enter a number to calculate the factorial: ")
#    number=5
    number=int(number)
    print"Calculating Factorial of 5"
    if number > 0:
       initialvalue=0
       factorial=1
       run=1
       for run in range(1,number):
            factorial=factorial * (number - initialvalue)
            initialvalue = initialvalue + 1
       print "The Factorial is =" , factorial
    else:
       print "Can't factorial a negative number"
fact ()
