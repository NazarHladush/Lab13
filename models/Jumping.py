from models.Athletics import Athletics


class Jumping(Athletics):
    def __init__(self, max_athlete_count, name_kind_of_sports, availability_finish_line, average_duration, length, kind_of_jump, height):
        super().__init__(max_athlete_count, name_kind_of_sports, availability_finish_line, average_duration, length)
        self.kind_of_jump = kind_of_jump
        self.height = height

    # def __repr__(self):
    #     return str(self.__dict__)
