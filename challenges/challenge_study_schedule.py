def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    if any(type(period) != tuple or type(period[0]) != int or type(period[1]) != int for period in permanence_period):
        return None

    quantity = 0
    for start, end in permanence_period:
        if start <= target_time <= end:
            quantity += 1

    return quantity