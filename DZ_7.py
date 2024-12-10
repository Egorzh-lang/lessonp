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
####################################################


file1 = input('Vvedite nazvanie buducshego faila: ')
outputfile = open(file1 + '.txt', mode='w', encoding='utf-8')
kolvo = int(input('vvedite kol-vo strok: '))
for i in range(kolvo):
    x = input()
    outputfile.write(f'{x}\n')

################################################################3
def simple_text_editor():
    filename = input("Введите имя файла (без расширения): ")
    filename += ".txt" 
    with open(filename, 'w', encoding='utf-8') as file:
        print("Введите строки текста. Для сохранения файла введите пустую строку или строку со спец. символом.")
        while True:
            line = input() 
            if line == "!5" or line == "":
                print(f"Файл '{filename}' сохранен.")
                break
            file.write(line + '\n')  
simple_text_editor()
