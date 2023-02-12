
import cv2



kernel_hit = cv2.getStructuringElement(cv2.MORPH_RECT,ksize=(3,3))
kernel_miss = cv2.getStructuringElement(cv2.MORPH_CROSS,ksize=(3,3))
def hitmiss(kernel_hit,kernel_miss):
    img = cv2.imread('D:\BTLXulianh\\1.png', cv2.IMREAD_UNCHANGED)
    cv2.imshow("Binary Image", img)
    hitmiss = cv2.morphologyEx(img, cv2.MORPH_HITMISS, kernel_hit,kernel_miss)
    cv2.imshow("Hit-miss Image", hitmiss)
    cv2.waitKey(0)
hitmiss(kernel_hit=kernel_hit,kernel_miss=kernel_miss)