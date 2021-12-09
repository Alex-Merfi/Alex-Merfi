# Починаємо з користувачів ,які нам потрібні перевірити,
unconfirmed_user=['mark','rob','bill','will','alice','mark','mike','den','jon','kristi','megan']
# та создаем словник в який на потрібно додати людей
confirmed_users=[]
# Необхідно перевірити людей поки вони не закінчились
# Потрібно переносити кожного перевіроного до списку пітверджені
while unconfirmed_user:
#за допомогою pop() ми вилучаєм зі списку людей,
# можно вилучати окремо людей за допомогую додавання індиксу pop(0)
    current_user=unconfirmed_user.pop()
# виводимо перевірених людей
    print(f"Verefing user:{current_user.title()}")
#далі проходимся по списку
    confirmed_users.append(current_user)
# Показуємо підтверджених людей
print("\nThe following users confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
