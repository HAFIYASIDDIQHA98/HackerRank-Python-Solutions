n = int(input().strip())
if n % 2 != 0:
    # Rule 1: Agar Odd hai
    print("Weird")
else:
    # Rule 2: Agar Even hai
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
