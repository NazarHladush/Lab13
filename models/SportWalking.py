from models.Athletics import Athletics

class SportWalking(Athletics):
    def __init__(self, max_athlete_count, name_kind_of_sports, availability_finish_line, average_duration, length, time, speed):
        super().__init__(max_athlete_count, name_kind_of_sports, availability_finish_line, average_duration, length)
        self.time = time
        self.speed = speed