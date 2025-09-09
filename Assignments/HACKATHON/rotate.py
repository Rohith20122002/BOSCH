def rotate(d, arr):
    n = len(arr)
    d = d % n  
    print(d)
    print(arr[d:] + arr[:d])
a=[1,2,3]
rotate(2,a)