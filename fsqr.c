float fsqr( float v)
{
    return v*v;
}

float fsqr_n( float v0, int n )
{
    float v=fsqr(v0);
    n--;
    while (n>0) {
        v=fsqr(v0);
        n--;
    }
    return v;
}