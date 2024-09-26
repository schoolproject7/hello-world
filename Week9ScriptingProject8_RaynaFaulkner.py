def traceElements(lyst, index):
    if(index == len(lyst)):
        return
    else:
        print(lyst[index])
        traceElements(lyst, index+1)

traceElements([1, 2, 3, 4, 5, 6, 7], 0)
