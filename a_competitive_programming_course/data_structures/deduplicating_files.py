def get_hash(file):
    actual_hash = ord(file[0])
    for letter in file[1:]:
        actual_hash = ord(letter)^actual_hash
    return actual_hash

while True:
    n_files = int(input())
    if n_files == 0:
        break
    hashes = {}
    unique_files = 0
    collisions = 0
    for i in range(n_files):
        file = input()
        file_hash = get_hash(file)
        if file_hash not in hashes:
            hashes[file_hash] = {file:1}
            unique_files+=1
        else:
            
            if file not in hashes[file_hash]:
                unique_files+=1
                hashes[file_hash][file] = 0
            collisions += sum(hashes[file_hash].values()) - hashes[file_hash][file]
            hashes[file_hash][file]+=1
    print(str(unique_files)+ " "+ str(collisions))
