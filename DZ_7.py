def longest_words(file):
    myfile = open(file, mode='r', encoding='utf-8')
    maximum = 0
    maximing = str()
    for line in myfile:
        a = [str(x) for x in line.split()]
        for x in a:
            if len(x) > maximum:
                maximum = len(x)
                maximing = x
            else:
                continue
    return maximing
# print(longest_words(file1))


file1 = input('Vvedite nazvanie buducshego faila: ')
outputfile = open(file1 + '.txt', mode='w', encoding='utf-8')
kolvo = int(input('vvedite kol-vo strok: '))
for i in range(kolvo):
    x = input()
    outputfile.write(f'{x}\n')
