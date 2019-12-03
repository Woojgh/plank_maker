"""."""
import random
import prettify

curr_students = ['Stephen Koch',
                 'Anastasia Lebedeva',
                 'Ting Luo',
                 'Leandro Rodriguez',
                 'Kateryna Shydlovska',
                 'Christopher Stanley',
                 'ilker zaimoglu',
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


class PairGenerator:
    """Generator that produces pairs."""
    def __init__(self, *args, **kwargs):
        self.students = curr_students
        self.recent_pairs = []
        self.final_pairs = []

        while len(self.recent_pairs) >= 11:
            del self.recent_pairs[0]
        self.create()
        return super().__init__(*args, **kwargs)

    def pairs_with_fillin(self, students):
        """Pairing function that adds a fillin value."""
        random.shuffle(students)

        for first_student, second_student in self.grouper(students, 2):
            print(str(first_student), "and", str(second_student))

    def pairs(self, t, size=2, fillvalue=None):
        """Pairing function that is for an even amount of students."""
        random.shuffle(t)
        it = iter(t)
        thing = zip(*[it] * size)
        pairs = [i for i in thing]
        return pairs

    def create(self):
        """Start the input process to choose which function to use."""
        user_input = input('Option 1: Pairs with fillin or 2: Regular pairs?')

        # User input for function choice.
        if user_input == 1:
            pairs = self.pairs_with_fillin(self.students)
        else:
            pairs = self.pairs(self.students)

        # Check against recent_pairs list.
        for pair in pairs:
            if pair not in self.recent_pairs:
                self.recent_pairs.append(pair)
                self.final_pairs.append(pair)

            else:
                shuffled = "".join(pairs)
                random.shuffle(shuffled)
                pairs(shuffled)
        print(prettify.make_pretty(pairs))


PairGenerator()
