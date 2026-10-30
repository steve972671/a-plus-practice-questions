# CompTIA A+ original practice quizzes (questions only)

**These are homemade practice quizzes for personal study.**

They are **not**:
- CompTIA exam dumps
- pirated or leaked official exam questions
- a "brain dump" of live exam content

They were written as original practice items (Core 1 / Core 2 style) for studying CompTIA A+ objectives. CompTIA owns its trademarks and official exams; this repo is an unofficial study aid only.

## Contents
- `core1-full-90-a.json` / `core2-full-90-a.json` - ~90-question practice sets (stems + choices only)
- shorter `*-practice-test-a.json` packs

Answer keys and integrity hashes live in a **separate private** repository (`a-plus-practice-answers`).

## Taking a quiz

### In a browser (`quiz.html`)
From this folder run `python -m http.server 8000`, then open http://localhost:8000/quiz.html and pick a quiz from the dropdown. (Opening `quiz.html` directly also works; use the file picker to load a quiz JSON.)
One question at a time, A-D buttons, Prev/Next, progress bar. Correctness stays hidden until you click Finish and load an answer key file from your own computer.

### In a terminal (`quiz.py`, Python 3, no extra packages)
```
python quiz.py --quiz core1-full-90-a.json
python quiz.py --quiz core1-full-90-a.json --key path/to/core1-full-90-a.answerkey.json
```
Options: `--shuffle` randomizes order. Enter A-D, S to skip, Q to quit. With `--key` you get a score, per-domain breakdown, and missed questions at the end; without it, just your picks.

Answer keys are **not** in this repo. They live in the private `a-plus-practice-answers` repo; neither runner contains any answers.

## License / use
Personal study use. Do not represent these as official CompTIA materials.
