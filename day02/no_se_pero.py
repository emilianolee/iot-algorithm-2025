def find_and_insert_data(friend,k_count):
    findPos = -1
    for i in range(len(katok)):
        pair = katok[i]
        if k_count >= pair[1]:
            findPos = i
            break
    if findPos == -1:
        findPos = len(katok)

    insert_data(findPos, (friend, k_count))


def insert_data(pos, friend):
    if pos < 0 or pos > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    katok.append(None)
    kLen = len(katok)

    for 