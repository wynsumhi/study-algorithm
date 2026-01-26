A, B = map(int, input().split())

sequence = []
num = 1

while len(sequence) < B:
    for _ in range(num):
        sequence.append(num)
        if len(sequence) >= B:
            break
    num += 1

result = sum(sequence[A-1:B])
print(result)