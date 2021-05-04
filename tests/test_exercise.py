import pytest
import src.exercise

def test_exercise():
    input_values = ["3","5","10","2","179","1534","1543","57"]
    input_values_stored = ["3","5","10","2","179","1534","1543","57"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)
    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)
    src.exercise.main()
    
    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)
    src.exercise.main()
    
    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)
    src.exercise.main()
    
    assert [output[0],output[1],output[2]] == ["","","7.5"]
    assert [output[3],output[4],output[5]] == ["","","10.0"]
    assert [output[6],output[7],output[8]] == ["","","137293.0"]
    assert [output[9],output[10],output[11]] == ["","","43975.5"]
