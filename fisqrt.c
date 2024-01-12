float fisqrt( float v )
{
    int i;
    float x2, y;
    const float threehalfs = 1.5F;

    x2 = v * 0.5F;
    y  = v;

    i  = * ( long * ) &y;                      /* float to int */
    i  = 0x5f3759df - ( i >> 1 );              /* int arithmetic */
    y  = * ( float * ) &i;                     /* int back to float */

    y  = y * ( threehalfs - ( x2 * y * y ) );  /* Newton's method */
    return y;
}

float fisqrt_n( float v, int n )
{
    while (n>0) {
        v=fisqrt(v);
        n--;
    }
    return v;
}