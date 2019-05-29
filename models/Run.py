from models.Athletics import Athletics

class Run(Athletics):
    def __init__(self, max_athlete_count, name_kind_of_sports, availability_finish_line, average_duration, length, kind_of_run, time, speed):
        super().__init__(max_athlete_count, name_kind_of_sports, availability_finish_line, average_duration, length)
        self.kind_of_run = kind_of_run
        self.time = time
        self.speed = speed

    # def __repr__(self):
    #     return str(self.__dict__)