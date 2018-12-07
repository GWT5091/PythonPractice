#Python_Practice02(12/8/Sat)
#Collatz Matrix
def collatz(num):
    if num % 2 == 0:
        return num /2
    else:
        return 3*num +1

def main():
    print('Enter the number')
    inp = int(input())
    print(inp)
    while(inp != 1):
        inp = int(collatz(inp))
        print(inp)

if __name__ == "__main__":
    main()
