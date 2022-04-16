import math

def found_max_sequence_count(array):
    sequence_count = 1
    max_sequence_count = 1
    for i in range(1, len(array)):
        if array[i] == array[i-1] + 1:
            sequence_count += 1
        else:
            sequence_count = 1
        max_sequence_count = max(max_sequence_count, sequence_count)

    return max_sequence_count


def biggest_chocolate_box(n,m,h,v):
    if n < 0 or m < 0:
        return  -1
    
    h.sort()
    v.sort()
    max_seq_count_h = found_max_sequence_count(h)
    max_seq_count_v = found_max_sequence_count(v)
    return (max_seq_count_h + 1) * (max_seq_count_v + 1)
        

if __name__ == '__main__':
    n = 6
    m = 6
    h = [4,3, 5]
    v = [2, 3]
    print(biggest_chocolate_box(n, m, h, v))
