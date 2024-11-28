
import re
f=str()
count_letters=re.search(r'[А-Яа-я]', f)
for i in count_letters:
    i+=1
    print(i)

##################################################################

import re
frint = "Уважаемый! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю. Еще одно время 23:59:59 и 10:30."


pattern = r"\d{2}:\d{2}:\d{2}|\d{2}:\d{2}"


new_frint = re.sub(pattern, "(TBD)", frint)

print(new_frint)
