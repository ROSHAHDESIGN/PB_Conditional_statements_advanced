exam_hour = int(input())
exam_minute = int(input())

arrival_hour = int(input())
arrival_minute = int(input())

#matematica
time_of_exam = exam_hour * 60 + exam_minute
time_of_arrival = arrival_hour * 60 + arrival_minute

#MINUTITE koito ostavat kato razlika
difference = time_of_arrival - time_of_exam

if difference > 0:
    print("Late")
    if difference < 60:
        print(f"{difference} minutes after the start")
    else:
        hours = difference // 60
        minutes = difference % 60
        print(f"{hours}:{minutes:02d} hours after the start" )
elif difference == 0:
    print("On time")
elif difference >= -30:
    print("On time")
    print(f"{abs(difference)} minutes before the start")
else:
    print("Early")
    if difference <= -60:
        hours = -difference // 60
        minutes = -difference % 60
        print(f"{hours}:{minutes:02d} hours before the start")
    else:
        print(f"{-difference} minutes before the start")
