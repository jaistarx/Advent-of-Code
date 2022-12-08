
# problem 1
arr=[]
def findLargest():
    total=0
    maxi=0

    h = open('input.txt', 'r')
    content = h.read()
    a=content.splitlines()  
    for i in a:
        if(i==''):
            arr.append(total)
            if(total>maxi):
                maxi=total
            total=0
        else:
            total=total+int(i)
    print(maxi)
findLargest()



# problem 2
def totalOfThreeLargest():
    arr_size = len(arr)
    first = arr[0]
    for i in range(1, arr_size):
        if (arr[i] > first):
            first = arr[i]

    second = arr[0]
    for i in range(0, arr_size):
        if (arr[i] > second and
            arr[i] < first):
            second = arr[i]

    third = arr[0]
    for i in range(0, arr_size):
        if (arr[i] > third and
            arr[i] < second):
            third = arr[i]

    print(first+second+third)
totalOfThreeLargest()