longest = 0
class TreeNode:
    def __init__(self):
        self.children=[]

def height(root):
    global longest
    heights= []
    for child in root.children:
        heights.append(height(child))
    
    if not heights:
        return 0    # 책에서 0이라는데 왜 0임?
    
    sorted(heights)
    if len(heights) > 1:
        longest = max(longest, 2 + heights[-1]+heights[-2])
    return heights[-1] + 1
    

def is_inside(parent, child):
    if ((x[parent]-x[child])**2 + (y[parent]-y[child])**2) < (r[parent]+r[child])**2 and r[parent] > r[child]:
        return True
    return False

def is_child(parent,child, n):
    if not is_inside(parent,child):
        return False
    
    for i in range(n):
        if i == parent or i == child:
            continue
        if is_inside(parent,i) and is_inside(i,child):
            return False
    return True

def make_tree(root, n):
    root_ptr = TreeNode()

    for i in range(n):
        if is_child(root,i, n):
            root_ptr.children.append(make_tree(i,n))
    return root_ptr

def solve(root):
    global longest
    longest = 0
    h = height(root)
    return max(h,longest)
        
for _ in range(int(input())):
    x , y, r = [], [], []

    for _ in range(int(input())):
        tempx , tempy, tempr = map(int,input().split())
        x.append(tempx)
        y.append(tempy)
        r.append(tempr)

    n = len(x)

    root = make_tree(0,n)

    print(solve(root))