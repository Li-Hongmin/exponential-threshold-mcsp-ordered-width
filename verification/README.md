Supplement to "Tight Ordered Width for Exponential-Threshold MCSP" (version 3).

check_lemma3.py (Python 3, standard library): for each of the pairs (n,r) in {(4,1),(4,2),(4,3),(5,2),(5,3),(6,2),(6,3)} it samples twenty balanced sets P in F_2^n (fixed seed), enumerates all r-dimensional row subspaces for each sample, and checks in exact rational arithmetic that the minimum and the average number of monochromatic fibres are at most 2^r(2^r-1)/(2^n-1), as in Lemma 3.

Coverage: sampled partitions, exhaustive over subspaces for each sample. It does not exhaust all balanced partitions, does not compute Fourier coefficients, and does not check the Parseval identity in the proof directly. It is a numerical sanity check of Lemma 3 at small sizes, not a proof and not evidence for the asymptotic theorem.

CONTENTS.sha256 lists the SHA-256 digests of README.md and check_lemma3.py (verify with shasum -a 256 -c CONTENTS.sha256).
