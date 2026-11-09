"""Small check of Lemma 3. For twenty sampled balanced sets P in F_2^n at each listed (n,r), enumerate
all r-dimensional row subspaces (surjective linear maps L: F_2^n -> F_2^r up to fibre structure) and check,
in exact rational arithmetic, that both the minimum and the average number of monochromatic fibres are at
most 2^r(2^r-1)/(2^n-1). Partitions are sampled, not exhausted; Fourier coefficients are not computed."""
import itertools, random
from fractions import Fraction
def subspaces(n,r):
    seen=set()
    vecs=range(1,2**n)
    for basis in itertools.combinations(vecs,r):
        span={0}
        for b in basis: span|={s^b for s in span}
        if len(span)==2**r:
            key=frozenset(span)
            if key not in seen: seen.add(key); yield basis
def dot(a,x): return bin(a&x).count('1')&1
random.seed(1)
for n,r in [(4,1),(4,2),(4,3),(5,2),(5,3),(6,2),(6,3)]:
    for trial in range(20):
        pts=list(range(2**n)); random.shuffle(pts); P=set(pts[:2**(n-1)])
        tot=Fraction(0); cnt=0; best=None
        for basis in subspaces(n,r):   # rows of L span K^perp
            fib={}
            for x in range(2**n):
                lab=tuple(dot(b,x) for b in basis); fib.setdefault(lab,set()).add(x in P)
            B=sum(1 for v in fib.values() if len(v)==1)
            tot+=B; cnt+=1; best=B if best is None else min(best,B)
        bound=Fraction(2**r*(2**r-1),2**n-1)
        assert best<=bound, (n,r,best,bound)
        assert tot/cnt<=bound, (n,r,tot/cnt,bound)
print("Lemma 3 inequalities hold on all sampled partitions and all enumerated subspaces.")
