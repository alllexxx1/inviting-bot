GREETING_MESSAGE = """
Добро пожаловать на бесплатный мини-курс «Магический экспресс»! 🚂

Наш поезд отправляется совсем скоро, и впереди — потрясающее путешествие:
❣️ Знакомства с новыми людьми.
❣️ Создание вашего уникального продукта.
❣️ Погружение в магию продаж.

📌 Для участия подпишитесь на эти каналы:
1️⃣ <a href="https://t.me/+fBrd8A2speIxNDdi">Канал Марии</a>
2️⃣ <a href="https://t.me/+dGXcKhTD4U1iODYy">Канал Екатерины</a>

Если вы готовы, но что-то непонятно — напишите сюда: @mgolichenko_support
"""

REMINDER = """
🚂 Поезд скоро отправляется! Не упустите возможность присоединиться к «Магическому экспрессу».

Осталось сделать последний шаг — выполните условие, чтобы занять своё место. 

⚡ Всё просто: вернитесь в бот и завершите этап. Мы уже ждём вас! Поторопитесь, чтобы не остаться на перроне! 

Если вдруг что-то непонятно, напишите в поддержку: @mgolichenko_support
"""

WAIT_FOR_SCREENSHOT_MESSAGE = """
Отлично, вы на верном пути! ✨

Теперь осталось всего одно действие, чтобы сесть на «Магический экспресс»:
1️⃣ Расскажите в любой соцсети, что идёте на бесплатный мини-курс. Поделитесь, что ждёте от курса или почему решили присоединиться. В посте оставьте ссылку на этого бота: ..., так болшее количество людей сможет отправиться в путшествие и получить пользу. 
2️⃣ Пришлите скриншот вашего поста сюда.

💡 Пример текста:
«Я иду на бесплатный мини-курс «Магический экспресс»! 🚂 Это про нетворкинг, создание продуктов и продажи. Кто со мной? (ссылка на курс)».

Как только мы всё проверим, вы получите ваш билет! 🎟️
"""

NOT_SUBSCRIBED_MESSAGE = """
Кажется, вы пропустили важный шаг. 🙈 Чтобы продолжить, нужно подписаться на оба канала:
1️⃣ <a href="https://t.me/+fBrd8A2speIxNDdi">Канал Марии</a>
2️⃣ <a href="https://t.me/+dGXcKhTD4U1iODYy">Канал Екатерины</a>

Без подписки мы не можем выдать вам билет на «Магический экспресс».

📌 Проверьте, всё ли выполнено, и нажмите кнопку «Я подписался(ась)»!

Если что-то не работает, пишите сюда: @mgolichenko_support
"""

BUTTON_IS_NOT_PRESSED_MESSAGE = """
Чтобы мы могли проверить выполнение условий, важно нажать кнопку «Подписался(ась)». 👇

📌 Если вы уже подписались, просто нажмите кнопку — это обязательный шаг для проверки.

Не забудьте, что только так вы сможете получить доступ к нашему курсу! 🚂

Если что-то пошло не так, напишите нам: @mgolichenko_support
"""

NOT_PICTURE_MESSAGE = """
Хм… Кажется, это не скриншот. 🙈

📌 Чтобы мы могли проверить выполнение условия, отправьте, пожалуйста, скриншот вашего поста.

Если вам нужна помощь, напишите в поддержку: @mgolichenko_support
Мы обязательно подскажем! ✨
"""

GENERIC_ERROR_MESSAGE = "Упс.. что-то пошло не так. Напишите нам: @mgolichenko_support"


def get_congratulation_message(ticket_number: str, link_to_the_closed_channel: str) -> str:
    congratulation_message = f"""
Поздравляем! 🎉 Вы получили ваш билет на «Магический экспресс»!

🎟️ Номер вашего билета: {ticket_number}
Сохраняйте его до конца поездки, он вам еще пригодится!

Наш поезд отправится совсем скоро! Чтобы занять своё место, сделайте следующее:
1️⃣ Перейдите по ссылке: {link_to_the_closed_channel} 
2️⃣ Присоединяйтесь к каналу и прочитайте закреплённое сообщение.

Мы уже ждём вас! 🚂
"""
    return congratulation_message
