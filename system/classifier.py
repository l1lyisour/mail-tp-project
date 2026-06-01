class Classifier:
    def __init__(self):
        self.keywords = {
            "security": ["взлом", "утечка", "безопасность", "вирус", "подозрительный"],
            "spam": ["реклама", "акция", "скидка", "рассылка", "отписаться", "выигрыш", "выиграли"],
            "technical": ["браузер", "зависает", "висит", "падает", "ошибка", "недоступен", "диагностика", "сервис", "monitoring"],
            "finance": ["оплата", "договор", "счёт", "финансы"],
            "documents": ["согласование", "отчёт", "проверка", "документы"],
            "access": ["доступ", "инструкция", "пароль"],
            "aho": ["гарнитура", "оборудование", "мебель", "заявка"],
            "hr": ["отпуск", "больничный", "кадры"],
            "events": ["приглашение", "мероприятие", "корпоратив", "тренинг", "созвон"] 
        }

    def classify(self, email):
        text = email.theme + " " + email.content
        text = text.lower()
        if "urgent" in text or "срочно" in text or "критично" in text:
            email.is_urgent = True
        for category, words in self.keywords.items():
            for w in words:
                if w in text:
                    return category
        return "unknown"