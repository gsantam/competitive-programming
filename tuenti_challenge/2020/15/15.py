import zlib

def crc32_combine(crc1, crc2, len2):
    """Explanation algorithm: https://stackoverflow.com/a/23126768/654160
    crc32(crc32(0, seq1, len1), seq2, len2) == crc32_combine(
        crc32(0, seq1, len1), crc32(0, seq2, len2), len2)"""
    # degenerate case (also disallow negative lengths)
    if len2 <= 0:
        return crc1

    # put operator for one zero bit in odd
    # CRC-32 polynomial, 1, 2, 4, 8, ..., 1073741824
    odd = [0xedb88320] + [1 << i for i in range(0, 31)]
    even = [0] * 32

    def matrix_times(matrix, vector):
        number_sum = 0
        matrix_index = 0
        while vector != 0:
            if vector & 1:
                number_sum ^= matrix[matrix_index]
            vector = vector >> 1 & 0x7FFFFFFF
            matrix_index += 1
        return number_sum

    # put operator for two zero bits in even - gf2_matrix_square(even, odd)
    even[:] = [matrix_times(odd, odd[n]) for n in range(0, 32)]

    # put operator for four zero bits in odd
    odd[:] = [matrix_times(even, even[n]) for n in range(0, 32)]

    # apply len2 zeros to crc1 (first square will put the operator for one
    # zero byte, eight zero bits, in even)
    while len2 != 0:
        # apply zeros operator for this bit of len2
        even[:] = [matrix_times(odd, odd[n]) for n in range(0, 32)]
        if len2 & 1:
            crc1 = matrix_times(even, crc1)
        len2 >>= 1

        # if no more bits set, then done
        if len2 == 0:
            break

        # another iteration of the loop with odd and even swapped
        odd[:] = [matrix_times(even, even[n]) for n in range(0, 32)]
        if len2 & 1:
            crc1 = matrix_times(odd, crc1)
        len2 >>= 1

        # if no more bits set, then done
    # return combined crc
    crc1 ^= crc2
    return crc1

memo = dict()
home = "/Users/guillermo/my_projects/competitive-programming/tuenti_challenge/2020/15/animals"
import zlib
def crc32_zeros(n_zeros):
    if n_zeros == 0:
        return 0
    if n_zeros == 1:
        return zlib.crc32(b'\x00')
    if n_zeros in memo:
        return memo[n_zeros]
    if n_zeros//2 in memo:
        left = memo[n_zeros//2]
    else:
        left = crc32_zeros(n_zeros//2)
        memo[n_zeros//2] = left
    if (n_zeros+1)//2 in memo:
        right = memo[(n_zeros+1)//2]
    else:
        right = crc32_zeros((n_zeros+1)//2)
        memo[(n_zeros+1)//2] = right
        
    solution = crc32_combine(left,right,(n_zeros+1)//2)
    memo[n_zeros] = solution
    return solution

input_ = open("testInput.txt","r")
output = []
lines = input_.readlines()
i=0
output = []

def format_hex(hex_):
    if len(hex_)<10:
        print(hex_)
    hex_ = hex_[2:]
    hex_="0"*(8-len(hex_))+hex_
    return hex_

while i < len(lines):
    line = lines[i].strip()
    print(line)
    file_name = line.split(" ")[0]
    cases = int(line.split(" ")[1])
    file_bytes_cmd = "stat -f%z  {home}/{file_name}".format(home = home,file_name=file_name)
    file_bytes = !{file_bytes_cmd}
    file_bytes = int(file_bytes[0])
    i+=1
    additions = []
    file_crc32 = format_hex(hex(crc32_zeros(file_bytes)))
    output.append(file_name + " 0:"+" "+file_crc32)
    for j in range(cases):
        line = lines[i].strip()
        pos = int(line.split(" ")[0])
        byte_crc32 = zlib.crc32(bytes([int(line.split(" ")[1])]))
        new_additions = []
        for pos_,byte_crc32_ in additions:
            if pos_<pos:
                new_additions.append((pos_,byte_crc32_))
            else:
                new_additions.append((pos_+1,byte_crc32_))
        
        new_additions.append((pos,byte_crc32))
        additions = sorted(new_additions)
        current_crc32 = 0
        prev = 0
        for pos,byte_crc32 in additions:
            current_crc32 = crc32_combine(current_crc32,crc32_zeros(pos-prev),pos-prev)
            current_crc32 = crc32_combine(current_crc32,byte_crc32,1)
            prev = pos + 1
        current_crc32 = crc32_combine(current_crc32,crc32_zeros(file_bytes+len(new_additions)-prev),file_bytes+len(new_additions)-prev)
        print(current_crc32)
        output.append(file_name + " "+str(j+1)+":"+" "+format_hex(hex(current_crc32)))
        i+=1
        
output_file = open("testOutput.txt","w")
output_file.write("\n".join(output))
output_file.close()
