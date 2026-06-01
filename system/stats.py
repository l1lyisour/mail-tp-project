class ReportGenerator:
    def __init__(self):
        self.stats = {}

    def add(self, category, is_urgent):
        if category not in self.stats:
            self.stats[category] = {'total': 0, 'urgent': 0}
        self.stats[category]['total'] += 1
        if is_urgent:
            self.stats[category]['urgent'] += 1

    def generate(self):
        summ_letters = sum(data['total'] for data in self.stats.values())
        report_lines = []
        report_lines.append('Отчёт обработки почты')
        for category, data in self.stats.items():
            if category == 'unknown':
                report_lines.append(f"{category}: {data['total']} писем")
            else:
                report_lines.append(f"{category}: {data['total']} писем, {data['urgent']} срочных")
        report_lines.append(f'Итого: {summ_letters} писем')
        for line in report_lines:
            print(line)
        with open('stats.txt', 'w', encoding = 'utf-8') as f:
            for line in report_lines:
                f.write(line + '\n')
