import cv2 as cv
 
img_color = cv.imread('img.format', cv.IMREAD_COLOR)
 
height,width = img_color.shape[:2]
print (height)
print (width)
f = open('image.txt', 'w')
 
for y in range(height):
    for x in range(width):
        f.write("%s"%img_color[y,x])
    f.write("\n")
 
f.close()
cv.waitKey(0)
