"""Small, inspectable calculation for the Week 1 learning example."""


def split_minutes(
    total_minutes: int,
    activity_count: int,
    break_minutes: int = 5,
) -> list[tuple[str, int]]:
    """Divide whole minutes fairly; earlier activities receive the remainder, plus a break."""
    if (
        type(total_minutes) is not int
        or type(activity_count) is not int
        or type(break_minutes) is not int
    ):
        raise ValueError("Use whole numbers for minutes and activities.")
    if total_minutes < 1 or activity_count < 1 or break_minutes < 0:
        raise ValueError("Choose at least one minute and one activity.")

    usable_minutes = total_minutes - break_minutes
    if usable_minutes < activity_count:
        raise ValueError(
            "Not enough minutes left after the break to give each activity at least 1 minute."
        )

    base, extra = divmod(usable_minutes, activity_count)
    blocks: list[tuple[str, int]] = [
        (f"Activity {index + 1}", base + (1 if index < extra else 0))
        for index in range(activity_count)
    ]
    if break_minutes > 0:
        blocks.append(("Break", break_minutes))
    return blocks
