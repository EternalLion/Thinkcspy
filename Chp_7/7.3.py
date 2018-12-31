def mark_grade_mapping(mark):
    if mark >= 90:
        print(f'The mark {mark} gets the grade A')
        print('{}, A'.format(mark))
    elif mark > 80:
        print(f'{mark}, B')
    elif mark > 70:
        print(f'{mark}, C')
    elif mark > 60:
        print(f'{mark}, D')
    else:
        print(f'{mark}, F')


for m in range(101):
    mark_grade_mapping(m)
