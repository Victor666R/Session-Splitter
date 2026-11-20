def split_minutes(total_minutes, activity_count, break_minutes=5):
    if type(total_minutes) is not int or type(activity_count) is not int:
        raise ValueError("Use whole numbers for minutes and activities.")
    if total_minutes < 1 or activity_count < 1:
        raise ValueError("Choose at least one minute and one activity.")

    usable_minutes = total_minutes - break_minutes
    if usable_minutes < activity_count:
        raise ValueError("Not enough minutes left after the break.")

    base, extra = divmod(usable_minutes, activity_count)
    blocks = []

    for i in range(activity_count):
        if i < extra:
            blocks.append(base + 1)
        else:
            blocks.append(base)

    blocks.append(break_minutes)
    return blocks
