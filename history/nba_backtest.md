# Market backtest, NBA 2023-24 to 2025-26 (3,969 games)

Built 2026-11-18 from The Odds API historical odds. Snapshots: 15 minutes before tip (close) and the morning of game day (am). 10 books. Graded against ESPN box scores: 15.9M rungs, with 224K voided because the player wasn't in the box score. Full tables are in `nba_backtest.json`.
ROI is the return of a flat $1 single bet at the posted price. "Games" means distinct player-games (or team-games), which is the honest sample size, because rungs on one ladder move together. The 2025-26 season is partial (through mid-November 2026).

## Headline: every NBA market costs more than its NFL counterpart
Nothing on the board is reliably +EV. Team markets cost about 3-5% per leg; prop alt ladders cost about 7-9%. The NFL figures were about 1-3% for team markets and 7-10% for props.

## Cost per leg at DraftKings close, legs priced -150 to -500
| Market | Hit % | Implied % | ROI | Games |
|---|---|---|---|---|
| Moneyline (h2h) | 68.2 | 70.8 | -3.6% | 2,280 |
| Rebounds main line (2-sided) | 59.3 | 61.5 | -3.6% | 10,576 |
| Alt totals | 67.5 | 70.5 | -4.3% | 7,864 |
| Threes main line (2-sided) | 61.7 | 64.5 | -4.3% | 23,564 |
| Assists main line (2-sided) | 59.5 | 62.3 | -4.5% | 11,027 |
| Alt spreads | 68.4 | 72.2 | -5.3% | 7,862 |
| Assists alt ladder | 66.3 | 71.4 | -7.2% | 27,100 |
| Points alt ladder | 65.1 | 70.3 | -7.5% | 45,957 |
| Rebounds alt ladder | 66.3 | 71.9 | -7.9% | 42,121 |
| Threes alt ladder | 66.0 | 72.5 | -9.0% | 29,424 |

Main game lines near even money at DK: totals -0.2%, team totals -2.5%, spreads -3.6% (-110..+120).
**Two-sided main prop lines cost about half as much as the alt ladders** (-3.6 to -4.5% vs -7.2 to -9.0%). When a prop is used, prefer the main line (or the rung nearest it) to a deeper ladder rung. The points main line has too few priced rungs (194) to judge.
Alt totals get cheaper the shorter they are (-500..-300: -2.7%; -1000..-500: -1.3%), but those prices pay very little.
Longshots are worst: ladder rungs above +200 lose 15-30%.

## Books
FanDuel is the cheapest book on ladders (about -5.5 to -6.5% from -1000 to -110). DK, ESPN Bet and BetRivers are about -7%. BetMGM, Hard Rock, Caesars (williamhill_us) and BetOnline are worst (-8 to -13% on favorites). Every book loses everywhere.

## DK price vs the median implied price of the other books (close, -1000..+150)
"Edge" is how many points DK's implied probability is below the median of the other books (positive = DK is cheaper). BetOnline is excluded from the median.
```
                           rungs  games   hit%  impl%     ROI
  props  -inf..-3          25076  20968   50.2   57.2  -12.6%
  props  -3..-1            83467  76018   51.0   56.4   -9.6%
  props  -1..+1           228191 154649   52.5   56.7   -7.5%
  props  +1..+2            99930  92030   54.9   58.4   -6.0%
  props  +2..+3            60305  54662   57.8   61.5   -6.0%
  props  +3..+5            56762  47312   60.5   63.7   -5.0%
  props  +5..+inf          16118  13204   61.6   64.9   -5.2%
  team   -inf..-3           4355   1521   59.9   63.6   -6.6%
  team   -3..-1            84934  15103   55.7   59.0   -5.5%
  team   -1..+1           169737  34432   56.9   60.4   -6.0%
  team   +1..+2            33185  11691   63.2   65.4   -3.5%
  team   +2..+3             9746   3904   68.9   70.2   -2.3%
  team   +3..+5             2120    835   74.9   73.9   +0.9%
```
- Team legs where DK is 3-5 points cheaper than the other books are roughly break-even (+0.9%, 835 games); 2-3 points cheaper costs -2.3%. This is the cheapest leg type found, and it's rare.
- Props improve when DK is cheaper but never get past about -5%. A prop where DK is pricier than the market (negative edge) costs 10-13%: avoid those.
- Use the `cs` consensus in /api/odds to compute the gap (`cg`) for every leg.

## Morning vs close (DK)
Morning prices are no better or worse than the close: within 0.1 points on every market, and the morning price beats the close only 41-44% of the time. Timing doesn't create an edge. The risk of betting in the morning is injury news, not price.

## Pick'em: market favorites by de-vigged probability
| Fav prob | Games | Won % |
|---|---|---|
| 50-55% | 502 | 50.2 |
| 55-60% | 609 | 57.6 |
| 60-65% | 592 | 61.3 |
| 65-70% | 549 | 66.7 |
| 70-75% | 461 | 75.9 |
| 75-80% | 425 | 76.0 |
| 80-85% | 393 | 83.5 |
| 85-90% | 317 | 88.6 |
| 90%+ | 113 | 96.5 |

The de-vigged market is well calibrated: favorites win at about their no-vig probability. Games in the 50-55% band are true coin flips (50.2%); there, pick the favorite but don't count on it, and use news or rest edges if any.

## Stability
DK prop ladders (-1000..-150) by season: 2023 -6.7%, 2024 -7.8%, 2025 -6.3%. The cost is steady from year to year.
