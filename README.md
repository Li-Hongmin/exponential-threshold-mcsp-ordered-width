# Tight Ordered Width for Exponential-Threshold MCSP

[![verify](https://github.com/Li-Hongmin/exponential-threshold-mcsp-ordered-width/actions/workflows/verify.yml/badge.svg)](https://github.com/Li-Hongmin/exponential-threshold-mcsp-ordered-width/actions/workflows/verify.yml) [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.24054545-blue)](https://doi.org/10.5281/zenodo.24054545)

**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo) · ORCID [0000-0003-0228-0600](https://orcid.org/0000-0003-0228-0600)

Main result of the manuscript: for every coordinate order, the minimum middle-layer width W of an ordered branching program computing MCSP at threshold S = 2^{μn} satisfies log₂ W = (1+o(1)) S log₂ S, simultaneously for deterministic, nondeterministic, parity and field-weighted ordered models.

- Manuscript on rStation: <https://rstation.ai/problems/computer_science/papers/2/v3> (version 3)
- Archived on Zenodo: concept DOI [10.5281/zenodo.24054545](https://doi.org/10.5281/zenodo.24054545) (all versions); this repository mirrors version 3, DOI [10.5281/zenodo.24054558](https://doi.org/10.5281/zenodo.24054558)

## Contents

- `paper/paper.md`, `paper/exponential-threshold-mcsp-ordered-width.pdf` — the manuscript (version 3).
- `verification/` — the supplement of that version, unpacked unchanged; its own README describes each file.
- `.github/workflows/verify.yml` — reruns every check below on each push.

## What the programs check

| Check | Command (run inside `verification/`) |
|---|---|
| Lemma 3: monochromatic-fibre bound in exact arithmetic | `python check_lemma3.py` |

The programs check the finite and exact computations used in the manuscript; the mathematical arguments are those written in the paper.

## Reproducing

```sh
cd verification
sha256sum -c CONTENTS.sha256      # or: shasum -a 256 -c CONTENTS.sha256
python check_lemma3.py
```

Requirements: Python 3.9+. Run the commands from a copy if you want to keep the recorded outputs untouched.

## Cite

```bibtex
@misc{li2026exponentialthresholdmcsp,
  author    = {Li, Hongmin},
  title     = {Tight Ordered Width for Exponential-Threshold MCSP},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.24054545},
  url       = {https://doi.org/10.5281/zenodo.24054545}
}
```

## License

Manuscript and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code: MIT (see `LICENSE`).
