from g4f.client import Client
import uuid


#vibor = input("Выбери 0 = математика, 1 = укр мова, 2 = Інформатика: ")
#varianti = лinput("Сколько нужно вариантов: ")
#skolko = input("Сколько будет вопросов: ")
#vopros = input("Напиши вопрос: ")

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
    model="gpt-4",
    messages=[{
        "role": "user",
        "content": ""
    }],
)

content = response.choices[0].message.content

print(content)  