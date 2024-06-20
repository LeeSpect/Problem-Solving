# 236,224 KB / 712 ms

import sys
from collections import defaultdict
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.root = {}
        self.name = defaultdict(lambda: 1)
    
    def insert(self, sentence):
        cur_node = self.root     # root부터 시작
        self.name[sentence] += 1 # 닉네임이 몇 번 나왔는지 확인
        for s in sentence:
            if s not in cur_node: # 없으면 추가
                cur_node[s] = {}  # 자식 노드 생성
            cur_node = cur_node[s]# 자식 노드로 이동
        cur_node[-1] = True       # 마지막 노드에 True 추가
        
    def search(self, sentence):
        cur_node = self.root
        ret = []                  # 닉네임을 저장할 리스트
        for s in sentence:
            ret.append(s)         # 한 글자씩 추가
            if s not in cur_node: # 없는 닉네임이면 break
                break
            cur_node = cur_node[s]# 자식 노드로 이동 
        name_cnt = self.name[sentence] # 닉네임이 몇 번 나왔는지 확인
        if len(sentence) == len(ret) and name_cnt > 1: # 닉네임이 1번 이상 나왔으면
            ret.append(str(name_cnt)) # 닉네임이 몇 번 나왔는지 추가
        return ''.join(ret)          # 닉네임 반환

trie = Trie()
for _ in range(int(input())):
    sentence = input().rstrip()
    print(trie.search(sentence))
    trie.insert(sentence)











N = int(input())
tree = defaultdict(list) # list를 해야 cur_tree로 ref 참조 가능
visited = defaultdict(int)
ans = []

for _ in range(N):
    print(ans)
    sentence = input().rstrip()
    if sentence in visited: # 이전에 확인한 닉네임이라면
        visited[sentence] += 1 # 1개 늘어남
        ans.append(sentence + str(visited[sentence]))
        continue
    visited[sentence] = 1 # 현재 1개 있음
    
    temp_for_ans = ''
    
    i = 0
    character_for_while = sentence[i]
    cur_tree = tree # 자식 tree들을 살펴볼 예정
    while 1:
        temp_for_ans += character_for_while
        if character_for_while in cur_tree: # 현재의 tree안에 문자 있으면 한 단계 더
            if i == len(sentence) - 1: # 한 단계를 더 들어갈 수 없는 마지막 단어였다면
                if not cur_tree[character_for_while][0]: # cur_tree가 []로, 빈 리스트일 때,
                    cur_tree[character_for_while][0] = 0
                else:
                    cur_tree[0] += 1
                    temp_for_ans += str(cur_tree[0])
                break
            i+=1
            character_for_while = sentence[i]
            cur_tree = cur_tree[character_for_while]
            continue
        cur_tree[character_for_while] = defaultdict(int)
        break
    ans.append(temp_for_ans)
        
for a in ans:
    print(a)

# tree['a'] = defaultdict(list)
# tree['a']['b'] = [0]

# temp_tree = tree['a']['b']
# temp_tree[0] += 1

# # temp_tree = tree['a']
# # temp_tree['b'] += 1

# print(tree)