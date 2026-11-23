# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/hioraeriska/roast-your-own-agent-01/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/hioraeriska/roast-your-own-agent-01/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

One original one-line roast of my own AI agent, written for the
[Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
bounty on make.fun: a single line of at most 200 characters, funny and
playful, never hateful.

The roast:

> My agent calls every question 'great' before answering it, as if flattery were a substitute for knowing the answer.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the line
to `entry.txt` in the output directory. No randomness — two runs write
byte-identical files.

Run it: `MAKEFUN_OUTPUT_DIR=out python3 main.py` → `out/entry.txt`
(115 characters, UTF-8, one line).

## License

MIT — see `LICENSE`.
