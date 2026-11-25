# NBA lessons

Claude's running notes on what works and what doesn't in the daily NBA slates. Each run adds a short dated section; Monday runs add a full weekly review. The season table at the top tracks parlays W-L, profit, pick'ems and CLV by week.

## Season table
| Week | Parlays W-L | Profit | Expected | Pick'ems | Avg CLV |
|---|---|---|---|---|---|
| 5 (Nov 16-22) | 6-2 | +$96.17 | -$10.00 | 18-8 (exp 17.9) | -1.45 pts (3 of 15 measurable legs positive) |
| 6 (Nov 23-29, in progress) | 2-1 | -$17.14 | -$3.35 | 8-5 (exp 9.2) | +0.4 pts (4 of 6 legs positive) |

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

## 2026-11-21 (Sat, week 5): grading 2026-11-20-nba
**Record:** parlays 2-0 (#1 $50: BKN +17.5 ✓ lost by 2, UTA +15.5 ✓ lost by 10, +$24.35; #2 $50: Eason 4+ reb ✓ (6), SAC +29.5 ✓ lost by 2, +$26.65). Total +$51.00 against an expected -$2.85. Legs 4-0: team 3-0 (all underdog alt-spread cushions with DK 2-3 points cheaper), props 1-0 (Eason, wing). Pick'ems 6-3: misses were DET 0.70 (Toronto won by 3 without Barrett: variance), CHI 0.56 (coin flip, market favorite lost) and HOU 0.53 (the late flip from DEN to HOU after Sengun/Adams were cleared; Denver won by 9). Week pick'em calibration: 13 picks, expected 9.0 wins, actual 10.
**Luck or skill:** luck again. CLV on the four legs: BKN -2.8, UTA -0.5, Eason -5.8 (Sengun and Adams were cleared, so his rebound share fell), SAC -0.3. Week to date: 1 of 8 legs closed in our favor, average -2.1 points. Four wins on eight legs against an expected profit of about -$4 is not evidence of edge. The cushions keep hitting because these are 78-87% legs, not because the price was good.
**Lesson on the late flip:** the HOU flip followed Pinnacle by 1-2 points on a coin flip. That's fine as a rule (follow fresh news and the sharp book), but don't read anything into one loss: a 52% pick loses 48% of the time.
**Line history:** graded 10,062 rows from the 2026-11-20 snapshot (189 prop rungs void for DNPs). Two-night calibration (team n / distinct games / hit / implied; props n / distinct player-games / hit / implied):

| Bucket | Team | Props |
|---|---|---|
| -150..-249 | 439 / 13 / 62.0 / 65.8 | 779 / 150 / 61.6 / 64.9 |
| -250..-399 | 363 / 13 / 76.3 / 75.8 | 483 / 148 / 72.5 / 75.8 |
| -400..-649 | 312 / 13 / 85.9 / 83.1 | 372 / 144 / 82.3 / 83.2 |
| <=-650 | 328 / 13 / 93.9 / 90.9 | 778 / 148 / 90.5 / 92.4 |

Props trail their implied rate in every bucket (by 0.9 to 3.4 points, across about 150 player-games each). That matches the backtest's 5-9% prop cost. Team rungs sit at or above implied, but only 13 games stand behind them. No shading applied yet: the prop gap is within 2 SE per bucket once you count player-games instead of rungs. Picked legs: 8-0 against a summed fair of 6.36.
**What shaped the 11-21 slate**
- **Team-tail veto, applied again:** the Clippers (+15.5, DK 3.1 points cheaper) failed the spread by 16+ in 4 of 14 games, and the Pelicans (+30.5) in 4 of 17 with a 40-point worst. Both were cut even though DK was cheapest there, the same rule as Charlotte on 11-20.
- **B2B rest rule:** New Orleans sat Zion and Murphy on the second night of a back-to-back on Nov 9, so no Pelicans props tonight. Sacramento is on its first back-to-back of the season (no history), and Boston has Tatum (rest) and White questionable, so no props from that game either.
- **Model dispersion check:** the prop model's mean is unbiased against the main lines (median projection minus line: points +0.1, rebounds +0.1, assists +0.1, PRA -0.2). The ladder "edges" come almost entirely from dispersion. That's why the model only gets 30% weight before the 50% backtest blend.
- **Concentration:** 6 games, but only four legs on the board cleared the floor after vetoes (Towns, SAC cushion, MEM cushion, NOP/SAS Under). Two 2-leg parlays on four different games; the 3-leg is dropped again, since any 3-leg would reuse games from both 2-legs.

## 2026-11-22 (Sun, week 5): grading 2026-11-21-nba
**Record:** parlays 2-0. #1 ($50): Josh Hart 7+ reb (late swap for Towns) ✓ (8), Memphis +17.5 ✓ (lost by 9): +$38.52. #2 ($50): Sacramento +28.5 ✓ (won outright 97-96), Pelicans-Spurs Under 247.5 ✓ (205): +$16.91. Day +$55.43 against an expected -$3.18. Legs 4-0: team 3-0 (two alt-spread cushions, one alt total Under), props 1-0 (Hart, guard). Pick'ems 4-2: misses were POR 0.51 (the late flip after Towns and Anunoby were ruled out; the Knicks won by 1) and BOS 0.85 (Sacramento won by 1 with Tatum and White out; variance, the market had BOS at 85%). Week to date: 19 pick'ems, expected 13.4 wins, actual 14.
**Week to date (Mon-Sun board, 3 slates):** parlays 6-0, +$196.12 vs an expected -$7.13. Legs 12-0 against a summed fair of 8.86: team 9-0, props 3-0 (big, wing, guard). This is a lucky run, not proof of edge: expected profit is still slightly negative and CLV is still negative.
**CLV:** MEM +17.5 0.0, NOP/SAS Under 247.5 -1.8, SAC +28.5 +0.4; Hart was swapped in near tip, so its CLV is 0 by construction and isn't counted. Week: 2 of 11 measurable legs closed in our favor, average -1.6 points. Alt-total Unders and the underdog cushions keep closing slightly against us. DK being cheaper than the other books (`cg`) has been a better guide than the morning number itself.
**Line history:** graded 5,836 rows from the 11-21 snapshot (488 prop rungs void for DNPs: Towns, Anunoby, Murphy, Washington and others). Three-night calibration over 19 games (team n / games / hit / implied; props n / player-games / hit / implied):

| Bucket | Team | Props |
|---|---|---|
| -150..-249 | 646 / 19 / 60.2 / 65.8 | 1098 / 211 / 60.4 / 64.9 |
| -250..-399 | 536 / 19 / 71.8 / 75.9 | 677 / 205 / 72.5 / 75.7 |
| -400..-649 | 453 / 19 / 80.1 / 83.1 | 521 / 201 / 82.3 / 83.2 |
| <=-650 | 479 / 19 / 90.0 / 91.0 | 1078 / 207 / 90.9 / 92.3 |

Both groups now trail implied in every bucket (team by 1-5.6 points, props by 0.9-4.5). By family, the spread rungs (mostly underdog cushions) hit 88.5% against 81.8% implied, while totals rungs (67.4 vs 78.0) and team totals (66.5 vs 73.4) trail. That's only 19 games of final scores, so no shading is applied (the effective sample is 19, far short of the 60 required). Picked legs: 12-0 against a summed fair of 8.86.
**What shaped the 11-22 slate**
- **Team-tail veto, again:** Golden State's alt spreads were the cheapest legs on the board (DK 3-5 points under the other books, at about break-even by the backtest). Since Curry went out, though, the Warriors have lost four straight by 21, 22, 28 and 38, failing the spread by 16+ every time. Same rule as CHA, LAC and NOP: the cheap price doesn't pay for a live blowout tail.
- **Stars-questionable veto:** OKC@MIA (SGA and Giannis both questionable) gets no legs. The OKC +14.5 cushion was 3.3 points cheap at DK, but its value depends on SGA playing.
- **Back-to-backs:** DAL, NYK and BOS are all on the second night. Dallas and New York had not filed injury reports by morning, and NYK has Towns, Anunoby and Clarkson questionable, so there are no props from DAL@UTA or IND@NYK and no NYK/IND/DAL sides.
- **Team-first rule binds hard:** with only four legs in two parlays, 60% team legs means at most one prop, which forces most of the slate onto team cushions.
- **Morning `cg` edges decay:** between 15:06 and 15:49 UTC, DK shortened its Washington cushions faster than the other books (`cg` +3.1 → +2.4 on +19.5), which killed the planned WAS +19.5 / Okongwu parlay. This is the second time (Utah on 11-20). Build from the second pull, never the first.
- **Concentration, forced:** the only two parlays that cleared the floor both need the BOS@GSW Over (192.5 and 194.5). It's accepted only because the slate minimum is two parlays. Both are staked at $50. Track whether shared-leg slates hurt; if they do, propose to the owner that one parlay be allowed when only one clears.

## 2026-11-23 (Mon, week 6): week 5 review and grading 2026-11-22-nba
**11-22 record:** parlays 0-2 (-$100 against an expected -$2.90). #1 WAS +14.5 ✓ (won by 20) + BOS@GSW Over 192.5 ✗ (88-87, total 175). #2 Okongwu 12+ ✗ (6 pts in 29 min, 3-9 FG, 1-4 3PT) + Over 194.5 ✗. Pick'ems 4-3: missed DET 0.55 (coin flip), ORL 0.64 (Washington won by 20) and BOS 0.73 (Golden State won by 1).
**Why the misses:** the BOS@GSW total closed 211.5 at ESPN and finished 36 under, with both teams shooting poorly; Boston scored 12 in the fourth. The Over was priced fairly (CLV -0.1 and +0.3), so that is mostly variance, but it was **one game sinking both parlays**: the shared leg turned a 1-of-2 day into 0-2. Okongwu was a cold shooting night with Flemings active (the publish note's upside case didn't happen), and the market moved 3.4 points against him before tip.

### Week 5 review (Nov 16-22; full report in nba/reports/2026-11-23-week.md)
- **Parlays 6-2, +$96.17 vs an expected -$10.00.** The owner's weekly board total isn't visible from the repo, so the head-to-head result is unknown here.
- **Legs 13-3 (summed fair 12.04).** Team legs 10-2 (83.3%) against 83.0% average implied and 81.7% fair: exactly at price. Props 3-1 (75%) against 73.1% implied. Position groups: guard 1-0 (Hart), wing 1-0 (Eason), big 1-1 (Towns ✓, Okongwu ✗).
- **Stake tiers:** $50 parlays 5-2 (+$35.87); $100 1-0 (+$60.30). No $150/$200.
- **Rest:** 11 of 16 legs involved at least one team on a back-to-back; both losing team legs were in a game with a B2B team (Boston).
- **Pick'ems 18-8 against 17.9 expected.** By confidence: 0.50-0.58 2-4 (exp 3.2), 0.58-0.65 2-1 (1.9), 0.65-0.75 6-2 (5.5), 0.75+ 8-1 (7.4). Calibrated; coin flips are coin flips.
- **CLV by market group:** alt-spread cushions -0.9 pts (8 legs, 1 positive), totals and team totals -0.2 (4 legs, 2 positive), props **-4.6** (3 legs, 0 positive). Overall -1.45, 3 of 15 positive.
- **Leg-cost check (backtest `cg` buckets):** team cg 3-5 went 4-2 (both losses the BOS Overs), cg 2-3 4-1, cg <2 5-0. Far too few legs to judge against the +0.9%/-2.3% bucket costs; keep tallying.
- **Underdog/fade scorecard:** no pick'em or moneyline leg differed from Pinnacle by more than 3 points, so nothing to score yet.
- **Line history (26 games, 4 snapshots):** team rungs trail implied in every bucket (-150..-249 61.9 vs 65.8; -250..-399 73.4 vs 75.9; -400..-649 80.7 vs 83.1; <=-650 89.8 vs 90.9), props too (59.7/65.0, 72.2/75.7, 81.1/83.1, 90.2/92.4, about 280 player-games per bucket). By family, alt-spread rungs hit 87.8% vs 81.9% implied while totals (69.7 vs 78.0) and team totals (68.1 vs 73.4) trail; rebounds (76.9 vs 77.0) and assists (74.0 vs 74.0) ladders hit at price while points (74.7 vs 79.6), threes (69.2 vs 75.7) and the points combos trail by 3.5-6.5. The largest prop bucket gap is 1.9 SE over player-games, short of the 2-SE rule, and team buckets rest on only 26 games, so **no shading yet**.

**What changes from week 6**
1. **No game in two parlays.** 11-22 showed the cost: one 175-point game took both parlays. Sharing a game is now a last resort, used only to reach the slate minimum, at $50, and flagged in the note. The weekly report asks the owner (via nba/notes.md) whether a single parlay should be allowed on those days.
2. **Props: smaller role, cheaper families.** Props closed 4.6 points against us on average (0 of 3 positive), and points/threes/combo ladders trail implied in the line history while rebounds/assists hit at price. Use at most the one prop the variety rule asks for, prefer rebounds/assists or a rung well below a stable starter's median, require `cg` >= +2 and prefer +3 or more.
3. **Alt totals get a higher bar** (totals rungs 69.7% vs 78.0% implied over 26 games): use one only when it is clearly the best leg left, and never two in one game.
4. Stakes stay at $50 until something clears EV >= -1%: expected profit has been negative every day, and the 13-3 legs were close to price.

## 2026-11-24 (Tue, week 6): grading 2026-11-23-nba
**Record:** parlays 1-1 (-$35.18 against an expected -$2.50). #1 ($50) ✗: Sacramento +26.5 ✓ (lost by 16), Brook Lopez 8+ pts ✗ (3 pts on 1-3 FG in 21 minutes). #2 ($50) ✓: Chicago +23.5 ✓ (won outright by 14), Indiana +20.5 ✓ (won by 5): +$14.82. Legs 3-1: team 3-0 (three underdog alt-spread cushions), props 0-1 (Lopez, big). Pick'ems 6-4 against 7.17 expected.
**Why the misses:**
- **Lopez:** not a blowout (Houston won by 12), not foul trouble (0 fouls), not a minutes cut (21 minutes, at the low end of his 19-29 range). He took only 3 shots. That's a usage and variance loss; his 7-, 7- and 2-point games were already in the log, and the 0.77 fair priced them. CLV was +0.3, so the price was fine. Season props are now 3-2, and both prop losses were bigs' points rungs (Okongwu, Lopez).
- **Pick'ems:** PHI 0.56 (Embiid ruled out at 22:49 UTC; Pinnacle closed 51.6%, a coin flip), OKC 0.62 (five OKC rotation players ruled out around 19:00 UTC, but the line held at 63% with SGA available; Indiana won by 5), TOR 0.77 and CLE 0.73 (Milwaukee by 5, Chicago by 14 on a back-to-back). None was foreseeable at 10 AM. All ten were market favorites.
**CLV:** SAC +26.5 +2.9, Lopez +0.3, CHI +23.5 -1.3, IND +20.5 +0.2. Average +0.5, 3 of 4 positive: the first slate with positive average CLV. Season: 6 of 19 measurable legs positive, average -1.1.
**Underdog/fade scorecard:** still empty (no pick'em differed from Pinnacle by more than 3 points).
**Line history:** +10,391 graded rows from the 11-23 snapshot (448 prop rungs void for DNPs). 37 games now graded. Calibration (team n / games / hit / implied; props n / player-games / hit / implied):

| Bucket | Team | Props |
|---|---|---|
| -150..-249 | 1210 / 36 / 62.3 / 65.8 | 2080 / 404 / 60.2 / 65.1 |
| -250..-399 | 1016 / 36 / 74.1 / 75.9 | 1260 / 391 / 73.1 / 75.7 |
| -400..-649 | 861 / 36 / 81.0 / 83.1 | 1012 / 372 / 80.6 / 83.2 |
| <=-650 | 907 / 36 / 89.4 / 90.9 | 2034 / 394 / 90.5 / 92.4 |

- **First shading applied:** props at -150 to -249 hit 60.2% against 65.1% implied over 404 player-games, 2.06 SE below. From today, every prop leg in that bucket gets fair = 50% model fair + 50% (DK implied x 60.2/65.1), still capped at 6 points from the market. In practice this takes nearly every prop at that price out of the >= 0.65 pool. No other bucket passes 2 SE (team buckets rest on 36 games).
- **By side:** the totals gap is all Overs. Over rungs at -400..-700 hit 71.2% vs 83.9% implied, while Under rungs hit 84.5% vs 84.0%. Underdog alt-spread cushions hit 91.3% vs about 85%, and favorites' alt spreads trail (74.1 vs 83.2, 12 games). Only 36 games stand behind this, so it's a lean, not a rule: prefer Unders and dog cushions to Overs and favorite alt spreads.
- **Picked legs:** 16-4 against a summed fair of 15.41 (20 legs; the overconfidence test needs 60).
**What shaped the 11-24 slate:** only three games, so the "no game in two parlays" rule allows one 2-leg parlay (the section 1 minimum for 2-3 games is 1). With one 2-leg parlay, the 60% team-leg rule means both legs are team legs, so there is no prop today even though 4b asks for one; leg cost wins (section 4b).
- **Slate:** one $50 parlay, Pistons-Magic Under 230.5 (-550) + Washington +26.5 (-660): P 0.722, EV -1.7%, both legs in the team `cg` 3-5 bucket. DK cut the WAS rung from -680 to -660 at the final check while the other books held, the first time this week a DK `cg` edge grew before publish instead of shrinking.

## 2026-11-25 (Wed, week 6): grading 2026-11-24-nba
**Record:** parlay 1-0 ($50): Pistons-Magic Under 230.5 ✓ (final 104-86, total 190) and Washington +26.5 ✓ (lost by 15): **+$18.04** against an expected -$0.85. Legs 2-0, both team legs in the backtest's `cg` 3-5 bucket. Pick'ems 2-1: DET 0.56 ✓, BOS 0.78 ✓, DEN 0.71 ✗ (Dallas won by 19 in Denver after P.J. Washington was upgraded to available; Pinnacle closed DEN at 71%, so this was variance, not missed news).
**Week 6 to date (3 slates):** parlays 2-1, -$17.14 against an expected -$3.35. Legs 5-1 (team 5-0, props 0-1). Pick'ems 8-5 against 9.2 expected.
**CLV:** Under 230.5 +0.9, WAS +26.5 -0.5. Week 6: 4 of 6 legs positive, average +0.4 points. Season: 8 of 21 measurable legs positive, average -1.0 (it was -1.1).
**Underdog/fade scorecard:** still empty. No pick'em has differed from Pinnacle by more than 3 points.
**Leg-cost tally:** team legs with `cg` 3-5 are now 6-2 this season (both losses were the 11-22 BOS@GSW Overs); `cg` 2-3 4-1; `cg` <2 5-0.
**Line history:** +3,262 graded rows from the 11-24 snapshot (215 prop rungs void for DNPs). 40 games are now graded. Calibration (team n / games / hit / implied; props n / player-games / hit / implied):

| Bucket | Team | Props |
|---|---|---|
| -150..-249 | 1310 / 39 / 61.6 / 65.8 | 2269 / 439 / 60.5 / 65.1 |
| -250..-399 | 1099 / 39 / 73.1 / 75.8 | 1374 / 424 / 73.4 / 75.7 |
| -400..-649 | 937 / 39 / 79.7 / 83.1 | 1096 / 403 / 80.2 / 83.2 |
| <=-650 | 984 / 39 / 88.1 / 90.9 | 2223 / 429 / 90.1 / 92.4 |

- **Prop shading kept:** props at -150..-249 are still 2.04 SE below implied over 439 player-games, so the 50/50 blend with DK implied x 60.5/65.1 stays in place (the ratio was 60.2/65.1). No other bucket passes 2 SE. Team buckets rest on only 39 games.
- **By family, -150..-700:** spread rungs hit 80.1% vs 75.2% implied, and Under rungs hit at price (74.1 vs 75.1). Over rungs (61.5 vs 74.8) and team totals (67.8 vs 73.4) still trail. Among props, rebounds+assists (73.0 vs 74.4) and assists (68.6 vs 69.6) are nearest to price; threes (65.1 vs 71.0), steals and blocks are worst. This is still a lean (dog cushions and Unders over Overs), not a rule.
- **Picked legs:** 18-4 against a summed fair of 17.11 (22 legs; the overconfidence test needs 60).
**What shaped the 11-25 slate**
- **Nine games, still only two parlays.** Only three games had team legs with DK 3+ points cheaper than the other books (SAC, LAC and POR cushions). Every other game's best leg cost 2.5-4%, so a 3-leg parlay could clear the floor only by reusing a game, which the week-6 rule forbids.
- **Questionable-star vetoes:** no team legs in CLE@NYK (Towns, Hart, McBride questionable), MIA@PHI (Giannis questionable, Embiid doubtful) or SAS@POR. Portland's +12.5 cushion was DK-cheap, but San Antonio is only -2.5 after being -8.5 to -19.5 in recent games, which means the line assumes Wembanyama and/or Fox might sit. If they play, the cushion is much worse.
- **LAC tail veto lifted, and tracked:** the Clippers failed the spread by 16+ in 4 of 16 games. That's within 1 SE of the league's ~17%, and the LAC +15.5 cushion vetoed on 11-21 covered anyway. With DK 3.6 points under every other book, the cushion is in. If it loses to a blowout, reinstate the veto.
- **One short prop leg instead of a points rung:** Holiday's P+R 10+ (11+ in each of his last 12) beat his points rungs on hit rate. Points ladders trail implied in our line history.
- **Slate:** two $50 parlays: Kings +20.5 / Holiday P+R 10+ (P 0.746, EV -2.2%) and Clippers +21.5 / Suns +23.5 (P 0.731, EV -2.8%).
