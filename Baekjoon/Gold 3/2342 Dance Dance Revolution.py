import sys; input=sys.stdin.readline
import copy

def rolling(mini, new_mini, cases, new_cases, target, direction):
    for k in cases.keys():
        if mini + 4 < cases[k]:
            continue
        val = 0
        new_case = 0
        if direction == 'LEFT':
            if k[1] == target:
                continue
            if not k[0]:
                val = 2
            elif k[0] == target:
                val = 1
            elif abs(k[0] - target) == 2:
                val = 4
            else:
                val = 3
            new_case = (target, k[1])
        elif direction == 'RIGHT':
            if k[0] == target:
                continue
            if not k[1]:
                val = 2
            elif k[1] == target:
                val = 1
            elif abs(k[1] - target) == 2:
                val = 4
            else:
                val = 3
            new_case = (k[0], target)
        if (new_case not in new_cases) or (new_case in new_cases and val < new_cases[new_case]):
            new_mini = min(new_mini, cases[k] + val)
            if new_mini + 4 < cases[k] + val:
                continue
            if new_cases.get(new_case):
                new_cases[new_case] = min(cases[k]+val, new_cases[new_case])
            else:
	            new_cases[new_case] = cases[k] + val
    return new_mini

def main():
    DDR = list(map(int, input().split()))
    i = 0
    cases = {(0, 0):0}
    mini = 0
    while DDR[i]:
        new_mini = float('inf')
        new_cases = {}
        new_mini = rolling(mini, new_mini, cases, new_cases, DDR[i], 'LEFT')
        new_mini = rolling(mini, new_mini, cases, new_cases, DDR[i], 'RIGHT')
        mini = new_mini
        cases = copy.deepcopy(new_cases)
        i += 1
    print(mini)

if __name__=='__main__':
    main()
