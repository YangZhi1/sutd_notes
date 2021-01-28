# This code applies a 3x3 filter kernel over a 5x5 image

# This is purely for exercise, function is designed to work with 5x5 image and 3x3 kernel

from PIL import Image
import numpy as np

img = [[30, 40, 20, 30, 40], [40, 20, 30, 40, 30], [20, 30, 40, 30, 40], [30, 40, 30, 40, 20], [40, 30, 40, 20, 30]]
kernel = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

def img_filtering(img, kernel):
    padding = [0] * (len(img) + 2)
    for row in img:
        row.insert(0, 0)
        row.append(0)
    img.insert(0, padding)
    img.append(padding)

    new_img = []
    tmp_row = []
    for row_no in range(len(img) - 2):
        tmp_row = []
        for col_no in range(len(img[0]) - 2):
            current_pixel = round((kernel[0][0] * img[row_no][col_no] + kernel[0][1] * img[row_no][col_no+1] + kernel[0][2] * img[row_no][col_no+2] + 
                            kernel[1][0] * img[row_no+1][col_no] + kernel[1][1] * img[row_no+1][col_no+1] + kernel[1][2] * img[row_no+1][col_no+2] + 
                            kernel[2][0] * img[row_no+2][col_no] + kernel[2][1] * img[row_no+2][col_no+1] + kernel[2][2] * img[row_no+2][col_no+2]) / 9)

            tmp_row.append(current_pixel)
        new_img.append(tmp_row)

    return new_img

new_image = img_filtering(img, kernel)

print(len(new_image))
print(len(new_image[0]))

print('\n', new_image)

# Uncomment the following lines if you want to see what the mini 5x5 image looks like and to save it 
#im = Image.fromarray(np.array(new_image))
#im.show()
#im.save('cohort_exercise')