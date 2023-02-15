# in_file = open("input_file.txt","r")
# fruit = in_file.readlines()
# print(fruit)
# in_file.close()

# in_file = open("input_file.txt","r")

# first_fruit = in_file.readline()
# second_fruit = in_file.readline()

def read_file(filename):
    in_file = open(filename,"r")
    first_line = in_file.readline()
    id = analyze_ID(first_line)


def test_read_file():
    from module import read_file
    filename = "my_test_data.txt"
    answer = read_file(filename)
    expected = 50
    assert answer == expected


def analyze_ID(input_line):
    patient_data = input_line.strip("\n").split("=")
    patient_id = int(patient_data[1])
    return patient_id