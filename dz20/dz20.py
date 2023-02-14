#Напишите программу, удаляющую из текста все слова, содержащие ""абв""

def remove_words(text):
    words = text.split()
    result = []
    for word in words:
        if "абв" not in word:
            result.append(word)
    return " ".join(result)

text = input("Введите текст : ")
print("Полученный текст после удаления 'абв' :", remove_words(text))