def send_email(message: str, recipient: str, *, sender="university.help@gmail.com"):
    recipient = recipient
    sender = sender
    tuple_ends_with = (".com", ".ru", ".net")
    if len(sender.split("@")) < 2 or len(recipient.split("@")) < 2:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}>")
    elif not sender.endswith(tuple_ends_with) or not recipient.endswith(tuple_ends_with):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}>")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
