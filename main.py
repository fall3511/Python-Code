def evenSum(array):
    sum1 = 0
    evenArr = []
    for i in array:
        if i%2 == 1:
            continue
        else:
            evenArr.append(i)
            
    for j in evenArr:
        sum1 += j

    print(sum1)        
    return 0

def oddSum(array):
    sum1 = 0
    oddArr = []
    for i in array:
        if i%2 == 0:
            continue
        else:
            oddArr.append(i)
            
    for j in oddArr:
        sum1 += j

    print(sum1)        
    return 0

        
def main():
    size = int(input("Number of elements in the Array : "))
    numbers = list(map(int,input("Enter elements of Array : ").strip().split()))

    opt = int(input("Enter 1 for Odd Sum and 2 for Even Sum of the Array : "))
    if opt == 1:
        oddSum(numbers)
    elif opt == 2:
        evenSum(numbers)
    else:
        print("Invalid Option")

main()
        
