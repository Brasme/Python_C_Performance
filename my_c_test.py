from time import time
from ctypes import CDLL, c_float, c_int
from inspect import getsourcefile
from os.path import abspath

path=abspath(getsourcefile(lambda:0)).rsplit('/',1)[0]
so_file = path+'/build/'+"libc_math.so"
m = CDLL(so_file)

m_fsqr = m.fsqr
m_fsqr.argtypes = [c_float]
m_fsqr.restype = c_float

m_fsqr_n = m.fsqr_n
m_fsqr_n.argtypes = [c_float,c_int]
m_fsqr_n.restype = c_float

m_fisqrt = m.fisqrt
m_fisqrt.argtypes = [c_float]
m_fisqrt.restype = c_float

m_fisqrt_n = m.fisqrt_n
m_fisqrt_n.argtypes = [c_float,c_int]
m_fisqrt_n.restype = c_float

print("InvereSqrt(4)=",m_fisqrt(4))
print("Sqr(4)       =",m_fsqr(4))

N=1000000

value=10.0

v=value
t0=time()
for i in range(N):
    v=m_fisqrt(v)
t1=time()
print("Time c_fisqrt  =",(t1-t0))

v=value
t0=time()
v=m_fisqrt_n(v,N)
t1=time()
print("Time c_fisqrt_n=",(t1-t0))

v=value
t0=time()
for i in range(N):
    v=v ** -0.5
t1=time()
print("Time v**-0.5   =",(t1-t0))

t0=time()
for i in range(N):
    v=m_fsqr(value)
t1=time()
print("Time c_fsqr  =",(t1-t0))

t0=time()
v=m_fsqr_n(value,N)
t1=time()
print("Time c_fsqr_n=",(t1-t0))

t0=time()
for i in range(N):
    v=value*value
t1=time()
print("Time v*v     =",(t1-t0))



