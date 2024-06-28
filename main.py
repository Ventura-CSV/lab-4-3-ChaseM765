def main():

    total = 0
    x = 0 
    while x<5:
        num = int(input('Enter value: '))
        total += num
        x += 1
    print(total)
    
    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
