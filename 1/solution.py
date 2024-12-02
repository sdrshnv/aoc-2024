left = []
right = []
with open('input.txt') as fin:
    for line in fin:
        n1, n2 = [int(n) for n in line.split()]
        left.append(n1)
        right.append(n2)

left.sort()
right.sort()
print(sum(abs(a - b) for a, b in zip(left, right)))
