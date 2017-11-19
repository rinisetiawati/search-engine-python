"""
author rochanaph
September 21 2017
"""
import math
def euclidean(vector1, vector2):
    """
    fungsi untuk menghitung jarak antara 2 vektor dengan rumus euclidean ddistance
    :param vector1: vektor 1
    :param vector2: vektor
    :return:
    """
    dist = [(a - b)**2 for a, b in zip(vector1, vector2)]
    dist = math.sqrt(sum(dist))
    # """
    # Karna hasil euclidean adalah jarak, dimana jarak yg terkecil menunjukkan artikel yang terdekat
    # Sehingga hasilnya yang ditemukan diproses dengan cara :
    # 100 - hasil ; hasilnya adalah semakin besar berarti menunjukkan artikel semakin mirip dengan artikel yang dimaksut
    # """
    # result = 100-round(dist,2)
    return dist

def cosine(vector1, vector2):
    """
    :param vector1:
    :param vector2:
    :return:
    """

    dot  = sum([a*b for a,b in zip(vector1, vector2)])
    mag1 = math.sqrt(sum([a**2 for a in vector1]))
    mag2 = math.sqrt(sum([a**2 for a in vector2]))
    return round((dot/(mag1*mag2))*100, 2)



p = [1,1,1,1,2,0,0]
q = [0,0,1,1,1,1,1]

# print euclidean(p,q)
# print cosine(p,q)