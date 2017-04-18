
    # we want to find the smallest element which is larger than value, table is sorted from smallest to largest
def search(table, a, b, value):
    while(a < b):
        middleIndex = (int)((a+b) / 2)
        if value >= table[b]:
            print('No answer')
            return
        if table[middleIndex] <= value:
            a = middleIndex + 1
        else:
                b = middleIndex

    print(table[b])

table = [5, 8, 8, 10, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 17, 19, 25, 30, 40, 41, 45, 50]
search(table, 0, 21, 45)
