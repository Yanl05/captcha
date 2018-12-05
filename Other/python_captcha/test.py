# coding:utf-8
from PIL import Image
import time
import hashlib
import math
import os

im = Image.open("captcha.gif")
# 将图片转换为8位像素模式
im.convert("P")
# 打印颜色直方图   白色序号255
#print(im.histogram())
im2 = Image.new("P", im.size, 255)  # 创建一个白色的图片
#im2.show()

for x in range(im.size[1]): # im.size[1] 为宽
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        if pix == 220 or pix == 227:
            im2.putpixel((y, x), 0)     # 改变单个像素点颜色，y,x为坐标 0为颜色
#im2.show()

#提取单个字符图片
inletter = False    # 末尾变量
foundletter = False # 开头变量
start = 0
end = 0
letters = []
for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y, x))
        if pix != 255: #如果像素点不等于255 就是像素点不为白色,则令末尾变量为真
            inletter = True
    if foundletter == False and inletter == True:
        foundletter = True
        start = y
    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start, end))

    inletter = False
# 得到每个图片的开头和结尾的序号
#print(letters)

count = 0
for letter in letters:
    #m = hashlib.md5()
    # (切割的起始横坐标，起始纵坐标，切割的宽度，切割的高度)
    im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
    #m.update(("%s%s" % (time.time(), count)).encode('utf-8')) # 哈希加密后需要编码，在每次update后面加上一个encode
    #im3.save("./%s.gif" % (m.hexdigest()))
    count += 1

d1 = {}
count = 0
for i in im.getdata():
    d1[count] = i
    print(d1[count])
    count += 1
# 返回图片每个点的色素而已
# {0: 255, 1: 255, 2: 255, 3: 255, 4: 255, 5: 255, 6: 255, 7: 255, 8: 255, 9: 255, 10: 255, 11: 255, 12: 255, 13: 255, 14: 255, 15: 255, 16: 255, 17: 255, 18: 255, 19: 255, 20: 255, 21: 255, 22: 255, 23: 255, 24: 255, 25: 255, 26: 255, 27: 255, 28: 255, 29: 255, 30: 255, 31: 255, 32: 255, 33: 255, 34: 255, 35: 255, 36: 255, 37: 255, 38: 255, 39: 255, 40: 255, 41: 255, 42: 255, 43: 255, 44: 255, 45: 255, 46: 255, 47: 255, 48: 255, 49: 255, 50: 255, 51: 255, 52: 255, 53: 255, 54: 255, 55: 255, 56: 255, 57: 255, 58: 255, 59: 255, 60: 255, 61: 255, 62: 255, 63: 255, 64: 255, 65: 255, 66: 255, 67: 0, 68: 0, 69: 0, 70: 255, 71: 255, 72: 255, 73: 255, 74: 0, 75: 0, 76: 0, 77: 255, 78: 0, 79: 255, 80: 255, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 255, 88: 255, 89: 0, 90: 255, 91: 255, 92: 255, 93: 0, 94: 0, 95: 255, 96: 0, 97: 255, 98: 0, 99: 255, 100: 255, 101: 0, 102: 0, 103: 0, 104: 0, 105: 0, 106: 0, 107: 255, 108: 255, 109: 0, 110: 0, 111: 0, 112: 0, 113: 0, 114: 255, 115: 255, 116: 255, 117: 0, 118: 0, 119: 0, 120: 255, 121: 0, 122: 255, 123: 255, 124: 255, 125: 0, 126: 0, 127: 0, 128: 255, 129: 0, 130: 0, 131: 255, 132: 255, 133: 0, 134: 0, 135: 0, 136: 255, 137: 0, 138: 0, 139: 0, 140: 0, 141: 0, 142: 0, 143: 255, 144: 255, 145: 0, 146: 0, 147: 0, 148: 0, 149: 0, 150: 0, 151: 255, 152: 255, 153: 255, 154: 255, 155: 0, 156: 0, 157: 0, 158: 255, 159: 255, 160: 255, 161: 255, 162: 255, 163: 255, 164: 255, 165: 255, 166: 255, 167: 255, 168: 255, 169: 255, 170: 255, 171: 255, 172: 255, 173: 255, 174: 255, 175: 255}

