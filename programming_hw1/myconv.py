import numpy as np
import matplotlib.pyplot as plt

def draw(x, y, x_label='', y_label='', title=''):
    plt.stem(x, y, basefmt='k-')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def my_colv(x1, x2):
    len1 = len(x1)
    len2 = len(x2)
    #result = [] ###直接乘
    # for i in range(len1+len2-1):
    #     sum = 0
    #     for j in reversed(range(i+1)):
    #         if j >= len2 or i-j >= len1:
    #             continue
    #         sum += x2[j]*x1[i-j]
    #     result.append(sum)
    # return np.array(result).astype(np.int32)
    conv_mat = []
    for i in range(len1 + len2 -1):
        tmp = []
        for j in range(len1):
            if i - j >= 0 and i - j < len2:
                tmp.append(x2[i-j])
            else:
                tmp.append(0)
        conv_mat.append(tmp)
    conv_mat = np.array(conv_mat)
    result = conv_mat @ x1
    return result
### Part a 
n = np.arange(0, 41)
x1 = np.where(n<21, n, 40-n)
x2 = np.where((n>=1)&(n<11), 1, 0)

draw(n, x1, 'n', 'x1')
draw(n, x2, 'n', 'x2')

### Part b
y1 = np.convolve(x1, x2, mode='full')
n = np.arange(0, len(y1))
draw(n, y1, 'n', 'y', 'np.convolve')

### Part c
y2 = my_colv(x1, x2)
draw(n, y2, 'n', 'y', 'my_colv')
print(y1.all() == y2.all())

### Part d
x1 = np.array([0, 3, 9, 27, 0])
x2 = np.array([0, 2, 4, 8, 16, 32, 0])
n = np.arange(0, 5)
draw(n, x1, 'n', 'x1')
n = np.arange(0, 7)
draw(n, x2, 'n', 'x2')

y1 = np.convolve(x1, x2, 'full')
n = np.arange(0, len(y1))
draw(n, y1, 'n', 'y', 'np.convolve')

y2 = my_colv(x1, x2)
draw(n, y2, 'n', 'y', 'my_conv')

print(y1.all() == y2.all())