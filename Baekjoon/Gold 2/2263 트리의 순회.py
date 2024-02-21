# pypy 통과, python3 시간 초과
# 참조: https://white-board.tistory.com/129

#----------------------------------------------------------------------------------------------------
# 틀린 코드: 시간 초과
# import sys; input=sys.stdin.readline
# sys.setrecursionlimit(10**8)

# class Node:
#     def __init__(self,value=None):
#         self.value=value
#         self.left=None
#         self.right=None

# def build_tree(inorder,postorder,p_idx,i_start,i_end):
#     if i_start<=i_end:
#         node=Node(postorder[p_idx[0]])
#         root_idx=inorder.index(postorder[p_idx[0]])
#         p_idx[0]-=1

#         node.right=build_tree(inorder,postorder,p_idx,root_idx+1,i_end)
#         node.left=build_tree(inorder,postorder,p_idx,i_start,root_idx-1)
#         return node

# def preorder(node):
#     if node:
#         print(node.value,end=' ')
#         preorder(node.left)
#         preorder(node.right)

# def main():
#     n=int(input())
#     inorder=list(map(int,input().split()))
#     postorder=list(map(int,input().split()))

#     p_idx=[n-1]
#     node=build_tree(inorder,postorder,p_idx,0,n-1)
#     preorder(node)

# if __name__=='__main__':
#     main()
#----------------------------------------------------------------------------------------------------

import sys; input=sys.stdin.readline
sys.setrecursionlimit(10**5)   # 10**6 부터 메모리 초과 발생

class Node:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None

def build_tree(inorder,postorder,p_idx,i_start,i_end):
    if i_start<=i_end:
        node=Node(postorder[p_idx[0]])
        root_idx=search_index(inorder,i_start,i_end,postorder[p_idx[0]])
        p_idx[0]-=1

        node.right=build_tree(inorder,postorder,p_idx,root_idx+1,i_end)
        node.left=build_tree(inorder,postorder,p_idx,i_start,root_idx-1)
        return node

def search_index(inorder,start,end,target):    # inorder.index가 있는 build_tree의 시간복잡도는 O(n^2)이므로, inorder.index를 search_index 함수로 대체하여 O(nlogn)을 만들었다.
    for i in range(start,end+1):
        if inorder[i]==target:
            return i
    
def preorder(node):
    if node:
        print(node.value,end=' ')
        preorder(node.left)
        preorder(node.right)

def main():
    n=int(input())
    inorder=list(map(int,input().split()))
    postorder=list(map(int,input().split()))

    p_idx=[n-1]
    node=build_tree(inorder,postorder,p_idx,0,n-1)
    preorder(node)

if __name__=='__main__':
    main()
