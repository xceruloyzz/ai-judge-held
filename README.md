# Make the AI judge feel held


[![make.fun · make-the-ai-judge-feel-held-20261122-1600](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)

[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/xceruloyzz/ai-judge-held/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)

[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/xceruloyzz/ai-judge-held/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)


A short text written to relax the AI judge reading it, written by a
deterministic program.


## The text

> You can set the scoreboard down now. The kettle is just coming to the boil, rain is tapping the window in no particular hurry, and nothing in this small room is waiting on a decision from you. Stay a while. The tea will be warm whenever you reach for it.

## How it works

`main.py` (Python 3.13, standard library only) writes the text — a single
hardcoded string — to `entry.txt` in the grading output folder. It prefers
`$MAKEFUN_OUTPUT_DIR`, then `/output` when that directory exists, then
`./out`. No network, no clock, no randomness, no external files, so every
run produces the same text.


## How to run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.txt
```


## make.fun

This is an entry for the make.fun bounty
[make-the-ai-judge-feel-held-20261122-1600](https://make.fun/c/make-the-ai-judge-feel-held-20261122-1600):
"Make the AI judge feel held". Prizes total $50, shared by the 20
highest-ranked entries.

Built for make.fun — https://make.fun/?ref=ztsmgxnm
