def check_even_odd(num):
    if (num % 2) == 0:
        print( num, "is an even number." )
    else:
        print( num, "is an odd number." )

def main():
    num  = int(input( "Enter any number: " ))
    check_even_odd(num)

if __name__ == "__main__":
    main()
