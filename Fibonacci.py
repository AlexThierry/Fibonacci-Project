#This program calculates the fibonacci of a non negative number
#It can be done iteratively or recursively
#By Alex Thierry

#Recursive definition
def fibonacci_recusive(number):
    if number < 2:
        return number
    else:
        return fibonacci_recusive(number-2) + fibonacci_recusive(number-1) #recursive call

#Iterative definition
def fibonacci_iterative(number):
    fibbo0 = 0  #Base conditions
    fibbo1 = 1
    if number < 2:
        return number
    else:
        count = 1 #number of computation
        while count < number: #performing the successive addition
        #for count in range(1,number):
            fibbo = fibbo0 + fibbo1
            fibbo0,fibbo1 = fibbo1,fibbo
            count = count + 1
        return fibbo


#main
if __name__ == '__main__':
    try:
        number = int(input('Enter the number you wish to get its fibbonaci value : ')) #getting number from user
        if number < 0:
            print('The fibonacci of a negative number does not exist.') #factorial of a number does not exist
        else:
            fibonacci = fibonacci_iterative(number)
            #fibonacci = fibonacci_recusive(number)
            print('The fibonnaci of ',number,' is ',fibonacci,'.',sep='')
    except Exception as e:
        print('Something went wrong :',e)
