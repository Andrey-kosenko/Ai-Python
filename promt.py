from g4f.client import Client
import os
import uuid

file_name = f"{uuid.uuid4()}.txt"

vibor = input("Выбери 0 = математика, 1 = укр мова, 2 = Інформатика: ")
varianti = input("Сколько нужно вариантов: ")
skolko = input("Сколько будет вопросов: ")
vopros = input("Напиши вопрос: ")

uchitel = ""
if vibor == '0':
    uchitel = "математики"
elif vibor == '1':
    uchitel = 'укр мова'
elif vibor == '2':
    uchitel = 'Інформатики'
else:
    print("Неверный ввод")
    exit()

client = Client()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": f"Представь что ты учетель по {uchitel}"
        f"И тебе надо зделать вопросы по теме {vopros} "
        f"Нужно будет зделать столько вариантов{varianti}"
        f"И нужно будет стлоько вопросов в одном варианте {skolko}"
        f"И еще каждий вариант не убольщает и не уменшает сложность"
        f"А только делает разные вопросы для избешания списования"
    }],
)

content = response.choices[0].message.content

print(content)  