def selection_sort(arr):
    spot_marker = 0
    while spot_marker < len(arr):
        for num in range(spot_marker, len(arr)):
            if arr[num] < arr[spot_marker]:
                arr[spot_marker], arr[num] = arr[num], arr[spot_marker]
        spot_marker += 1
        print(arr)
l = [997, 853, 701, 571, 433, 307, 181, 71, 991, 839, 691, 569, 431, 293, 179, 71, 983, 829, 683, 563, 421, 283, 173, 67, 977, 827, 677, 577, 419, 281, 167, 61, 971, 823, 673, 547, 409, 277, 163, 59, 967, 821, 661, 541, 401, 271, 157, 53, 953, 811, 659, 523, 397, 269, 151, 47, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647]
selection_sort(l)