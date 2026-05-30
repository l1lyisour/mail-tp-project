class Email:
    def __init__(self, name, content, theme, path, is_urgent=False, attachments=None):
        self.name = name
        self.content = content
        self.theme = theme
        self.path = path
        self.is_urgent = is_urgent
        self.attachments = attachments or []

    def __str__(self):
        urgent = "срочное" if self.is_urgent else "обычное"
        attach = f", вложения: {', '.join(self.attachments)}" if self.attachments else ""
        return f"Письмо от: {self.name}, тема: {self.theme}, важность: {urgent}{attach}"

    

    