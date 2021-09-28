def sub_pa(elements):
    r = elements[-1] - elements[0]
    results = []

    while r > 0:
        print(f"R: {r}")

        for a1 in elements:
            print(f"A1: {a1}")
            a2 = a1 + r
            a3 = a2 + r
            if a2 not in elements or a3 not in elements:
                break

            sub_pa = [a1, a2, a3]
            an = a3
            while True:
                an = an + r
                if an in elements:
                    sub_pa.append(an)
                else:
                    break


            results.append(sub_pa)

        r = r-1

    return results





if __name__ == "__main__":
    assert sub_pa([1, 2, 3]) == [[1, 2, 3]]
    assert sub_pa([2, 4, 6, 10]) == [[2, 6, 10], [2, 4, 6]]

    # GABARITO ORIGINAL
    # assert sub_pa([1, 2, 3, 4]) == [[1, 2, 3, 4]]
    # sub_pa((1,2,3,5,6,7,9)) = [
    #     (1,2,3),     # r=1, a1=1
    #     (5,6,7),     # r=1, a1=5
    #     (1,3,5,7,9), # r=2, a1=1
    #     (3,6,9),     # r=3, a1=3
    #     (1,5,9),     # r=4, a1=1
    # ]