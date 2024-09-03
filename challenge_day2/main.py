from tests import tests
from station2 import solution_station_2
from station3 import solution_station_3
from station5 import solution_station_5
from station6 import solution_station_6

observation2 = ('10:09:20', '2024-07-15', 3235, "Kimiya", 12)
observation3 = ('10:09:34', '2024-01-14', 52762, "Tadas", 52)
observation5 = ('10:09:41', '2024-11-08',8674, "Mark", 86

def combined_algorithm(observations: tuple) -> int:
    output2 = solution_station_2(observations[5])
    output3 = solution_station_3(observations[2])
    output5 = solution_station_5(observations[3])
    
    assert isinstance(output2, str)
    assert isinstance(output3, bool)
    assert isinstance(output5, int)
    
    
    return int.from_bytes(output2[0].encode("unicode_escape"), byteorder='big') * (3 if output3 else 2) * output5 * output6

FINAL_OUTPUT2 = combined_algorithm(observation2)
FINAL_OUTPUT3 = combined_algorithm(observation3)
FINAL_OUTPUT5 = combined_algorithm(observation5)
FINAL_OUTPUT6 = combined_algorithm(observation6)


tests.Test_Exercise(combined_algorithm)
