dict = {
    '00111101': "Абдулов Илья Александрович",
    '10001011': "Авокадо Ева Сергеевна",
    '11010111': "Адрат Олеся Александровна",
    '00000101': "Алексеев Тимофей Юрьевич",
    '00010111': "Бабаев Руслан",
    '00110001': "Белисов Глеб",
    '11101001': "Боженко Мария Александровна",
    '00010001': "Горлов Игорь" ,	
    '01111110': "Затикян Сергей Арменович",	
    '00111100': "Кабдулвахитов Эмир Ержанович",
    '11100010': "Касьяненко Вера Михайловна",
    '00110101': "Комелин Глеб Александрович",
    '01101100': "Конопля Алексей Константинович",	
    '10011000': "Кремпольская Екатерина Александровна",
    '00011110': "Миляев Дмитрий Дмитриевич",
    '11111000': "Надери Мариам Шаховна",	
    '01010110': "Оншин Дмитрий Николаевич",
    '11011110': "Петрова Наталья Глебовна",
    '10000000': "Садовая Анастасия Романовна",
    '00110000': "Смирнов Игорь Иванович",
    '00010100': "Телунц Эдуард Рубенович",	
    '01110100': "Царёв Александр Сергеевич" ,
    '11101000': "Шаллиева Вера Владимировна",
    '00111110': "Шестаков Максим Олегович",	
    '01110110': "Шишминцев Дмитрий Владимирович",	
    '01100100': "Язев Григорий",
}
arr  = [
    'Этот человек женского пола? (1/0) ',
    'Этот человек из СПб? (1/0) ',
    'Практику по линалу ведет Тушавин? (1/0) ',
    'Ему 18 лет? (1/0) ',
    'Он носит очки? (1/0) ',
    'Рост выше 175см? (1/0) ',
    'Есть вторая половинка? (1/0) ',
    'Что бы он выбрал 1 или 0? (1/0) '
]
str = ''
for i in arr:
    str += input(i)
if str in dict.keys():
    print(f'Это - {dict[str]}')
else:
    print('Такого челвека нет у нас в группе(')
