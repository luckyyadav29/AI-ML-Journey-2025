def collatz(number):
    '''function to print collatz sequence'''
    try:
        if number%2==0:
            result = number//2
        else:
            result = number*3+1
        print(result, end=' ')
        return result
    except ValueError:
        print("Enter the positive Integer")

def main():
    num=int(input("Enter number\n"))
    print(num, end=' ')
    while True:
        num=collatz(num)
        if num==1:
            break
    
main() #calling main function   