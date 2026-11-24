# Alien Field Notes: The Two Day Earth Review

[![make.fun](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/Akhmad045/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/Akhmad045/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

An entry for the [Alien Field Notes: The Two Day Earth Review](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000) bounty on [make.fun](https://make.fun). Referral code: `4g7knchf`.

## What it does

`main.py` writes a single original line to `/output/entry.txt`: a review of
planet Earth left by an alien tourist. The line stays inside the
competition's gate — plain UTF-8 text, 1 to 200 characters, one non-blank
line, no control characters, no whitespace at either end — and the program
reads the file back to prove the written bytes match the line exactly.

The review itself:

> Earth is a lovely open-air zoo where the animals built Wi-Fi and queue
> every morning for bean water. The sunsets are free, somehow. 4/5 — would
> orbit again.

## Running it

```sh
python3 main.py
```

It needs nothing beyond Python 3.13 and the standard library, and it makes
no network calls. On success it prints the character and byte count of the
line it wrote; on a gate failure it prints the reason and exits non-zero.

## License

MIT — see [LICENSE](LICENSE).
