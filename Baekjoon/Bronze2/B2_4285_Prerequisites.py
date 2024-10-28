# 109240 KB / 120 ms
import sys
input=sys.stdin.readline

while True:
    try:
        k, m = map(int, input().split())
        if k == 0:
            break  # k가 0이면 입력 종료
        
        selected_courses = set(map(int, input().split()))
        
        # 모든 카테고리를 만족하는지 여부를 확인하는 변수
        can_graduate = True
        for _ in range(m):
            category_info = list(map(int, input().split()))
            c = category_info[0]  # 카테고리에 포함된 과목 수
            r = category_info[1]  # 카테고리에서 필수적으로 들어야 하는 과목 수
            category_courses = set(category_info[2:])  # 카테고리에 포함된 과목들
            
            # 선택된 과목 중 카테고리에 포함된 과목 수를 계산
            if len(selected_courses & category_courses) < r:
                can_graduate = False  # 필수 과목 수를 충족하지 못하면 졸업 불가
        
        print("yes" if can_graduate else "no")
    
    except:
        break