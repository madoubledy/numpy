import numpy as np
my_list = [1,3,4,5,9,7]
arr = np.array(my_list)
print(arr)
[1 3 4 5 9 7]
print(type(arr))
<class 'numpy.ndarray'>
print(arr.shape)
(6,)
print(arr.reshape(1,6))
print(arr.reshape(6,1))
[[1 3 4 5 9 7]]
[[1]
 [3]
 [4]
 [5]
 [9]
 [7]]
l1 = [12,15,17]
l2 = [11,88,76]
l3 = [56,54,22]
a =np.array([l1,l2,l3])
print(type(a))
print(a)
print(a.shape)
<class 'numpy.ndarray'>
[[12 15 17]
 [11 88 76]
 [56 54 22]]
(3, 3)
print(a.reshape(1,9))
print(a.reshape(9,1))
[[12 15 17 11 88 76 56 54 22]]
[[12]
 [15]
 [17]
 [11]
 [88]
 [76]
 [56]
 [54]
 [22]]
l4=[1,2,3,4,5]
l5=[7,8,9,0,1]
l6=[1,3,4,5,6]
l7=[7,7,2,3,4]
b= np.array([l4,l5,l6,l7])
print(b)
[[1 2 3 4 5]
 [7 8 9 0 1]
 [1 3 4 5 6]
 [7 7 2 3 4]]
print(b[:,:])
[[1 2 3 4 5]
 [7 8 9 0 1]
 [1 3 4 5 6]
 [7 7 2 3 4]]
print(b[2:,1:3])
[[3 4]
 [7 2]]
print(b[1:,1:])
[[8 9 0 1]
 [3 4 5 6]
 [7 2 3 4]]
print(b[1:3,:2])
[[7 8]
 [1 3]]
ar4=np.arange(1,20,3)
print(ar4)
[ 1  4  7 10 13 16 19]
ar7=np.linspace(1,20,10)
print(ar7)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_4172/330283214.py in <module>
----> 1 ar7=np.linspace(1,20,10)
      2 print(ar7)

TypeError: 'tuple' object is not callable
ar4*2
array([ 2,  8, 14, 20, 26, 32, 38])
ar4%2==0
array([False,  True, False,  True, False,  True, False])
ar4[4:8:2]=11
print(ar4)
[ 1  4  7 10 11 16 11]
ar4[4:]=10
print(ar4)
[ 1  4  7 10 10 10 10]
print(np.random.randn(3,4))
[[ 0.24417192 -0.76668562 -2.14479775  0.64551041]
 [-0.75507944 -1.23046464 -1.77331616 -0.54900989]
 [-1.39846675  1.40576716 -0.84902157 -0.15645248]]
print(np.random.rand(3,4))
[[0.6273391  0.92200334 0.42508942 0.55234215]
 [0.4432475  0.69656145 0.740405   0.92499799]
 [0.88206959 0.16504969 0.23498233 0.03248786]]
