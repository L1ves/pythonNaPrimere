import csv
"""Создайте файл .csv с данными, приведенными в следующей таблице. Назовите его Books.csv .

        Книга              Автор  Год выпуска
0 To Kill a Mockingbird Harper Lee 1960
1 A Brief History of Time Stephen Hawking 1988
2 The Great Gatsby F. Scott Fitzgerald 1922
3 The Man Who Mistook His Wife for a Hat Oliver Sacks 1985
4 Pride and Prejudice Jan Austen 1813
"""
file = open("Book.csv","w")
newrecord = "To Kill a Mockingbird, Harper Lee, 1960\n"
file.write(str(newrecord))
newrecord = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(newrecord))
newrecord = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(newrecord))
newrecord = "The Man Who Mistook His Wife for a Hat,  Oliver Sacks,  1985\n"
file.write(str(newrecord))
newrecord = "Pride and Prejudice, Jan Austen, 1813\n"
file.write(str(newrecord))

file.close()