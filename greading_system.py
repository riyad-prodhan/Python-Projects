
class student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

        self.mark = {
            'Innovation & Entrepreneurship': 0,
            'Digital Marketing Technique': 0,
            'Network Administration & Services': 0,
            'Cyber Security & Ethics': 0,
            'Apps Development Project': 0,
            'Multimedia & Animation': 0,
            'Project Work-II': 0,
        }

        self.avg_mark = 0

    def add_mark(self, subject, mark):
        if subject in self.mark and 0 <= mark <= 100:
            self.mark[subject] = mark
        else:
            print('Enter valid subject or mark')

    def calculate_average(self):
        total = sum(self.mark.values())
        self.avg_mark = total / len(self.mark)
        return self.avg_mark

    def calculate_grade(self):
        if self.avg_mark >= 80:
            return 'A+'
        elif self.avg_mark >= 70:
            return 'A'
        elif self.avg_mark >= 60:
            return 'A-'
        elif self.avg_mark >= 50:
            return 'B'
        elif self.avg_mark >= 40:
            return 'C'
        elif self.avg_mark >= 33:
            return 'D'
        else:
            return 'Fail'

    def display_report(self):
        print('Name:', self.name)
        print('Roll:', self.roll)

        print('\nSubject Marks:')
        for subject, mark in self.mark.items():
            print(subject, ':', mark)

        print('Average:', self.avg_mark)
        print('Grade:', self.calculate_grade())


students = student('Riyad', 716381)

students.add_mark('Innovation & Entrepreneurship', 85)
students.add_mark('Digital Marketing Technique', 75)
students.add_mark('Network Administration & Services', 80)
students.add_mark('Cyber Security & Ethics', 90)
students.add_mark('Apps Development Project', 70)
students.add_mark('Multimedia & Animation', 65)
students.add_mark('Project Work-II', 85)

students.calculate_average()
students.display_report()
