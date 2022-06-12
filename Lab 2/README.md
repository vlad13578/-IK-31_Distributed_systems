# **Лабораторна робота №2**

-----------------------------------
## Необхідні ресурси:
- Встановлений компілятор для Python.

## Інформація про програму:
- Виводить в терміналі "Hello World!".
- Виконує команди: ping, echo, login, list, msg, file, exit.

## Опис Команд:
### 1. Команда `ping <Address: String>`.
#### Ця команда перевіряє зєднання з сервером, сайтом чи будь-яким іншим пристроєм за вказаною IP або DNS адресою. Дані команді передається тільки один параметр - `<Address: String>`
#### Результатом виконання у разі успішного зєднання в першому рядку записується `Ping <Address: String> ...` і в наступному рядку `Ping <Address: String> request success.`.
#### Якщо ж кількість введених параметрів не буде рівна "1", то замість результату виводиться повідомлення з описом помилки в дужках`PING ERROR (Incorect input argument)`

### Приклад виконання команди:
```text
============ RESTART: C:\Users\13578\Desktop\РІКС\Git\Lab 2\Lab2.py ============
Hello World!
========================================
Input Command: ping
Entered command = "ping", parameters = []
----------------------------------------

Results:
PING ERROR (Incorect input argument)
========================================
Input Command: ping 192.168.0.13
Entered command = "ping", parameters = ['192.168.0.13']
----------------------------------------

Results:
Ping 192.168.0.13 ...
Ping 192.168.0.13 request success.
========================================
Input Command: ping google.com vns.lpnu.ua
Entered command = "ping", parameters = ['google.com', 'vns.lpnu.ua']
----------------------------------------

Results:
PING ERROR (Incorect input argument)
========================================
Input Command: ping vns.lpnu.ua
Entered command = "ping", parameters = ['vns.lpnu.ua']
----------------------------------------

Results:
Ping vns.lpnu.ua ...
Ping vns.lpnu.ua request success.
========================================
Input Command: 
```

### 2. Команда `echo <anyText: String> <anyText: String> ...`.
#### Ця команда виводить на екрані текст з вхідних параметрів - `<anyText: String>`. Ця команда може отримувати будь-яку кількість параметрів. Кожний параметр відображається в новому рядку.

### Приклад виконання команди:
```text
============ RESTART: C:\Users\13578\Desktop\РІКС\Git\Lab 2\Lab2.py ============
Hello World!
========================================
Input Command: echo 123
Entered command = "echo", parameters = ['123']
----------------------------------------

Results:
123
========================================
Input Command: echo hello std1
Entered command = "echo", parameters = ['hello', 'std1']
----------------------------------------

Results:
hello
std1
========================================
Input Command: echo "123"
Entered command = "echo", parameters = ['123']
----------------------------------------

Results:
123
========================================
Input Command: 
```

### 3. Команда `login <login: String> <password: String>`.
#### Ця команда дозволяє користувачу залогінитися. Дані команді передається два параметри - `<login: String>` і `<password: String>`.
#### Результатом виконання команди буде:
- Якщо логін даного користувача немає в базі даних, то в консолі виводиться `LOGIN ERROR (Incorect input login or password)`.
- Якщо логін даного користувача є в базі даних, але відповідний до нього пароль введений неправильно, то в консолі виводиться `LOGIN ERROR (Incorect input login or password)`.
- Якщо логін даного користувача є в базі даних, і відповідний до нього пароль введений правильно, то в першому рядку консолі виводиться - `LOGIN SUCCESS:`, а в наступному рядку - `Hello, <nameUsers: String>`.
- Якщо кількість введених параметрів не дорівнює 2, то в консолі виводиться `LOGIN ERROR (Incorect input argument)`.

### Приклад виконання команди:
```text
============ RESTART: C:\Users\13578\Desktop\РІКС\Git\Lab 2\Lab2.py ============
Hello World!
========================================
Input Command: login std_1 12601
Entered command = "login", parameters = ['std_1', '12601']
----------------------------------------

Results:
LOGIN SUCCESS:
 Hello, std1
========================================
Input Command: login std_1
Entered command = "login", parameters = ['std_1']
----------------------------------------

Results:
LOGIN ERROR (Incorect input argument)
========================================
Input Command: login std_5 12605
Entered command = "login", parameters = ['std_5', '12605']
----------------------------------------

Results:
LOGIN ERROR (Incorect input login or password)
========================================
Input Command: login std_1 12602
Entered command = "login", parameters = ['std_1', '12602']
----------------------------------------

Results:
LOGIN ERROR (Incorect input login or password)
========================================
Input Command:
```

### 4. Команда `list`.
#### Ця команда виводить на екран список назв всіх зареєстрованих користувачів які знаходяться в базі даних. Для цієї команди не потрібно вводити параметри, якщо було введено параметри то вони ігноруються. Назва кожного користувача відображається в новому рядку з його поряковим номером - `<№Users: Int>. <nameUsers: String>` .
#### База даних:
- user_names = `std1`, `std2`, `std3`, `std4`
- user_logins = `std_1`, `std_2`, `std_3`, `std_4`
- user_passwords = `12601`, `12602`, `12603`, `12604`

### Приклад виконання команди:
```text
============ RESTART: C:\Users\13578\Desktop\РІКС\Git\Lab 2\Lab2.py ============
Hello World!
========================================
Input Command: list
Entered command = "list", parameters = []
----------------------------------------

Results:
1. std1
2. std2
3. std3
4. std4
========================================
Input Command: 
```

### 5. Команда `msg <destinationUser: String> <text: String>`.
#### Ця команда надсилає текстове повідомлення іншому користувачу. Дані команді передається два параметри - `<destinationUser: String>` і ` <text: String>`.
#### Результатом виконання команди буде:
- Якщо назви даного користувача немає в базі даних, то в консолі виводиться `MESSAGE SENDING ERROR (This user not found)`.
- Якщо назва даного користувача є в базі даних, то в консолі виводиться `MESSAGE SENDING SUCCESS`.
- Якщо кількість введених параметрів не дорівнює 2, то в консолі виводиться `MESSAGE SENDING ERROR (Incorect input argument)`.

### Приклад виконання команди:
```text
============ RESTART: C:\Users\13578\Desktop\РІКС\Git\Lab 2\Lab2.py ============
Hello World!
========================================
Input Command: msg std1
Entered command = "msg", parameters = ['std1']
----------------------------------------

Results:
MESSAGE SENDING ERROR (Incorect input argument)
========================================
Input Command: msg std1 "111"
Entered command = "msg", parameters = ['std1', '111']
----------------------------------------

Results:
MESSAGE SENDING SUCCESS
========================================
Input Command: msg std5 "123"
Entered command = "msg", parameters = ['std5', '123']
----------------------------------------

Results:
MESSAGE SENDING ERROR (This user not found)
========================================
Input Command: 
```

### 6. Команда `file <destinationUser: String> <filename: String>`.
#### Ця команда надсилає файлове повідомлення іншому користувачу. Дані команді передається два параметри - `<destinationUser: String>` і ` <filename: String>`.
#### Результатом виконання команди буде:
- Якщо назви даного користувача немає в базі даних, то в консолі виводиться `FILE SENDING ERROR (User not found)`.
- Якщо назва даного користувача є в базі даних, але даного файлу немає, то в консолі виводиться `FILE SENDING ERROR (File not found)`.
- Якщо назва даного користувача є в базі даних, і цей файл існує, то в консолі виводиться `FILE SENDING SUCCESS`.
- Якщо кількість введених параметрів не дорівнює 2, то в консолі виводиться `FILE SENDING ERROR (Incorect input argument)`.

### Приклад виконання команди:
```text
============ RESTART: C:\Users\13578\Desktop\РІКС\Git\Lab 2\Lab2.py ============
Hello World!
========================================
Input Command: file std1 README.md
Entered command = "file", parameters = ['std1', 'README.md']
----------------------------------------

Results:
FILE SENDING SUCCESS
========================================
Input Command: file std2 lab10
Entered command = "file", parameters = ['std2', 'lab10']
----------------------------------------

Results:
FILE SENDING ERROR (File not found)
========================================
Input Command: file std5 README.md
Entered command = "file", parameters = ['std5', 'README.md']
----------------------------------------

Results:
FILE SENDING ERROR (User not found)
========================================
Input Command: 
```

### 7. Команда `exit`.
#### Ця команда виходить з циклу для опитування введення команд. Для цієї команди не потрібно вводити параметри, якщо було введено параметри то вони ігноруються.
- Результатом виконання команди буде - `Exit from cycle`

### Приклад виконання команди:
```text
============ RESTART: C:\Users\13578\Desktop\РІКС\Git\Lab 2\Lab2.py ============
Hello World!
========================================
Input Command: list
Entered command = "list", parameters = []
----------------------------------------

Results:
1. std1
2. std2
3. std3
4. std4
========================================
Input Command: exit
Entered command = "exit", parameters = []
----------------------------------------

Results:
Exit from cycle
```

### Примітка: щоб ввести текст в якому містяться символ " " потрібно використовувати адинарні або подвійні дужки в кінці і на початку тексту.
### Примітка: Якщо було некоректно введено команду або її не існує, то в консолі виводиться `No Command = "ddd"`.

### Приклад спроби виконання іншої команди:
```text
============ RESTART: C:\Users\13578\Desktop\РІКС\Git\Lab 2\Lab2.py ============
Hello World!
========================================
Input Command: ddd
Entered command = "ddd", parameters = []
----------------------------------------

Results:
No Command = "ddd"
========================================
Input Command: 
```
