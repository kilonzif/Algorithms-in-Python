def Binary_Search(arr,target):
'''
Binary Search Algorithm implemented
Iteratively

'''
    # First and last index values
    left=0
    right=len(arr)-1
    
    while left<=right:
        mid=(left+right)//2
        # Match found
        if arr[mid]==target:
            return True
        # Set new midpoints up or down depending on comparison
        else:
            if target>arr[mid]:
                #set up
                left = mid+1

            else:
                #set down
                right = mid-1
            

    return False





def rec_bsearch(arr,target):
'''
Binary Search Algorithm implemented
Recursively

'''
    
    # Base Case!
    if len(arr) == 0:
        return False
    
    # Recursive Case
    else:
        
        mid = len(arr)//2
        
        # If match found
        if arr[mid]==target:
            return True
        
        else:
            
            # Call again on second half
            if target<arr[mid]:
                return rec_bsearch(arr[:mid],target)
            
            # Or call on first half
            else:
                return rec_bsearch(arr[mid+1:],target)
