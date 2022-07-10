n = int(input("Please enter a positive integer: "))
pp_list = [1] * n
direction = 1
for i in range(1, n):
    if i % 7 == 0 or str(i).find('7') != -1:
        direction = - direction
    pp_list[i] = pp_list[i - 1] + direction

print("The %sth element in ping-pong sequence is: %s" % (n, pp_list[-1]))
