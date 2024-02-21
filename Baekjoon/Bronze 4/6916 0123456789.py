# 틀린 코드
import sys; input = sys.stdin.readline

def main():
    n = int(input())
    if n == 0:
        print(' * * *')
        print('*     *')
        print('*     *')
        print('*     *')
        print('')
        print('*     *')
        print('*     *')
        print('*     *')
        print(' * * *')
    elif n == 1:
        print('      *')
        print('      *')
        print('      *')
        print('')
        print('      *')
        print('      *')
        print('      *')
    elif n == 2:
        print(' * * *')
        print('      *')
        print('      *')
        print('      *')
        print(' * * *')
        print('*')
        print('*')
        print('*')
        print(' * * *')
    elif n == 3:
        print(' * * *')
        print('      *')
        print('      *')
        print('      *')
        print(' * * *')
        print('      *')
        print('      *')
        print('      *')
        print(' * * *')
    elif n == 4:
        print('*     *')
        print('*     *')
        print('*     *')
        print(' * * *')
        print('      *')
        print('      *')
        print('      *')
    elif n == 5:
        print(' * * *')
        print('*')
        print('*')
        print('*')
        print(' * * *')
        print('      *')
        print('      *')
        print('      *')
        print(' * * *')
    elif n == 6:
        print(' * * *')
        print('*')
        print('*')
        print('*')
        print(' * * *')
        print('*     *')
        print('*     *')
        print('*     *')
        print(' * * *')
    elif n == 7:
        print(' * * *')
        print('      *')
        print('      *')
        print('      *')
        print('')
        print('      *')
        print('      *')
        print('      *')
    elif n == 8:
        print(' * * *')
        print('*     *')
        print('*     *')
        print('*     *')
        print(' * * *')
        print('*     *')
        print('*     *')
        print('*     *')
        print(' * * *')
    else:
        print(' * * *')
        print('*     *')
        print('*     *')
        print('*     *')
        print(' * * *')
        print('      *')
        print('      *')
        print('      *')
        print(' * * *')

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------
# 수정 코드: 질문 게시판 참고
import sys
input = sys.stdin.readline

n = int(input())
l = [
    """ * * *
*     *
*     *
*     *

*     *
*     *
*     *
 * * *""",
    """
      *
      *
      *

      *
      *
      *
""",
    """ * * *
      *
      *
      *
 * * *
*
*
*
 * * * """,
    """ * * *
      *
      *
      *
 * * *
      *
      *
      *
 * * *""",
    """
*     *
*     *
*     *
 * * *
      *
      *
      *
""",
    """ * * *
*
*
*
 * * *
      *
      *
      *
 * * *""",
    """ * * *
*
*
*
 * * *
*     *
*     *
*     *
 * * *""",
    """ * * *
      *
      *
      *

      *
      *
      *
""",
    """ * * *
*     *
*     *
*     *
 * * *
*     *
*     *
*     *
 * * *""",
    """ * * *
*     *
*     *
*     *
 * * *
      *
      *
      *
 * * *""",
]
print(l[n])
