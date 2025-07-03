from _file import file_iterator

def get_cats_info(path: str) -> list[dict] :
    result = []
    for line in file_iterator(path):
        try:
            uuid, name, age = line.split(',')
            result.append({'id': uuid, 'name': name, 'age': int(age)})
        except ValueError:
            continue
    return result


if __name__ == '__main__':
    cats_info = get_cats_info("../data/cats.csv")
    print(cats_info)