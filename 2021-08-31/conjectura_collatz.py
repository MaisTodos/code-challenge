def collatz(number):
    if number % 2 == 0:
        return number / 2
    return number * 3 + 1

def collatz_list(number):
    if number == 1:
        return [1]
        
    result = [number]
    item = collatz(number)
    result.append(item)

    while item != 1:
        item = collatz(item)
        result.append(item)

    return result


if __name__ == "__main__":
    assert collatz(2) == 1
    assert collatz(3) == 10
    assert collatz(1) == 1

    assert collatz_list(13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert collatz_list(5) == [5, 16, 8, 4, 2, 1]

    print("YEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEY `o´")