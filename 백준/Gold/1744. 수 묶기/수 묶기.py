import sys

input = sys.stdin.readline


# 순서가 상관없음 -> 정렬

# 양수
# 홀수개면 -> 가장 작은 걸 더하면 되잖아요 그죠?
# 짝수개면 걍 싹다 순서대로 둘둘 묶어서 곱해버리면 된다.

# 음수
# 음수는 짝수개 곱해져야한다. -> 홀수개라면 가장 큰 수가 더해지는개 맞다.
# 음수가 홀수개인데 0이 있으면 0이랑 곱해지면 좋다.

# 0
# 0은 무조건 더해져야한다.
# 다만, 답이 음수가 나올 경우에는 0이 곱해지는게 좋다.


# 1, -1
# 1은 무조건 더해져야한다.
# -1은 짝수개라면 곱해지는게 맞다.
# 홀수개라면 계속 더하다가 곱하는게 맞다. -> 근데 두개씩만 묶을 수 있으니 더하면 안된다 -> 그냥 놔둬도된다.

def main():
    N = int(input())
    arr = sorted([int(input()) for _ in range(0,N)])

    answer = 0

    minus_len = -1
    isZero = False

    for i in range(0, len(arr)):
        if arr[i] == 0:
            isZero = True
            break

        if arr[i] > 0:
            break
        minus_len = i

    if len(arr) == 1:
        print(arr[0])
        return


    minus = arr[:minus_len+1] # minus_len이 -1경우 주의
    plus = []
    if isZero:
        plus = arr[minus_len+2:] # minus_len이 -1경우 주의. 0이 포함된 아이다.
    else:
        plus = arr[minus_len+1:]

    if len(minus) % 2 == 1:
        answer += minus.pop()
        if isZero == True: # 0이랑 곱해지기 때문에 0으로 초기화
            answer = 0

    for i in range(0, len(minus), 2):
        if len(minus) == 0:
            break
        # # 길이가 홀수인 경우
        # if i == len(minus)-1:
        #     break
        answer += minus[i] * minus[i+1]


    last_one_index = -1
    for i in range(0, len(plus)):
        if plus[i] == 1:
            last_one_index = i
            answer += 1
            continue
    plus = plus[last_one_index+1:]

    if len(plus) % 2 == 1:
        answer += plus.pop(0)

    for i in range(0, len(plus), 2):
        if len(plus) == 0:
            break
        answer += plus[i] * plus[i+1]    

    print(answer)

main()