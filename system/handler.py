import os
import shutil
import logging
from system.stats import ReportGenerator
from system.classifier import Classifier
from system.mail import Email

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
        stats = ReportGenerator()
        files = os.listdir(self.inbox_path)
        for filename in files:
            if filename.startswith("."):  
                continue
            filepath = os.path.join(self.inbox_path, filename)
            if os.path.isfile(filepath):
                self.handle_one(filepath, stats)
        stats.generate()
        return stats

    def handle_one(self, filepath, stats):
        try:
            with open(filepath, "r", encoding="utf-8") as source:
                raw_content = source.read()

            name = ""
            theme = ""
            content = ""
            sender_email = ""
            attachments = []

            for line in raw_content.split("\n"):
                if line.startswith("От кого:") or line.startswith("From:"):
                    value = line.replace("От кого:", "").replace("From:", "").strip()
                    if "<" in value and ">" in value:
                        name = value.split("<")[0].strip()
                        sender_email = value.split("<")[1].split(">")[0].strip()
                    else:
                        name = value
                        sender_email = ""
                elif line.startswith("Тема:") or line.startswith("Subject:"):
                    theme = line.replace("Тема:", "").replace("Subject:", "").strip()
            
                elif (
                    line.startswith("Прикрепил:")
                    or line.startswith("Файл:")
                    or line.startswith("Вложение:")
            ):
                    attachment = line.split(":", 1)[1].strip()
                    attachments.extend(
                        file.strip() for file in attachment.split(",")
                    )
            parts = raw_content.split("\n\n", 1)
            if len(parts) > 1:
                content = parts[1].strip()

            email = Email(name=name, content=content, theme=theme, path=filepath, attachments=attachments,sender_email=sender_email)
            category = self.classifier.classify(email)
            stats.add(category, email.is_urgent)

            destination = os.path.join(self.processed_path, category)
            shutil.move(filepath, destination)
            logging.info(str(email) + f"Категория: {category}")

        except UnicodeDecodeError:
            logging.warning(f'Не удалось прочитать файл: {filepath}')
            shutil.move(filepath, os.path.join(self.processed_path, 'unknown'))
            return 'unknown', False
        except FileNotFoundError:
            logging.error(f'Файл не найден: {filepath}')
            return None
        except Exception as e:
            logging.warning(f'Ошибка обработки {filepath}: {e}')
            return 'unknown', False



