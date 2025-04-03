{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "98b83dcb-d053-4060-8452-e9faf610c3a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "be5d5e59-d183-4a6a-9add-ff2d785f9675",
   "metadata": {},
   "outputs": [],
   "source": [
    "myarr=np.array([[1 , 2 , 3 , 4]] , np.int64)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b75b7e67-768d-4a20-bbb6-a12cc31df62a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4])"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myarr[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "10b2281d-b559-4461-89a3-4a528769f943",
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
    "myarr.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "99e0dd7e-73fc-4d03-90a6-f04087e5e6ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 4)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myarr.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "de62534f-dc57-4e82-b8a2-458208dfec98",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(2)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myarr[0 , 1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a36fcc60-7019-41c8-8dd8-c2355ec092ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "myarr[0,1]=64"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e51aa6ac-32b3-4d75-90f6-3189e31676f9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1, 64,  3,  4]])"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myarr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6ccc9c5-c6a1-4c5f-941f-1ddd67ba8084",
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
