def threeNumberSum(array, targetSum):
    output=[]
    array.sort()
    for i in range(len(array)-2):
        left=i+1
        right=len(array)-1
        while left<right:
            currSum = array[left] + array[right] + array[i]
            if currSum == targetSum:
                output.append([array[i], array[left],array[right]])
                left+=1
                right-=1
            elif currSum > targetSum:
                right-=1
            else:
                left+=1
    return output