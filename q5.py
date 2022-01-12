def checkMirror(list):
    a = len(list)
    for i in range(a):
        if(list[i] != list[a - i - 1]):
            return False
    return True


array = [1, 2,  2, 1]
array1 = [1, 2, 3]
print(checkMirror(array))
