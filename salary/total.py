from _file import file_iterator

def total_salary(path: str) -> list[float]:
    try:
        total = .0
        average = .0
        records = 0
        for line in file_iterator(path):
            name, salary = line.strip().split(',')
            salary = float(salary)

            total += salary
            average += salary
            records += 1

        average /= records
        return [total, average]
    except:
        return [.0, .0]

if __name__ == '__main__':
    total, average = total_salary("../data/salary.csv")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")