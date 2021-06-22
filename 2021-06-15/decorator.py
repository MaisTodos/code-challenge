import operator
import ipdb

def person_lister(f):

    def wrapper(group):
        group.sort(key=lambda x: int(x[2]))
        resp = []
        for person in group:
            resp.append(f(person))
        return resp

    return wrapper

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    persons = ["Bruno Borges 33 M", "Ana Carolina 27 F", "Isabela Toso 22 F"]
    group = [x.split() for x in persons]
    print(name_format(group))
