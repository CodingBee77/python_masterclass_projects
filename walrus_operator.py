import time

data = [54, 45, 87, 3, 2, 1, 4, 6, 45, 23, 78, 995, 443]


def count_odds(data: list) -> int:
    odds = [o for o in data if o % 2 == 1]
    return len(odds)


t1 = time.time()
if count_odds(data) > 1:
    print(f'{count_odds(data)} odds')
t2 = time.time()
print(f"Took {t2 - t1} seconds.")  # Took 9.775161743164062e-05 seconds.

# Using walrus operator
t1 = time.time()
if (n := count_odds(data)) > 1:
    print(f'{n} odds')
t2 = time.time()
print(f"Took {t2 - t1} seconds.")  # Took 3.0994415283203125e-05 seconds.
