from system.handler import MailHandler

def main():
    inbox_dir = 'inbox'
    processed_dir = 'processed'
    
    print('Начинаем обработку входящих писем.')

    handler = MailHandler(inbox_path=inbox_dir, processed_path=processed_dir)
    handler.handle_all()

if __name__ == '__main__':
    main()