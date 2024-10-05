from g4f.client import Client

predmet = input("Предмет? ")
klas = input("Класс? ")
varianti = input("Сколько вариантов? ")
skolko = input("Сколько задач в каждом варианте? ")
vopros = input("Тип задач? ")

client = Client()

prompt = (f"Предложи {varianti} разных примеров уравнений для {klas} класса по предмету {predmet}. "
          f"В каждом примере должно быть по {skolko} уравнений. "
          f"Тип уравнений похож на {vopros}, но числа в каждом примере должны быть разные. "
          f"Убедись, что формат уравнений одинаковый: с пробелами перед и после знаков '=', '+' и '-'. "
          f"Пример формата: '2х + 3 = 9'. Ответ должен быть структурирован по следующим правилам: "
          f"Вариант 1:\n1. Уравнение 1\n2. Уравнение 2\n... "
          f"Вариант 2:\n1. Уравнение 1\n2. Уравнение 2\n...")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
)

content = response.choices[0].message.content
print(content)
