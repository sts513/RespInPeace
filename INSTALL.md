# Installing RespInPeace (patched fork)

This is a patched fork of the original RespInPeace toolkit by Marcin
Wlodarczak (https://github.com/mwlodarczak/RespInPeace), updated to run
on current versions of Python/NumPy/SciPy, with a couple of additional
pre-existing bugs fixed along the way. See CHANGES.md for the full,
itemized list of exactly what was changed and why.

## 1. Make sure Python 3 is installed

Open a terminal (Terminal on Mac, PowerShell or Command Prompt on Windows)
and run:

    python3 --version

If that fails, try `python --version` instead. You need Python 3.9 or
newer. If you don't have Python at all, install it from python.org first.

## 2. Get a copy of this repository

Either clone it with git:

    git clone <this fork's URL>
    cd RespInPeace

or download it as a zip (green "Code" button on GitHub > "Download ZIP")
and unzip it somewhere convenient, e.g. your Desktop or Documents folder.

Then open a terminal *inside* that folder:

- Mac: right-click the folder in Finder > "New Terminal at Folder" (or
  `cd` into it manually)
- Windows: open the folder in File Explorer, click the address bar, type
  `cmd`, press Enter

## 3. Create a virtual environment (recommended)

This keeps RespInPeace's dependencies separate from anything else on your
computer, so it can't conflict with other Python projects.

    python3 -m venv venv

Then activate it:

- Mac/Linux: `source venv/bin/activate`
- Windows:    `venv\Scripts\activate`

Your terminal prompt should now start with `(venv)`. You'll need to run
the activate command again each time you open a new terminal to use
RespInPeace.

## 4. Install RespInPeace and its dependencies

With the virtual environment active:

    pip install .

This reads `setup.py` and installs RespInPeace plus everything it needs
(NumPy, SciPy, pandas, Matplotlib, tgt).

## 5. Check it worked

Still with `(venv)` active, run:

    python3 -c "import rip; print('RespInPeace loaded OK')"

You should see `RespInPeace loaded OK` with no errors.

## 6. Try it on the included example

    cd notebooks
    python3 -c "
from rip import Resp
resp = Resp.from_wav('resp.wav')
resp.remove_baseline(method='savgol')
resp.find_cycles(include_holds=False)
resp.find_holds()
resp.save_annotations('resp.TextGrid', tiers=['cycles', 'holds'])
print('Done -- wrote resp.TextGrid with', len(resp.inhalations), 'breath cycles and', len(resp.holds), 'holds')
"

If that prints a "Done" line, everything is working. `resp.TextGrid` can
then be opened in Praat.

## Using it on your own data

The general pattern (see `notebooks/demo.ipynb` for the full walkthrough):

    from rip import Resp

    resp = Resp.from_wav('your_recording.wav')
    resp.remove_baseline(method='savgol')
    resp.find_cycles(include_holds=False)
    resp.find_holds()
    resp.save_annotations('your_recording.TextGrid', tiers=['cycles', 'holds'])

## If something goes wrong

- "command not found: python3" -> Python isn't installed, or isn't on
  your PATH. Reinstall from python.org and make sure to check "Add
  Python to PATH" during setup (Windows).
- "No module named rip" -> you're not in the activated virtual
  environment, or step 4 didn't complete. Re-run
  `source venv/bin/activate` (or the Windows equivalent) and then
  `pip install .` again.
