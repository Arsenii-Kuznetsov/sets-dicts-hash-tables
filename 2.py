authors_and_books = dict()
while True:
    add_author = input('Добавить имя автора в словарь(да, нет)? ')
    match add_author:
        case 'да':
            author = input('Введите имя автора: ')
            add_books = input('Введите названия книг этого автора через пробел: ')
            books = set(add_books.split())
            if author in authors_and_books.keys():
                authors_and_books[author] |= (books)
            else:
                authors_and_books[author] = books
        case 'нет':
            break
        case _:
            exit('Введены некорректные данные')
print(authors_and_books)
author = input('Введите имя автора, книги которого вы хотите найти: ')
print(authors_and_books.get(author, 'Имени такого автора нет в словаре'))
