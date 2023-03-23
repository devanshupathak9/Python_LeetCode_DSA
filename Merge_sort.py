def merge_sort(arr,l,r):
	if l==r:
		return [arr[l]]
	mid=(l+r)//2
	lft=merge_sort(arr,l,mid)
	rght=merge_sort(arr,mid+1,r)
	i,j=0,0
	newarr=[]
	while i<len(lft) and j<len(rght):
		if lft[i]<rght[j]:
			newarr.append(lft[i])
			i+=1
		else:
			newarr.append(rght[j])
			j+=1
	while i<len(lft):
		newarr.append(lft[i])
		i+=1
	while j<len(rght):
		newarr.append(rght[j])
		j+=1
	return newarr

#arr=list(map(int,input().split()))
arr=[2,3,6,5,1,7,9,8,0,12,10]
n=len(arr)
New=merge_sort(arr,0,n-1)
print(New)