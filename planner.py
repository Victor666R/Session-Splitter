"""Small, inspectable calculation for the Week 1 learning example."""


def split_minutes(total_minutes: int, activity_count: int) -> list[int]:
    """Divide whole minutes fairly; earlier activities receive the remainder."""
    if type(total_minutes) is not int or type(activity_count) is not int:
        raise ValueError("Use whole numbers for minutes and activities.")
    if total_minutes < 1 or activity_count < 1:
        raise ValueError("Choose at least one minute and one activity.")
    if activity_count > total_minutes:
        raise ValueError("Give each activity at least one minute, or choose fewer activities.")
    base, extra = divmod((total_minutes-5), activity_count)
    return list([base + (1 if index < extra else 0) for index in range(activity_count)])
