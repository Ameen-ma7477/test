def get_number():
    '''input number from the user and return
    '''
    num = int(input('enter number: '))
    return num

def odd_even(num):
    '''checkking if number is odd or even
    '''
    if num % 2 == 0:
        print('even')
    else:
        print('odd')
def check_sign(num):
    '''checking if number is positive or negative
    '''
    if num >0:
        print('positiv')
    elif num <0 :
        print('negative')
    else:
        print('zero')
def find_square(num):
    print('square = ', num**2)
def find_cube(num):
    print('cube = ',num**3)
def main():
    num = get_number()
    odd_even(num)
    check_sign(num)
    find_square(num)
    find_cube(num)
main()