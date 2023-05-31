# import datetime

# def solution(n, t, m, timetable):
#     # timetable 순서대로 정렬
#     timetable.sort()
#     table = timetable[:]
        
#     curTime = datetime.datetime.strptime("09:00", "%H:%M")

#     # 태운 손님 확인을 위한 인덱스
#     index = 0

#     # 마지막으로 태운 손님 시간
#     lastPass = [datetime.datetime.strptime("00:00", "%H:%M"), datetime.datetime.strptime("00:00", "%H:%M")]
    
#     some = 0
    
#     # 순회
#     for i in range(n):
#         some = 0
#         many = 0
#         print(f"table : {table}")
#         # 줄 서있는 크루 확인
#         for j, crew in enumerate(table):
#             if j >= m:
#                 break
#             waitTime = datetime.datetime.strptime(crew, "%H:%M")
            
#             print(f"waitTime : {waitTime}")
#             print(f"curTime : {curTime}")
#             # 줄 선 시간이 현재 시간보다 크다면 for문 탈출
#             if waitTime > curTime:
#                 break
#             # 아니라면 태우고감
#             print("ride")
#             index+=1
#             many+=1
#             lastPass[0] = lastPass[1]
#             lastPass[1] = waitTime
#             some+=0
            
#         for j in range(many):
#             table.pop(0)
            
            
#         if t == 60:
#             temp=datetime.datetime.strptime("1", "%H")
#             curTime = curTime + datetime.timedelta(hours=temp.hour)
#             continue
#         temp=datetime.datetime.strptime(str(t), "%M")
#         curTime = curTime + datetime.timedelta(minutes=temp.minute)
        
        
#     print(lastPass)
#     # print(curTime)
    
#     # 경우를 나눌 수 있는 요소 : 줄 선 시간, 줄 선 인원
    
#     # 한명도 못타는 경우 curTime을 리턴한다.
#     if lastPass[1] == datetime.datetime.strptime("00:00", "%H:%M"):
        
#         if t == 60:
#             curTime = curTime + datetime.timedelta(hours=-1)
#         else :
#             curTime = curTime + datetime.timedelta(minutes=-t)
#         return curTime.strftime("%H:%M")
    
    
    
    
#     # 마지막 사람의 줄 선 시간이 9시보다 빠를때
#     if lastPass[1] < datetime.datetime.strptime("09:00", "%H:%M"):
#         ## timetable의 lnegth가 m보다 크거나 같으면 timetable의 m-1번째 요소의 사람 뒤에 서면 된다.
#         if index >= m:
#             print('why')
#             # 마지막 줄 선 사람과 그 앞사람의 시간이 같으면 1분 빠르게 서면 된다.
#             if lastPass[0] == lastPass[1]:
#                 dt = lastPass[1] + datetime.timedelta(minutes=-1)
#                 return dt.strftime("%H:%M")
#             dt = curTime + datetime.timedelta(minutes=-1)
#             # return dt.strftime("%H:%M")
#             return timetable[m-2]
#         ## timetable의 length가 m보다 작으면 그냥 09시에 서면 된다.
#         print('what')
#         return "09:00"
    
#     # 만약에 some이 m으로 나뉘어지지 않는다면, 맨마지막 사람 뒤에 서면 된다.
#     if some%m != 0:
#         print(f"index : {index}")
#         return lastPass[1].strftime("%H:%M")
    

#     # 만약 some이 m으로 나뉘어 떨어질 때, 맨 뒷사람과 그 앞사람의 도착시간이 같다면 나는 1분더 일찍와야된다.
#     if (lastPass[0] == lastPass[1]):
#         print("hi")
#         dt = lastPass[0] + datetime.timedelta(minutes=-1)
#         return dt.strftime("%H:%M")
    
    
#     # 만약 some이 m으로 나뉘어지면, 맨마지막 사람보다 1분 일찍 뒤에 서면 된다.
#     print("hello")
#     df = lastPass[1] + datetime.timedelta(minutes=-1)
#     return df.strftime("%H:%M")

import datetime as dt

def solution(n, t, m, timetable):
    timetable.sort()
    
    arrive = dt.datetime.strptime("09:00", "%H:%M")
    print(arrive)
    
    isEmpty = True
    # 도착시간, 대기시간, 인원수
    
    lastPerson = dt.datetime.strptime("00:00", "%H:%M")
    index = 0
    for i in range(n):
        count = 0
        print(f"{i+1}번째 버스")
        print(f"index : {index}")
        for j, crew in enumerate(timetable[index:]):
            
            waitTime = dt.datetime.strptime(crew, "%H:%M")
            
            if arrive < waitTime:
                break
            index+=1
            print(f"waitTime : {waitTime}")
            lastPerson = waitTime
            count+=1
            # 마지막 버스의 자리가 다 찬 경우
            if i+1 == n and count >= m:
                isEmpty = False
                break
            
            if count >= m:
                break
                
        if i+1 == n:
            break
        
        if t == 60:
            arrive = arrive + dt.timedelta(hours=1)
            continue
        arrive = arrive + dt.timedelta(minutes=t)

    print(f"isEmpty : {isEmpty}")
    print(f"lastPerson : {lastPerson}")
                
    # 마지막 버스가 빈 경우
    if isEmpty == True:
        # 마지막 크루가 9시 이전에 도착한 경우
        print(f"hour : {lastPerson.hour}")
        if lastPerson.hour < 9:
            print('hi')
            return arrive.strftime("%H:%M")
        print('hello')
        # res = arrive + dt.timedelta(minutes=-1)
        return arrive.strftime("%H:%M")
    
    # 버스가 꽉 찬 경우
    # 마지막 사람이 9시 이전에 도착한 경우
    # if lastPerson.hour < 9:
    res = lastPerson + dt.timedelta(minutes=-1)
    return res.strftime("%H:%M")
    