
def insertion_sort(arr):
    l = len(arr)
    i=1
    while i<l:
        x=arr[i]
        j=i-1
        while j>=0 and arr[j]>x:
            arr[j+1] = arr[j]
            j=j-1

        arr[j+1]=x
        i=i+1

    return arr



def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]



def bubble_sort(alist):
    n=len(alist)
    for i in range(n):
        for j in range(i):
            if alist[j]>alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp



    return alist           


def merge(left,right,compare):
	result = [] 
	i,j = 0,0
	while (i < len(left) and j < len(right)):
		if compare(left[i],right[j]):
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while (i < len(left)):
		result.append(left[i])
		i += 1
	while (j < len(right)):
		result.append(right[j])
		j += 1
	return result



def merge_sort(arr, compare = lambda x, y: x < y):
     #Used lambda function to sort array in both(increasing and decresing) order.
     #By default it sorts array in increasing order
	if len(arr) < 2:
		return arr[:]
	else:
		middle = len(arr) // 2
		left = merge_sort(arr[:middle], compare)
		right = merge_sort(arr[middle:], compare)
		return merge(left, right, compare)
