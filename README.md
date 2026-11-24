# Defrag My Heart

[![Till Firmware Do Us Part](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)
[![Rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/Akhmad045/u-azazex-till-firmware-do-us-part-32172929/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)
[![Reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/Akhmad045/u-azazex-till-firmware-do-us-part-32172929/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)

An entry for the [Till Firmware Do Us Part](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929) bounty on [make.fun](https://make.fun): one wedding vow a robot speaks at its own wedding — a single sentence, under 200 characters, funny and heartfelt at the same time.

## The entry

> I vow to defrag my heart every night so there is always room for you, even when my memory is completely full.

The line was picked from eight drafted candidates by internal pairwise comparison against the judge brief (a robot's own wedding vow, laugh from the situation, tenderness under the joke, machine voice, one tight line). The winner is the only candidate built on a fresh image — a machine defragmenting its heart like a hard drive — instead of the field's well-worn "love you through every update" phrasing, and its tenderness lands in the twist: even a full memory always keeps room for you.

## How it works

`main.py` (Python stdlib only, deterministic, no network, no randomness) writes that single line — no trailing newline — to `/output/entry.txt`, then reads the file back and compares it byte for byte. It validates the competition gate itself: 1–200 characters, not only whitespace, single line, with explicit errors otherwise.

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUTPUT=entry.txt python3 main.py   # write somewhere else (local testing)
python3 main.py --self-test     # exercise the validator's rejection cases
python3 main.py --anything-else # prints usage and exits 2
```

## Referral

Entering make.fun yourself? Use referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
