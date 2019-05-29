class SportManager:
    def __init__(self, sport_list):
        self.sport_list = sport_list

    def sort_by_average_duration(self, reverse):
        return sorted(self.sport_list, key = lambda a: a.average_duration, reverse = reverse)

    def sort_max_athlete_count(self , reverse):
        return sorted(self.sport_list, key = lambda a: a.max_athlete_count, reverse = reverse)