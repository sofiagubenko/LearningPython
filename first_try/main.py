'''
Приймає від користувача довільне текстове повідомлення (мінімум 4 слова),
аналізує його, витягує ключові слова, формує з них структуру,
та виводить статистику: кількість слів, найдовше слово, скільки слів містять певну літеру,
будує словник зі словами та їх довжинами,
формує список унікальних слів у зворотному порядку, з великої літери.
Усі операції відбуваються у пам’яті — жодного файлу.
Користувач не знає, що програма робить всередині — вона просто «розумна».
'''


Sentence = input("Enter any sentence(at least 4 words): ")
Sentence = Sentence.split()

LongestWord = Sentence[0]
for i in range(len(Sentence)):
    if len(Sentence[i]) > len(LongestWord):
        LongestWord = Sentence[i]

print('General statistics:',
      'sentence lengh -', len(Sentence),
      'longesr word -', LongestWord )

lenOfWordsDictionary = {}
for i in range(len(Sentence)):
    lenOfWordsDictionary[Sentence[i]] = len(Sentence[i])

print("Here you can see the number of letter in each word:",
      lenOfWordsDictionary)

unicWords = set(Sentence)
unicWords = list(unicWords)[::-1]
for i in range(len(unicWords)):
    unicWords[i] = unicWords[i].capitalize()

print("Here you can see the list of unic words in another order:",
      unicWords)







