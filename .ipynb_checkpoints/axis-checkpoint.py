{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5b62d295-e0f8-4988-825e-10b905911f00",
   "metadata": {},
   "source": [
    "# axis in numpy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3402d0d4-8ad1-4b4a-afb1-ce62f7b4dee0",
   "metadata": {},
   "source": [
    "**attributes**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e3692cbe-c4a4-4c4d-ad4a-a952f8bd6f32",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e57755df-35f4-42ad-a3cd-ba188dbcbe1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=[[1 , 2 , 3],[4 , 5 , 6],[7 , 8 , 9]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "37de20b1-843e-4601-818e-c70c4bff75c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr=np.array(x , np.int32)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "74e9cbce-ca0a-49e2-ba11-b89591b575f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 5, 6],\n",
       "       [7, 8, 9]])"
      ]
     },
     "execution_count": 4,
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
   "execution_count": 5,
   "id": "f1379d66-f26e-4de7-b60d-0632ad1695ba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([12, 15, 18])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.sum(axis=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "778362ab-ebff-49bc-b255-787ebe497a9a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 6, 15, 24])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.sum(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "870129af-3257-46d7-8c26-dbc49eb201cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 4, 7],\n",
       "       [2, 5, 8],\n",
       "       [3, 6, 9]])"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "78b3bf51-4901-4496-86a5-f33779929103",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<numpy.flatiter at 0x1670111d920>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.flat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "db3af534-a8f2-46fa-a3fd-ed26f4ac1ded",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "for item in arr.flat:\n",
    "    print(item)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "49ceb061-27f4-4119-8580-7253ee60b1ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "16104304-5d7d-4700-8409-35187d1cfee3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "517f278f-e33a-49aa-96c4-a2575e6c3b89",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "36"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.nbytes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db0ce9af-82e2-4a8b-9e96-2ae38f54d826",
   "metadata": {},
   "source": [
    "**methods**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c53b2218-f124-4fbb-ae68-476254fc3984",
   "metadata": {},
   "outputs": [],
   "source": [
    "one = np.array([1 , 3 , 4 , 634 , 2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "b488d3e4-5441-4c8c-a6fd-1a8df8468abf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(3)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "one.argmax()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c595900f-c902-4e32-9740-a429fe5c2bf9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "one.argmin()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "89e3bd86-5b51-4468-9995-05b9a0c7bdb7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 4, 1, 2, 3])"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "one.argsort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "2cb67548-0292-4ac7-8c01-c2e5bfd72431",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(0)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.argmin()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5b40e303-56aa-45eb-973b-8f65f62a552f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(8)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.argmax()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "fd573ca7-07e5-4183-876a-11d591cec941",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0])"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.argmin(axis=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "ab63301d-2888-45ff-9df3-d42e8f57e146",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 2, 2])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.argmax(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "5dadbbb5-abc7-45b9-adba-9bd6599fe9a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.argmin(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "7d07a824-2c98-4a44-b17e-585cbd6849bc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 2, 2])"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.argmax(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e80e6e28-a325-48de-8f56-819655737e0b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 1, 2],\n",
       "       [0, 1, 2],\n",
       "       [0, 1, 2]])"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.argsort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "c345c135-2068-436d-8863-cb0bb28005ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 0, 0],\n",
       "       [1, 1, 1],\n",
       "       [2, 2, 2]])"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.argsort(axis=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "b7b38eaf-f27d-40b5-a2b5-6d0b86fe4c5f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 1, 2],\n",
       "       [0, 1, 2],\n",
       "       [0, 1, 2]])"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr.argsort(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "6686b3e2-026a-4ecd-8624-5e75ee8bbdc4",
   "metadata": {},
   "outputs": [],
   "source": [
    "a1=np.array([1 , 2 , 3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "b90cb930-f2bf-41df-8bd7-27f81a2933cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "a2=np.array([4 , 5 , 6])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "5d840ce4-db39-4e4e-8dfe-9ea3c0756bea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([5, 7, 9])"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a1+a2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "970dd115-6a14-4427-b303-e2ec132ed044",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6]"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[1 ,2 , 3]+[4 , 5 , 6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "3182412a-7d78-4434-80f3-f74a22c2ee66",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr1=np.array([[1 , 2 , 3],[4 , 5 , 6] , [7 , 8 , 9]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "d2ae3c6c-dfca-4e6f-9b69-52d803280ae1",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr2=np.array([[9 , 8 , 7],[6 , 5 , 4],[3 , 2 , 1]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "5641938d-4473-46fd-8c77-47537bed4a86",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr3=arr1+arr2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "f2bd3125-ad96-4b43-ac7f-6cc300f134b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 9, 16, 21],\n",
       "       [24, 25, 24],\n",
       "       [21, 16,  9]])"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1*arr2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "5f9e393c-8fed-498b-8070-41476e76e4fb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[10, 10, 10],\n",
       "       [10, 10, 10],\n",
       "       [10, 10, 10]])"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "bb200219-f789-4f71-966a-e75936fbb082",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3.16227766, 3.16227766, 3.16227766],\n",
       "       [3.16227766, 3.16227766, 3.16227766],\n",
       "       [3.16227766, 3.16227766, 3.16227766]])"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.sqrt(arr3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "e8e20c36-992e-4063-9bf5-24a836b09f20",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(1)"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1.min()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "b2a8394b-b55f-4495-92dd-960770675792",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(9)"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1.max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "27303ef5-44ce-4b87-b386-6f29c4df5d96",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([1, 1, 1, 2, 2, 2]), array([0, 1, 2, 0, 1, 2]))"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.where(arr1>3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "e907ca84-c471-4822-849b-12e7269be2c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "2279e981-3f31-4243-bdb2-64144ab39ccf",
   "metadata": {},
   "outputs": [],
   "source": [
    "x1=[1 , 2, 3 , 4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "60828779-1a3c-4acb-94ba-8e1db78d0973",
   "metadata": {},
   "outputs": [],
   "source": [
    "x2=np.array(x1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "22720e97-5f0c-4a64-8038-cb58552f778b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4])"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "b6db3234-2aed-43b6-974d-2afb86f03170",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "112"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sys.getsizeof(1)*len(x1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "f4630ea7-f734-4206-9883-049b8f725814",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "32"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x2.itemsize*x2.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7cafbc15-4fdb-413d-8f66-f205753a1a7b",
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
