"""."""
import random
import prettify
from itertools import zip_longest


class PairGenerator:
    """Generator that produces pairs."""

    def __init__(self, *args, **kwargs):
        self.students = ['Stephen Koch',
                         'Anastasia Lebedeva',
                         'Ting Luo',
                         'Leandro Rodriguez',
                         'Christopher Stanley',
                         'James Bond',
                         'Christopher Ceder',
                         'Ethan Davis',
                         'Raven Delaney',
                         'Terrell Douglas',
                         'Amy Evans',
                         'Charles Glass',
                         'Joseph Hangarter',
                         'Sharmarke Ibrahim',
                         'Aaron Imbrock',
                         'Alvian Joseph',
                         'Travis',
                         ]
        self.recent_pairs = []
        self.final_pairs = []

        while len(self.recent_pairs) >= 11:
            del self.recent_pairs[0]
        self.create(self.students)
        return super().__init__(*args, **kwargs)

    # def pairs_with_fillin(self, students, size,  fillin='TA'):
    #     """Pairing function that adds a fillin value."""

    #     random.shuffle(students)
    #     student_list = self.students

    #     for first_student, second_student in self.pairs(student_list, 2, 'TA'):
    #         print(str(first_student), "and", str(second_student))

    def shuffle(self, student_list):
        """Shuffle students."""

        random.shuffle(student_list)
        return student_list

    def pairs(self, student_list, size=2):
        """Pairing function that is for an even amount of students."""

        it = iter(student_list)
        thing = zip_longest(*[it] * size)

        pairs = [i for i in thing]
        return pairs

    def create(self, student_list):
        """Start the input process to choose which function to use."""
        length = len(student_list)
        print(length)
        # user_input = input('Option 1: Pairs with fillin or 2: Regular pairs?')
        # if user_input == '1':
        if length / 2 != 0:
            count = 0
            students_absent = input('Enter abesnt, seperate with comma: ')
            students_absent = students_absent.split(',')
            student_list = [student.lower() for student in student_list]
            for absent in students_absent:
                count += 1
                for student in student_list:
                    if absent.lower() in student.lower():
                        student_list.remove(student)
                        student_list.append(f'ta{count}')

            assignemt_input = input('Todays assignment: Option 1: Lab or option 2: Whiteboard?')
            while assignemt_input not in ['1', '2']:
                assignemt_input = input('Todays assignment: Option 1: Lab or option 2: Whiteboard?')
            if assignemt_input.lower() == '1':
                last_pick = (self.shuffle(student_list).pop(),)
                pairs = self.pairs([student.title() for student in student_list])
                shuffled_pairs = self.shuffle(pairs)
                shuffled_pairs[-1] = shuffled_pairs[-1] + last_pick
            elif assignemt_input.lower() == '2':
                pairs = self.pairs([student.title() for student in student_list])

        else:
            pairs = self.pairs(student_list)

        self.recent_check(pairs)

    def recent_check(self, pairs):
        """Check recent pair list."""

        student_count = 0
        for pair in pairs:
            student_count += 2
            if pair not in self.recent_pairs:
                self.recent_pairs.append(pair)
                self.final_pairs.append(pair)

        print(prettify.make_pretty(pairs))


PairGenerator()
