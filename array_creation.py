{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "cfa54df0-71ee-4f5f-81e5-0a2aabf67767",
   "metadata": {},
   "source": [
    "# array creation: conversion from other python structures"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "17de9a80-2253-4f0f-9f5f-e7ccabfe5786",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bf7810fb-6cda-4822-81de-3b1cc2ed6e9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "listarray=np.array([[1 , 2 , 3 , 4] , [5 , 4 , 9 , 0] , [ 5 , 8 , 6 , 1]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b9d55106-4665-44a0-8595-e8d7297a94f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3, 4],\n",
       "       [5, 4, 9, 0],\n",
       "       [5, 8, 6, 1]])"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listarray"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d4031bf1-9ae9-4a7c-916b-a5e3d95e5e7f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int64')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listarray.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ec8533a0-9ca2-4ff9-a69b-f34e5ea0cb80",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 4)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listarray.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "aa2f8ab3-7733-4406-8d63-de380801e86d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listarray.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4664385b-fd66-4159-9a43-f08af1567aa1",
   "metadata": {},
   "outputs": [],
   "source": [
    "listarr1=np.array({32 , 24 , 24})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9286d836-b9e7-49ef-a95e-517279a9efd8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array({32, 24}, dtype=object)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listarr1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "58513504-396a-4d86-88ed-3cd529dd14a2",
   "metadata": {},
   "source": [
    "# zeros , ones , arange"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "42fc490a-eac4-4a63-8eb0-5473882630df",
   "metadata": {},
   "outputs": [],
   "source": [
    "zeros=np.zeros((4 , 3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "aa137460-6281-4161-8ba5-b0d3b7bbea50",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zeros.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "23a6009b-e9e4-4464-aeec-d9b2b2e40ce0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0., 0.],\n",
       "       [0., 0., 0.],\n",
       "       [0., 0., 0.],\n",
       "       [0., 0., 0.]])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zeros"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "853f0445-074a-412c-8c35-8b20bfa9e8dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "ones=np.ones((4 , 3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "1ddef318-60fa-4f98-9ed0-56a568c069fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ones.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "2f37f70d-6697-4685-b372-d9eb0edc33a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 1., 1.],\n",
       "       [1., 1., 1.],\n",
       "       [1., 1., 1.],\n",
       "       [1., 1., 1.]])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ones"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "fb627d37-5bcf-48cb-8511-2292d7baa867",
   "metadata": {},
   "outputs": [],
   "source": [
    "rng=np.arange(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "5fdd6384-3361-4799-a272-d73775ea75b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int64')"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rng.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "568de5d7-7e2f-436f-9843-f90de19c507c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,\n",
       "       17, 18, 19])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rng"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "518fc8ee-2383-4556-a753-848aab0b6a04",
   "metadata": {},
   "outputs": [],
   "source": [
    "lspace=np.linspace(1 , 50 , 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "05bdac7e-d661-484a-90e3-31a0641a316a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1.        ,  6.44444444, 11.88888889, 17.33333333, 22.77777778,\n",
       "       28.22222222, 33.66666667, 39.11111111, 44.55555556, 50.        ])"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lspace"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "d78d399f-1c36-42a4-8795-0aa4e5c460db",
   "metadata": {},
   "outputs": [],
   "source": [
    "emp=np.empty((4 , 5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "936fa50f-ce73-4975-a77c-925df09d7b73",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[6.23042070e-307, 4.67296746e-307, 1.69121096e-306,\n",
       "        9.34609111e-307, 1.42413555e-306],\n",
       "       [1.78019082e-306, 1.37960147e-306, 1.33511562e-306,\n",
       "        2.22518251e-306, 1.33511969e-306],\n",
       "       [1.78022342e-306, 1.05700345e-307, 1.69118108e-306,\n",
       "        8.06632139e-308, 1.20160711e-306],\n",
       "       [1.69119330e-306, 1.29062229e-306, 6.89804133e-307,\n",
       "        1.11261162e-306, 8.34443015e-308]])"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "e90eb19d-e40d-415c-9d9e-2282fd58d345",
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_like=np.empty_like(lspace)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "7c1ec905-b225-4b08-8456-933b07e33789",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1.        ,  6.44444444, 11.88888889, 17.33333333, 22.77777778,\n",
       "       28.22222222, 33.66666667, 39.11111111, 44.55555556, 50.        ])"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp_like"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "eb01bdf1-55dc-4e7a-b4d5-1f9e1c213a15",
   "metadata": {},
   "outputs": [],
   "source": [
    "ide=np.identity(50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "a3700741-6c5f-4286-9c4f-9be6e32b90ef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 1., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 1., ..., 0., 0., 0.],\n",
       "       ...,\n",
       "       [0., 0., 0., ..., 1., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 1., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 1.]])"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ide"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "13843918-4e85-4430-b1b9-19fa50e6cdca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(50, 50)"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ide.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "05012a59-fd48-40d5-969a-3397b78777b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2500"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ide.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "e33700e6-f4f4-4ca1-a0dc-355b0800edab",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr=np.arange(99)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "d2df3d06-b604-410a-94ec-b530439f8a66",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,\n",
       "       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,\n",
       "       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,\n",
       "       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,\n",
       "       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,\n",
       "       85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98])"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "7c4d80a8-4975-4b7d-926e-5f6f655474bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15,\n",
       "        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,\n",
       "        32],\n",
       "       [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,\n",
       "        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,\n",
       "        65],\n",
       "       [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,\n",
       "        82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,\n",
       "        98]])"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.reshape(3 , 33)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "af823e9a-bbdf-4c57-ad0e-d89d04437117",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,\n",
       "       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,\n",
       "       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,\n",
       "       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,\n",
       "       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,\n",
       "       85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98])"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "3b6164d7-203a-4ea1-9e3b-8957413db7a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(99,)"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "f13181b8-046e-45e1-a1e2-125e67e0d4f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr=arr.reshape(3 , 33)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "1cf83649-014f-4008-90dc-b083c8813d90",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15,\n",
       "        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,\n",
       "        32],\n",
       "       [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,\n",
       "        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,\n",
       "        65],\n",
       "       [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,\n",
       "        82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,\n",
       "        98]])"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "d08fb35d-bb4d-4083-bca0-7c96855f28d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr=arr.ravel()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "76212976-5bef-4aab-b29b-dfa9b1ea065e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,\n",
       "       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,\n",
       "       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,\n",
       "       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,\n",
       "       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,\n",
       "       85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98])"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5102cba0-c4e4-4828-b70e-44c2ea7e27a6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
