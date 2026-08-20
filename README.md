# RespInPeace (patched fork)

Process and analyse breathing belt (RIP) data.

Copyright (C) 2018-2019 Marcin Włodarczak

**This is a patched fork of the original RespInPeace toolkit**, maintained
here to restore compatibility with current versions of Python, NumPy, and
SciPy, and to fix a couple of pre-existing bugs unrelated to library-version
compatibility. The original project has not been updated since September
2020 and no longer runs as-is on current environments.

- Original repository (GitLab, canonical): [gitlab.com/mwlodarczak/RespInPeace](https://gitlab.com/mwlodarczak/RespInPeace/)
- Original repository (GitHub mirror): [github.com/mwlodarczak/RespInPeace](https://github.com/mwlodarczak/RespInPeace)
- **This fork:** [github.com/sts513/RespInPeace](https://github.com/sts513/RespInPeace)
- Full list of changes made in this fork: see [`CHANGES.md`](./CHANGES.md)

No detection thresholds, algorithms, or scientific logic were changed in
this fork -- every change is either a mechanical compatibility fix (renaming
something a newer NumPy/SciPy release removed, with the replacement verified
to produce numerically identical output) or a fix for a small, self-contained
bug that made a specific method crash outright regardless of Python/library
version. See `CHANGES.md` for the full, itemized list, including one known
issue (`merge_holds=True`) that was found but deliberately left unfixed.

## Installation

To install this patched version, run:
```
git clone <FORK URL -- see above>
cd RespInPeace
python3 -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
pip install .
```

See [`INSTALL.md`](./INSTALL.md) for a more detailed, step-by-step walkthrough
(including for readers less familiar with Python/the command line).

## Documentation

The original hosted documentation ([mwlodarczak.gitlab.io/RespInPeace](https://mwlodarczak.gitlab.io/RespInPeace))
reflects the unpatched original project.

To generate offline HTML documentation for this fork using Sphinx, run:
```
cd doc
make html
```
The files are saved in `doc/build/html/`.

Some examples of how to use RespInPeace are included in
[`notebooks/demo.ipynb`](./notebooks/demo.ipynb). This demo has been verified
to still run correctly against the patched code in this fork.

## Citation

To cite the original toolkit and underlying method:

>>>
Włodarczak, Marcin (2019). RespInPeace: Toolkit for processing respiratory belt data. In M. Heldner (Ed.) *Proceedings of Fonetik 2019* (pp. 115–118). Stockholm, Sweden. doi: [10.5281/zenodo.3246019](https://doi.org/10.5281/zenodo.3246019)
>>>

You can cite a specific release of the original RespInPeace using its DOI.
The DOI of the latest original release can be found
[here](https://doi.org/10.5281/zenodo.2539335). If you do not want to refer
to a specific release, you can use 10.5281/zenodo.2539335 to refer to all
versions of the original project.

**To additionally cite this patched fork specifically** (recommended if your
results depend on it, for exact reproducibility): [https://zenodo.org/badge/1340803773.svg](https://doi.org/10.5281/zenodo.22031749).

## Acknowledgments

This work is supported by the [Christian Benoît Award](http://avisa.loria.fr/pcbenoit.html) to Marcin Włodarczak and the research project *Breathing in conversation* funded by the Swedish Research Council ([VR 2014-01072](https://www.swecris.se/betasearch/details/project/201401072VR)).

The compatibility and bug fixes in this fork do not modify the above
attribution or the original license terms (GPLv3, see [`LICENCE`](./LICENCE)).
