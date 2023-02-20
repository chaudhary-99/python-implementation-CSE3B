def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print("Move disk 1 from {} to {}".format(source, target))
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print("Move disk {} from {} to {}".format(n, source, target))
    tower_of_hanoi(n-1, auxiliary, source, target)

tower_of_hanoi(3, 'A', 'B', 'C')