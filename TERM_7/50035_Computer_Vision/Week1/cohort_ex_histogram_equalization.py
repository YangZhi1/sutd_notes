import math

# Purpose of histogram equalization is to raise the contrast in an image
# to produce a better quality image

'''
function: summation
input:
    1. accumulated counts of the pixels
    2. current pixel intensity (0-255)
    3. min accumulated count
    4. max accumulted count

returns: normalized accumuated count
'''
def summation(accumulated_counts, pixel_value, acc_min, acc_max):
    this_pixel_acc = accumulated_counts[pixel_value]
    return (this_pixel_acc-acc_min)/(acc_max-acc_min)


'''
function: histogram equalization

input: 2D array (image)
returns: image that has been applied histogram equalization
'''
def histogram_equalization(img):
    L = 256
    pixel_counts = [0] * 256
    total_count = 0
    for row in range(len(img)):
        for col in range(len(img)):
            pixel_counts[img[row][col]] += 1
            total_count += 1

    accumulated_counts = [0] * 256
    for index in range(len(pixel_counts)):
        if(pixel_counts[index] != 0):
            accumulated_counts[index] = sum(pixel_counts[:index+1])

    #print(accumulated_counts)
        
    acc_min = total_count
    acc_max = total_count
    for index in range(len(accumulated_counts)):
        if(accumulated_counts[index] != 0 and accumulated_counts[index] < acc_min):
            acc_min = accumulated_counts[index]
    print('acc_min, acc_max: ', acc_min, acc_max)

    return_image = []
    for row in range(len(img)):
        tmp_row = []
        for col in range(len(img)):
            T_k = math.floor((L-1) * summation(accumulated_counts, img[row][col], acc_min, acc_max))
            tmp_row.append(T_k)
        return_image.append(tmp_row)

    return return_image


input1 = [[1, 3, 1, 3], [2, 3, 10, 11], [11, 10, 2, 3], [1, 2, 3, 3]]
output1 = histogram_equalization(input1)
print(output1)

# output1: [[0, 176, 0, 176], [58, 176, 215, 255], [255, 215, 58, 176], [0, 58, 176, 176]]


input2 = [[52,52,53,72], [72,72,53,53], [88,72,52,52], [88,88,53,53]]
output2 = histogram_equalization(input2)
print(output2)

# output2: [[0, 0, 106, 191], [191, 191, 106, 106], [255, 191, 0, 0], [255, 255, 106, 106]]