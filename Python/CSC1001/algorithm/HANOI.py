def hanoi(from_rod, to_rod, help_rod, n):
    if n==1:
        print("move from",from_rod,"to",to_rod)
    else:
        hanoi(from_rod, help_rod, to_rod, n-1)
        print("move from",from_rod,"to",to_rod)
        hanoi(help_rod, to_rod, from_rod, n-1)
hanoi('left', 'middle', 'right', 5)
