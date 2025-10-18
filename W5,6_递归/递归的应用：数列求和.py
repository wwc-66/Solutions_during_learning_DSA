def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]

    else:
        return numlist[0] + listsum(numlist[1:])


numlst = eval(input())
print(listsum(numlst))