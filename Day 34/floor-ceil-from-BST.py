
def ceil(root, inp):
     
    if root == None:
        return -1
  
    if root.key == inp :
        return root.key
     
   
    if root.key < inp:
        return ceil(root.right, inp)
     
   
    val = ceil(root.left, inp)
    return val if val >= inp else root.key


def floor(root, inp):

    if root == None:
        return -1
  
    if root.key == inp :
        return root.key
     
   
    if root.key > inp:
        return ceil(root.left, inp)
     
   
    val = ceil(root.right, inp)
    return val if val <= inp else root.key
