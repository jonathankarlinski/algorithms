def study_schedule(presence_periods, target_time):
    if target_time is None:
        return None
    students = 0

    for time in target_time:
        quantity = 0
        for period in presence_periods:
            if period[0] <= time < period[1]:
                quantity += 1
        if quantity > students:
            students = quantity

    return students