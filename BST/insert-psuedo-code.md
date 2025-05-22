Psuedo code 

##### we don't need the temp variable if root is pointing to None 
if root == None then root = new_node 
create new_node
temp = self.root

while loop
    if new_node == temp return False 
    if < left else > right
    if None insert new_node else move to next 


#### Modified Psuedo-Code 

```
Function insert(new_node):
    If root is None:
        root = new_node
        Return True

    temp = root

    While True:
        If new_node.value == temp.value:
            Return False  // Duplicate value

        Else if new_node.value < temp.value:
            If temp.left is None:
                temp.left = new_node
                Return True
            Else:
                temp = temp.left

        Else:  // new_node.value > temp.value
            If temp.right is None:
                temp.right = new_node
                Return True
            Else:
                temp = temp.right

```