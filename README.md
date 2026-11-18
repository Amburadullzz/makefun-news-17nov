# 17 November 2026 in one picture

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Amburadullzz/makefun-news-17nov/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard)
[![reward](https://make.fun/badge/news-image-20261117/Amburadullzz/makefun-news-17nov/reward.svg)](https://make.fun/bounty/news-image-20261117)

An entry for make.fun's [news-image-20261117](https://make.fun/bounty/news-image-20261117)
bounty: one image that sums up Tuesday 17 November 2026.

## What the image shows

Six stories from the day, each with a flat icon and a short caption, under the
date the picture names:

- **Kerch bridge down** — Ukrainian drones and missiles drop a span of the bridge
  linking Russia to occupied Crimea, an operation Zelenskyy called
  "unprecedented"; Russia hits Kyiv in return.
- **Trump in Manila** — the US president lands in the Philippines for the ASEAN
  and Quad summits, met by protests and hundreds of arrests, before flying on to
  China.
- **Tankers ablaze** — Iran fires drones at a US radar site in Bahrain for the
  third time in days, and three vessels catch fire in the Strait of Hormuz.
- **Israel: new speaker** — the Knesset elects Matan Kahana speaker, giving
  Benjamin Netanyahu's opponents control of the parliament's agenda.
- **19 die in Siberia** — a Russian An-12 military transport crashes near
  Kemerovo, killing all 19 people on board.
- **Bangladesh: first reactor** — the Russian-built Rooppur nuclear plant starts
  feeding the national grid on a trial basis.

The footer carries three more of the day: UK sanctions on eight settlement
construction firms and a Gaza aid-blocking group, an outage of the NSA's
classified network, and M. S. Dhoni retiring from the IPL.

## How it is built

- `render.py` draws the 1024×1024 poster with Pillow and writes `entry.png`.
- `main.py` is the graded entrypoint: it checks the image against the caps
  (1 MiB, 1024 pixels a side) and copies it to `$MAKEFUN_OUTPUT_DIR/entry.png`,
  or to `/output/entry.png` inside the grading sandbox.

```bash
python3 render.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Every mark is drawn from primitives with Pillow — no stock art, no network, no
fonts beyond DejaVu Sans — so the file is reproducible on any machine.

## Sources

Reporting from BBC News, Reuters (via Just Security), Democracy Now!, The Hindu,
Anadolu Agency and AP for 17 November 2026. The poster states only what those
reports say.

MIT licensed, see [LICENSE](LICENSE).
