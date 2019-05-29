from models.Athletics import Athletics

class Throw(Athletics):
    def __init__(self, max_athlete_count, name_kind_of_sports, availability_finish_line, average_duration, length, kind_of_throw):
        super().__init__(max_athlete_count, name_kind_of_sports, availability_finish_line, average_duration, length)
        self.kind_of_throw = kind_of_throw

    # def __repr__(self):
    #     return str(self.__dict__)