# The World in One Day — 23 November 2026

[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/ranstar04/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/ranstar04/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

A one-page newspaper front page that sums up Monday 23 November 2026
in six stories, drawn as a single 1024×1024 image.

Entry for the [news-image-20261123 bounty](https://make.fun/bounty/news-image-20261123)
on [make.fun](https://make.fun) — join via my referral:
https://make.fun/r/dn9c31df

## The six stories

1. **Climate — COP31 collapses.** UN climate talks end with no deal:
   the EU and others reject any text without language on phasing out
   fossil fuels.
2. **Strait of Hormuz — tankers under fire.** At least three oil
   tankers are struck near the strait; two more hit naval mines.
   Attacks on shipping there are at their highest since the war began.
3. **Libya — drone strike at sea.** Suspected Ukrainian sea drones hit
   the Russian corvette Merkury at the Benghazi naval base; the ship
   capsizes and 10 people are injured.
4. **Ukraine — flat hit in Dymer.** A Russian drone hits a five-storey
   apartment block north of Kyiv; 2 people are killed and 11 are
   missing, including two children.
5. **Space — Mercury orbit.** After an eight-year journey, the
   European-Japanese BepiColombo spacecraft enters orbit around
   Mercury — only the second mission ever to do so.
6. **Indonesia — factory fire.** A fire at a candy factory in Cikande,
   Banten; rescuers recover 24 body bags and dozens of workers are
   still missing.

## How it is built

`draw_poster.py` draws `entry.png` locally with Pillow (run once,
before submitting). `main.py` is standard-library only: it copies
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, so both grader runs
write byte-identical output.

```sh
python3 draw_poster.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
