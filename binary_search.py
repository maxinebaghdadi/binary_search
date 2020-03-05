#!/bin/python3

def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT: 
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    if len(xs) == 0:
        return None

    left = 0
    right = len(xs)-1

    val = 0

    def go(left,right):
        mid = (left+right)//2
        if val < xs[mid]:
            if xs[mid-1] < val: #checking for negative
                if left == mid:
                    return mid
                left = mid
            else: 
                right = mid-1
        if val > xs[mid]:
            left = mid+1
        if val==xs[mid]:
            index = mid + 1 #returning closest to 0 in sorted list 
            return index
        if left >= right:
            if xs[mid] > val:
                return mid
            else:
                if xs[mid-1] < val:
                    return None
                index = mid + 1 
                return index
        return go(left,right)
    return go(left,right)
    

def goofy(xs,x):
    
    left = 0
    right = len(xs)-1
    
    def go(left,right):
        mid = (left+right)//2
        if left >= right:
            if len(xs) == 0:
                return 0
            if x == xs[mid]:
                return mid
            else:
                return 0
        if x > xs[mid]:
            right = mid-1
        if x < xs[mid]:
            left = mid+1
        if x == xs[mid]:
            if xs[mid-1] == x:
                right = mid
            else:
                return mid
        return go(left,right)
    return go(left,right)

def dominant(xs,x):
    
    left = 0
    right = len(xs)-1
    
    def go(left,right):
        mid = (left+right)//2
        if left >= right:
            if len(xs) == 0:
                return 0
            if x == xs[mid]:
                return mid + 1
            else:
                return 0
        if x > xs[mid]:
            right = mid-1
        if x < xs[mid]:
            left = mid+1
        if x == xs[mid]:
            if xs[mid+1] == x:
                if mid == len(xs) - 2: 
                    return mid + 2
                elif xs[mid+2] < x:
                    return mid + 2
                else: 
                    left = mid
            else:
                return mid + 1
        return go(left,right)
    return go(left,right)

def count_repeats(xs, x):
    
    smallest = goofy(xs,x)
    biggest = dominant(xs,x)
    
    difference = biggest - smallest
    
    return difference


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''

    def go(lo,hi):
        m1 = lo + (hi-lo)/3
        m2 = lo + ((hi-lo)/3)*2
        if abs(lo-hi) < epsilon:
            return (hi+lo)/2
        if f(m2) < f(m1):
            lo = m1
        if f(m2) > f(m1):
            hi = m2
        if f(m2) == f(m1):
            lo = m1
            hi = m2
        return go(lo,hi)
    return go(lo,hi)


