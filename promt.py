from g4f.client import Client
predmet = input("Предмет? ")
tema = input("Тема? ")
varianti = input("Сколько вариантов? ")
skolko = input("Сколько задач в каждом варианте? ")
client = Client()
prompt = (f"Сгенерируй {varianti} варианта заданий по предмету {predmet}. "
          f"Каждый вариант должен содержать {skolko} задач по теме '{tema}'. "
          f"Задания должны быть написаны в стандартном формате, например: x^2 - 5x + 6 = 0. "
          f"Обеспечь разнообразие вопросов и тематики, соответствующей введённой теме {tema}. "
          f"Формат ответа: Вариант 1:\n1. Задание 1\n2. Задание 2\n... "
          f"Вариант 2:\n1. Задание 1\n2. Задание 2\n...")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
)
content = response.choices[0].message.content
print(content)