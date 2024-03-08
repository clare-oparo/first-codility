def solution(A, B):
    # Convert time strings into hours and minutes
    start_hour, start_minute = map(int, A.split(':'))
    end_hour, end_minute = map(int, B.split(':'))

    # Calculate the total duration
    duration = (end_hour - start_hour) * 60 + (end_minute - start_minute)

    # If end time is earlier than start time, add 24 hours (1440 minutes)
    if duration < 0:
        duration += 1440

    # Calculate the number of full rounds
    full_rounds = duration // 15
    

    return full_rounds