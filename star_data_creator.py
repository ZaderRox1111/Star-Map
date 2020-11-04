import sys
from random import *
import math

def main():
    write_file = sys.argv[1]
    entries = int(sys.argv[2])

    choice = input("Do you want to randomly make a constellation? y n --> ").upper()
    if choice == 'Y':
        name_file = input("Name: ")

        con_data, star_list = create_constellation()

        with open(name_file, 'w') as con:
            con.writelines(con_data)

        data = create_data(entries, choice, star_list)

    else:
        data = create_data(entries, choice)

    with open(write_file, 'w') as writing:
        writing.writelines(data)

def create_data(amount, choice, star_list = None):
    data = []
    counter = 0

    for i in range(amount):
        vector_l = random()**0.4
        angle = random()

        x = vector_l * math.cos(angle * 2 * math.pi)
        y = vector_l * math.sin(angle * 2 * math.pi)
        z = random()**0.4

        if random() < 0.75:
            z *= -1

        if random() < 0.85:
            magnitude = round(uniform(3.5, 7.5), 2)
        else:
            magnitude = round(uniform(1, 10), 2)

        useless_1 = 'x'
        counter += 1

        line = f'{x} {y} {z} {useless_1} {magnitude} {counter}\n'

        data.append(line)
    
    data.sort()

    if choice == 'Y':
        place = randint(0, amount)

        y = float((data[place].split())[1])
        margin = 0.1

        for star in star_list:
            current_line = data[place][:len(data[place])-2]

            while abs(y - float((current_line.split())[1])) > margin:
                place -= 1
                current_line = data[place][:len(data[place])-2]

            current_line += f' {star}\n'
            data[place] = current_line

            place -= randint(1,5)

    return data

def create_constellation():
    star_list = []
    num = randint(5,25)
    for i in range(num):
        star_name = f'X8236{i}'
        star_list.append(star_name)

    con_data = []
    for i in range(len(star_list)):
        star_lines = ''
        if i < len(star_list) - 1:
            star_lines += f'{star_list[i]},{star_list[i + 1]}\n'
        else:
            star_lines += f'{star_list[i]},{star_list[2]}\n'

        con_data.append(star_lines)

    return con_data, star_list

def truncate(number, digits):
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

if __name__ == '__main__':
    main()
