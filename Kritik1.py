#First step: make sure that any x value we want to apply the arctan function to, fits within the domain
x = 0.75
#Since the question asks to test values with decimals, everything for x must be written as a flot
if x < 0.0 or x > 1.0:
    print("Error! Select a value of x in the domain")

#The goal is to find a value for n that makes the expression (x^(2n+1))/(2n+1) less than or equal to 0.0001
#Notice the question says "up to an error" so that's why we include equal to
else:
    n = 0
    #n will only be integers so we can write it without a decimal
    #Second step: create a while loop

    placeholder = 0
    #choose any arbitrary variable and assign it a value. This is simply a way to make the while loop run

    while placeholder == 0:
        error = (x**(2.0*n+1.0))/(2.0*n+1.0)
        #Third step: use the right hand part of the inequality provided in the question and create an if statement
        if error <=0.0001:
            #At this point we have found an n value that results in an error less than or equal to 0.0001
            ria_est = 0
            for i in range(0, n):
            #Fourth step: create a for loop that performs the approximation equation
            #The following takes care of the summation part of the equation
                ria_est = ria_est + (((-1)**i)*x**(2*i+1))/(2*i+1)
            print(x)
            print(n)
            print(error)
            print(ria_est)
            #We want to stop the while loop now so redefine the placeholder
            placeholder = 1
        else:
            #Fifth step: if the value of n was not large enough to create a small enough error, increment it by 1
            n = n+1



