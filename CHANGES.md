# Changes in this patched version

Original project: https://github.com/mwlodarczak/RespInPeace
(last updated 2020-09-25). Unmaintained since. The fixes below fall
into two groups: (1)-(4) restore compatibility with current
Python/NumPy/SciPy without changing any calculations or logic, and
(5)-(6) fix genuine pre-existing bugs in the original code that made
two specific methods crash whenever they were called, regardless of
Python/library version.

## Compatibility fixes (no behaviour change)

1. `peakdetect.py`: `from scipy import fft, ifft` -> `from scipy.fft
   import fft, ifft`. SciPy removed the old top-level aliases; this
   points to the modern replacement module. Verified numerically
   identical output on test data.

2. `rip.py`: `.astype(np.int)` -> `.astype(np.int64)` (4 occurrences).
   `np.int` was a deprecated alias for Python's built-in `int` and was
   removed in NumPy 1.24+. `np.int64` is a direct, explicit equivalent.

3. `peakdetect.py`: `np.Inf` -> `np.inf` (7 occurrences). Same
   constant, NumPy 2.0 removed the capitalized alias.

4. `setup.py`: switched from `distutils.core.setup` to
   `setuptools.setup`. `distutils` was removed in Python 3.12;
   `setuptools` is the standard drop-in replacement. Also added
   `install_requires` so `pip install .` pulls in dependencies
   automatically.

## Pre-existing bug fixes (present in the original code, unrelated to
## library version rot -- these code paths were apparently never
## exercised/tested by the original author)

5. `rip.py`: added `import csv` at the top of the file. `Resp.save_resp
   (..., filetype='table')` calls `csv.writer(...)` but the module was
   never imported, so this call always raised `NameError`. Confirmed
   fixed: saving a sample-by-sample table now works.

6. `rip.py`, `calibrate_vc()`: changed `self.samples.idt[...]` to
   `self.idt[...]` (2 occurrences). `self.samples` is a plain NumPy
   array with no `.idt` attribute -- `.idt` is a property on `Resp`
   itself (a time-based indexer over `self.samples`). The original
   code always raised `AttributeError` when called. Confirmed fixed:
   `calibrate_vc()` now runs and rescales the signal as documented.

Both bugs were found by (a) running `pyflakes` over the whole codebase
to catch undefined-name errors statically, and (b) exercising every
public method against the bundled demo data. No detection thresholds,
algorithms, or numerical logic were changed by any of these six fixes.

## Known remaining issue (not fixed -- flagged for visibility)

`Resp.save_annotations(..., merge_holds=True)` is still broken. It
calls `self.merge_holds(...)`, but the method is actually named
`_merge_holds` (leading underscore) -- a simple rename would fix the
call, but the `_merge_holds` method itself has a deeper logic bug: it
immediately overwrites its own `cycles` argument with a fresh empty
`tgt.IntervalTier()`, so it always returns an empty tier regardless of
input. Making `merge_holds=True` actually work as intended would
require rewriting that merge logic, not just fixing a name, since the
original implementation appears to have never worked/been tested.
`merge_holds` defaults to `False`, and this repo's own scripts never
set it to `True`, so it does not affect normal use of the library.

Verified against the bundled `notebooks/resp.wav` demo file: baseline
removal, breath-cycle/hold detection, range/REL estimation, feature
extraction, calibration, table export, and TextGrid/EAF export all run
end-to-end and produce physiologically plausible output (see
conversation for details).
