string=input()
count=0
vij=0
for i in string.split():
    if i == "н":
        count+=1
    if count>vij:
        count=vij
    else:
        count=0
longest_str="н"*vij
mod=string.replace("н", "!")
count=string.count("н")
print(count)
print(mod)
print(longest_str)

#########################################################


input_string = "Пример строки (содержимое) для теста."
open_index = input_string.find('(')
close_index = input_string.find(')')
if open_index < close_index:
    inside_content = input_string[open_index + 1:close_index]
else:
    print("Скобки не найдены или расположены некорректно.")
print("Символы внутри скобок:", inside_content)

##########################################################################################

input_string = "Абстракция, авария, аллея, машина, земля, арка, зебра"
words = input_string.split()
result = []
for word in words:
    if word.lower()[:1] == "а" or word.lower()[-1:] == "я":
        result.append(word)
print("Подходящие слова:", result)



