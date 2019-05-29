from manager.SportManager import SportManager
from models.Jumping import Jumping
from models.Run import Run
from models.Throw import Throw
from models.KindOfRun import KindOfRun
from models.KindOfThrow import KindOfThrow
from models.KindOfJump import KindOfJump

def main():

    run = Run(122, "Run", True, 30, 188, KindOfRun.LONG, 87, 66)
    jumping = Jumping(12, "Jumping", True, 90, 188, KindOfJump.TRIPLEJUMP, 75)
    throw = Throw(142, "Throw", True, 80, 188, KindOfThrow.DISK)

    sportList = [run, jumping, throw]

    manager = SportManager(sportList)

    for a in manager.sort_by_average_duration(reverse=False):
        print('Name:', a.name_kind_of_sports,',', 'Average duration: ', a.average_duration)

    print('\n')

    for a in manager.sort_max_athlete_count(True):
        print('Name:', a.name_kind_of_sports,',', 'Max athlete count: ', a.max_athlete_count)

if __name__ == '__main__':
    main()
