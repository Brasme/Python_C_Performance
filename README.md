# Python_C_Performance

Simple test of performance calling C functions from Python

Note - assumes linux (loads .so file)

1) Run cmake to build the build/libc_math.so
2) Run the my_c_test

# Typical output

    InvereSqrt(4)= 0.49915358424186707
    Sqr(4)       = 16.0
    Time c_fisqrt  = 0.25681304931640625
    Time c_fisqrt_n= 0.005357265472412109
    Time v**-0.5   = 0.043802499771118164
    Time c_fsqr  = 0.2603158950805664
    Time c_fsqr_n= 0.0016047954559326172
    Time v*v     = 0.046372175216674805

This shows that single c calls have a significant overhead. But - 1000000 iterations inside C outperforms Python