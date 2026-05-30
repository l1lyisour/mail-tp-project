import os
import shutil
import logging

class MailHandler:
    def __init__(self, inbox_path, processed_path):
        self.inbox_path = inbox_path
        self.processed_path = processed_path
        self.classifier = Classifier()
        logging.basicConfig(
        filename="run.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s")

    def handle_all(self):
        for filename in os.listdir(self.inbox_path):
            filepath = os.path.join(self.inbox_path, filename)
            self.handle_one(filepath)

    def handle_one(self, filepath):
        with open(filepath, "r", encoding="utf-8") as source:
            raw_content = source.read()

        name = ""
        theme = ""
        content = ""
        for line in raw_content.split("\n"):
            if line.startswith("От кого:"):
                name = line.replace("От кого:", "").strip()
            elif line.startswith("Тема:"):
                theme = line.replace("Тема:", "").strip()
        
        parts = raw_content.split("\n\n", 1)
        if len(parts) > 1:
            content = parts[1].strip()

        email = Email(name=name, content=content, theme=theme, path=filepath)
        category = self.classifier.classify(email)

        destination = os.path.join(self.processed_path, category)
        shutil.move(filepath, destination)
        logging.info(str(email) + f"Категория: {category}")



