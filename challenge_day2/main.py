from tests import tests
from station2 import solution_station_2
from station3 import solution_station_3
from station5 import solution_station_5
from station6 import solution_station_6

observation2 = 
observation3 = 
observation5 = 
observation6 = ('18:15:00', 'input6', 8, 'data8', 3.14)

def combined_algorithm(observations: tuple) -> int:
    output2 = solution_station_2(observations[1])
    output3 = solution_station_3(observations[2])
    output5 = solution_station_5(observations[3])
    output6 = solution_station_6(observations[4])
    
    assert isinstance(output2, str)
    assert isinstance(output3, bool)
    assert isinstance(output5, int)
    assert isinstance(output6, float)
    
    return int.from_bytes(output2[0].encode("unicode_escape"), byteorder='big') * (3 if output3 else 2) * output5 * output6

FINAL_OUTPUT2 = combined_algorithm(observation2)
FINAL_OUTPUT3 = combined_algorithm(observation3)
FINAL_OUTPUT5 = combined_algorithm(observation5)
FINAL_OUTPUT6 = combined_algorithm(observation6)


tests.Test_Exercise(combined_algorithm)
