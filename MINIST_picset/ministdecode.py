# coding=UTF-8
import numpy as np
import numpy
import struct
import matplotlib.pyplot as plt
import scipy.misc
import os


def parese_idx3(idx3_file):
    """
    idx3文件解析方法
    :param idx3_file: idx3文件路径
    :return: 数据集
    """
    # 读取二进制数据
    bin_data = open('train-images.idx3-ubyte', 'rb').read()

    # 解析文件头信息 magic、imgs、height、width
    # '>IIII'是说使用大端法读取4个unsinged int32
    offset = 0
    fmt_header = '>iiii'
    magic, imgs, height, width = struct.unpack_from(fmt_header, bin_data, offset)
    print('magic:%d, imgs: %d, heightXwidth: %dX%d' % (magic, imgs, height, width))

    # 解析数据集
    image_size = height * width
    offset += struct.calcsize(fmt_header)
    fmt_image = '>' + str(image_size) + 'B'
    images = np.empty((imgs, height, width))
    for i in range(100):   ##imgs
        if (i + 1) % 10000 == 0:
            print('已解析 %d' % (i + 1) + '张')
        images[i] = np.array(struct.unpack_from(fmt_image, bin_data, offset)).reshape((height, width))
        offset += struct.calcsize(fmt_image)
        #img = images[i]
#        images[i][images[i] > 0] = 1
        images[i] = images[i].astype(np.int)
#        img = np.dtype('int')
        savename = str(i) + '.bin'
        fullpath = os.path.join('F:\大四\北大先修课\深度学习加速\MINIST_picset\训练集2进制1', savename)
        numpy.savetxt(fullpath, images[i], delimiter=',')
        #scipy.misc.imsave(fullpath, images[i])
    return images


# def parese_idx1(idx1_file):
# """
# idx1文件解析方法
# :param idx1_file: idx1文件路径
# :return: 数据集
# """
# 读取二进制数据
##    bin_data = open(idx1_file, 'rb').read()
##
# 解析文件头信息 magic、imgs
##    offset = 0
##    fmt_header = '>ii'
##    magic, imgs = struct.unpack_from(fmt_header, bin_data, offset)
##    print ('magic:%d, imgs: %d' % (magic, imgs))
##
# 解析数据集
##    offset += struct.calcsize(fmt_header)
##    fmt_image = '>B'
##    labels = np.empty(imgs)
# for i in range(imgs):
# if (i + 1) % 10000 == 0:
##            print ('已解析 %d' % (i + 1) + '张')
##        labels[i] = struct.unpack_from(fmt_image, bin_data, offset)[0]
##        offset += struct.calcsize(fmt_image)
# return labels


imgs = parese_idx3("train-images.idx3-ubyte")
#imgs[imgs > 0] = 1
#numpy.savetxt('E:\pythonpractice\minist\minist.bin', imgs, delimiter=',')
#labs = parese_idx1("ubyte/t10k-labels.idx1-ubyte");

for i in range(10):
   # print(labs[i])
    plt.imshow(imgs[i])
    plt.show()
