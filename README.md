# Персональний помічник 
Технiчний опис проєкту
Основний функцiонал

“Персональний помічник” вміє:

1. Зберігати контакти з іменами, адресами, номерами телефонів, email та днями народження до книги контактів. 
2. Виводити список контактів, у яких день народження через задану кількість днів від поточної дати. 
3. Перевіряти правильність введеного номера телефону та email під час створення або редагування запису та повідомляти користувача у разі некоректного введення. 
4. Здійснювати пошук контактів серед контактів книги. 
5. Редагувати та видаляти записи з книги контактів. 
6. Зберігати нотатки з текстовою інформацією. 
7. Проводити пошук за нотатками. Редагувати та видаляти нотатки.
8. Додавати в нотатки "теги", ключові слова, що описують тему та предмет запису; 
9. Здійснювати пошук та сортування нотаток за ключовими словами (тегами); 

------------------------------------------------------------------------------------------------------
# Щоб встановити наш додаток потрібно
1. Створити та активуйвати віртуальне середовище:
py -m venv venv
source venv/bin/activate  # для Unix або MacOS
.\venv\Scripts\activate  # для Windows
2. Встановіть проект:
pip install .
3. Команда notebook буде доступна для запуску вашого додатку з командного рядка.

------------------------------------------------------------------------------------------------------
# Це команди для консольного спілкування з помічником:
Command Functions:

hello exit close

Adding Contacts:

add John 1234567890 1234ElmSt john@example.com 05.12.1985

add Jeine 1515151515 1987ArreySt jaine@example.com 15.02.1984

add Simon 6564987854 2568MorsSt simon@example.com 08.09.1991

Changing Phone Numbers change John 0987654321

Viewing Phone Numbers phone John

Showing All Contacts all

Birthday Management

Show or change Birthday birthday John 12.05.1990

Listing Upcoming Birthdays birthdays 5

Deleting Contacts delete John

Note Management Adding Notes

add_note Meeting "Discuss project goals" add_note Meeting "Meeting with John"

Finding Notes find_note Meeting

show_notes

Editing Notes edit_note Meeting "Discuss project objectives"

Adding Tags to Notes add_tag Meeting project

Searching Notes by Tags search_by_tag project

Deleting Notes delete_note Meeting

exit close