def Linear_Search(arr,target):
  
    #iterate to the end of the list
    for i in range(len(arr)):
        #match found, return true
        if arr[i]==target:
            return True

    return False
		
