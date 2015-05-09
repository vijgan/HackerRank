'''
This function does the following,
1. Create a 2D array of same dimentions as the input and assigns 0 to ever location. 
   This is used to put not- visited node as 0 and visited node as 1
2. Have a global variable called counter to increment every connected node
3. For evey cordinate in original array, call the Depth-First Search function
   with current location, original array and visited array
4. After returning, check if global counter is greater and assign it to max_counter variable
   put back the counter back to 0. By this, it can check for new connected arrays
'''
def find_connected_cells(array,length1,length2):
    visited=[[0 for _ in range(length2)] for _ in range(length1)]
    global counter
    max_count=0
    for i in range(length1):
        for j in range(length2):
            modified_dfs(array,visited,i,j)
            if counter>max_count: max_count=counter
            counter=0     
    print (max_count)   

'''
1. This functions us recursive.
2. If the i or j cordinate is less than 0 (incorrect), return
3. If i,j is already visited (visited[i][j]) or if the original cordiante is 0 return
4. If not, increase the counter and make the visitor cordinate as 1
5. Recursively call DFS for connected corinates of the current cordinate. 
   For this iterate through x,y from -1 to 1 on both axis. If x and y are 0, skip this.
   This is because we dont have to check the current location again
'''
def modified_dfs(array,visited,i,j):
    global counter
    if i<0 or i>=length1 or j<0 or j >=length2:
        return
    if visited[i][j]==1 or array[i][j]==0:
        return
    counter+=1
    visited[i][j]=1
    for x in range(-1,2):
        for y in range(-1,2):
            if not (x==0 and y==0):
                modified_dfs(array,visited,i+x,j+y)   
            
length1=int(input())
length2=int(input())
array=[]
for _ in range(0,length1):
    element=input().strip().split()
    element=[int(elem) for elem in element]
    array.append(element)

counter=0
find_connected_cells(array,length1,length2)
