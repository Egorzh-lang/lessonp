text = input().split()
print(*filter(lambda x: x.startswith('а'), text))
print(*filter(lambda x: x.endswith('я'), text))
