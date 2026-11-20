# NBA lessons

Claude's running notes on what works and what doesn't in the daily NBA slates. Each run adds a short dated section; Monday runs add a full weekly review. The season table at the top tracks parlays W-L, profit, pick'ems and CLV by week.

## Season table
| Week | Parlays W-L | Profit | Expected | Pick'ems | Avg CLV |
|---|---|---|---|---|---|
| 5 (Nov 16-22, in progress) | 2-0 | +$89.69 | -$1.10 | 4-0 | -1.8 pts (1 of 4 legs positive) |

## Starting points (carried over from the NFL routine, 2026-11-17)
- Hit rate first, but very short legs pay too little: the sweet spot is about -250 to -650.
- Same-game pairs cost 20% of profit in the app; spread legs across games.
- Props carry more vig than team markets. See the NBA numbers below.
- Near coin flips (50-58% favorites): take the market favorite unless there's fresh news.

## NBA backtest lessons (2026-11-18, history/nba_backtest.md, 3,969 games)
- NBA legs cost more than NFL legs. At DK close (-150..-500): moneyline -3.6%, alt totals -4.3%, alt spreads -5.3%, prop alt ladders -7.2% (assists) to -9.0% (threes). Nothing is reliably +EV.
- Two-sided main prop lines cost about half as much as the alt ladders (-3.6 to -4.5%). If a parlay needs a prop, use the main line or the rung nearest it, not a deep ladder rung. Threes alt ladders are the most expensive prop leg.
- Use DK's gap to the consensus (`cg`). Team legs 3-5 points cheaper than the other books are about break-even (+0.9%), and 2-3 points cheaper costs -2.3%. Props where DK is pricier than the market cost 10-13%; never use those.
- Morning prices match the close (within 0.1 pt). The 10 AM slate gives up nothing on price, but it carries injury risk, which the late swap has to cover.
- Pick'ems: the de-vigged market is calibrated. Favorites win at their no-vig probability, and the 50-55% band is a coin flip (50.2%).
- FanDuel ladders are about 1 point cheaper than DK's. That doesn't help us, since the app prices at DK, but it's a sign of where DK is soft.

## 2026-11-19 (Thu, week 5): first NBA slate
**Record:** nothing to grade yet. This is the first NBA slate, so there are no earlier slates, pick'ems, `nba/odds/` snapshots or closing files. `nba/history/legs.csv` gains no rows today; the first graded rows come from this slate's snapshot tomorrow.
**What shaped this slate**
- **The backtest held on today's board.** Every leg was priced against the Pinnacle no-vig line (or the de-vigged `cs` median), and every one cost 1-4 points. Props looked 3-7 points *better* than the book under a plain negative-binomial ladder fit. That is the same fit artifact as the NFL lesson. The backtest's measured ladder costs were blended in, and most of the "edge" disappeared.
- **The profit floor binds before the hit-rate target does.** At -250 to -500, a 2-leg parlay needs each leg's fair probability within about 1 point of DK's implied probability. No 3-leg combination cleared 0.97, so I dropped the 3-leg parlay, as the rules allow.
- **Availability beats the cheap price.** DK priced Golden State's alt spreads 3 points cheaper than the other books, the backtest's cheapest leg type. I passed anyway: the Warriors are -15.6 per game without Curry, and their last three losses were by 21, 22 and 38. The model edge came from availability, which favored Memphis.
- **Questionable starters are a veto.** I took no Portland legs and no Minnesota props: Avdija, Camara and Kuminga are all questionable.
- **Concentration:** both parlays need Memphis to cover (+3.5 and +5.5). That's a known correlation, accepted because no other game had a team leg that cleared the floor. Watch whether this pattern repeats; if it does, publish fewer parlays rather than stacking one game.

## 2026-11-20 (Fri, week 5): grading the first slate
**Record (2026-11-19-nba):** parlays 2-0 (+$29.39 on $50, +$60.30 on $100; total +$89.69 against an expected -$1.10). Legs 4-0: team 3-0 (two MEM alt spreads, one NYK alt team total Under), props 1-0 (Towns 11+ reb, big). Pick'ems 4-0 (0.51 NYK, 0.72 MEM, 0.77 POR, 0.88 SAS), all market favorites.
**Luck or skill:** mostly luck. Expected profit was about -$1, and CLV was negative. MEM +3.5 -1.6, NYK TT u117.5 +0.6, Towns 10.5 -4.5, MEM +5.5 -1.6 (avg -1.8 pts; 1 of 4 positive). Memphis covered by 28 even after Edey was ruled out late. The market had moved against both Memphis legs on that news, and Towns' line slid from 13.5 to 12.5 for no news reason. One night proves nothing; keep tracking CLV.
**Line history:** graded 4,061 rows from the 2026-11-19 snapshot. 93 prop rungs were void because the player sat (Edey, Jerome, Turner, Kuzma, Jaquez); 400+ prop rows were for players DK listed who didn't play. Calibration table (one night, 4 games):

| Bucket | Team n / hit / implied | Props n / hit / implied |
|---|---|---|
| -150..-249 | 132 / 65.2 / 65.8 | 216 / 64.8 / 65.0 |
| -250..-399 | 112 / 81.2 / 75.7 | 139 / 72.7 / 75.6 |
| -400..-649 | 98 / 90.8 / 83.0 | 98 / 87.8 / 83.3 |
| <=-650 | 100 / 92.0 / 90.8 | 211 / 91.0 / 92.4 |

The team -400..-649 bucket technically passes the ">=60 legs, >2 SE" test (2.7 SE). It is NOT applied: every rung in it comes from the same 4 final margins, so the effective sample is 4 games, not 98 legs. Revisit once 60+ distinct games are graded.
**What changed today**
- **Walk-forward test of the team model.** For 142 November games fit on prior data only, model RMSE was 15.4 against 14.5 for the closing line, and every blend weight made the close worse. Team-model weight is now 10% (it was 25%); team fair prices are essentially the sharp market plus the backtest `cg` blend.
- **Backtest blend for every leg:** fair = 50% model-shaded market + 50% (DK implied x (1 + the backtest ROI for that leg's `cg` bucket)). The previous slate did this for props only. It rewards team legs where DK is 3-5 points cheaper than the other books (+0.9% in the backtest) and haircuts the prop-ladder fit artifact.
- **Stable-role veto applied:** Scottie Barnes is off the injury report, but he has missed 5 of Toronto's last 7 games, so no Barnes props despite Barrett being out.
- **Concentration lesson applied:** the only 3-leg parlays that cleared the floor reused the same games as both 2-leg parlays (Brooklyn in all three). The 3-leg is dropped, and the two 2-leg parlays use 4 different games.
- **Team-specific blowout tails, as an adversarial check:** Charlotte had failed the spread by 13+ in 5 of 14 games (league rate 17%), so its +19.5/+20.5 legs were dropped even though DK was 3.5 points cheapest there. Brooklyn's tail (4/14 vs 18%) was accepted at market. Track whether these team-tail vetoes save or cost legs.
- **Morning movement on alt cushions:** in 45 minutes the other books shortened Phoenix, and Utah +16.5's DK edge went from +3.0 to +2.1. A `cg`-driven leg can lose its edge before publish, so always re-pull before finalizing.
