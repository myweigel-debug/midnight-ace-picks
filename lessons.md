# Lessons learned

## Week 9 notes (seeded by the owner)
- Week 9 went winless. The parlays were EV-maximizing long shots (avg ~16% hit chance) built on model edges over the market that didn't hold up.
- Several Sunday games were played in heavy rain and the unders hit. The forecasts were available and the picks didn't account for them: weather deserved far more weight, on totals and on every passing, receiving and kicking leg.

## 2026-11-03 review: ESPN Week 8 slates (2026-10-27-tue / -wed / -sat, graded from ESPN box scores)
These are the slates the owner's notes call "Week 9". ESPN numbers the Oct 29 - Nov 2 games Week 8.

**Record**
- Parlays went 1-12. The only win was wed-2 (Ollie Gordon U10.5 rec yds + Tee Higgins O79.5 rec yds). The 13 parlays had an average claimed hit chance of 16%.
- Legs went 19-20:

| Group | W-L |
|---|---|
| Receiving | 9-3 |
| Rushing | 4-1 |
| Kicker | 2-0 |
| Defense | 1-3 |
| QB | 1-4 |
| Team | 2-9 |

- Pick'ems went 9-4 (69%) against an average stated confidence of 65%, so roughly calibrated. There were no underdog picks.
- The four misses: DAL at 72% (lost 30-33 in OT to ARI after Minshew came on), NYJ at 55%, KC at 52% (a coin flip) and SEA at 60% (lost 17-34 to CHI).

**Closing-line value:** only 2 legs carried a closing price, and both moved our way (JSN +126 to +112, Darnold INT -107 to -119). That sample is too small to read anything from.

**Why legs lost**
- **Team unders and alt underdog spreads went 2-9.** These were model leans against the market:
  - MIN +1.5 and MIN +3, where the model had Minnesota better than the market did.
  - The DEN, BUF, DAL and NE team-total unders.
  - MIA +2.5.

  Most of them lost by a wide margin: BUF scored 36, DEN 28, DAL 30. These losses were foreseeable, because the market was right and the model was not.
- **QB pass-TD unders went 0-3**, each losing to exactly 2 TDs. That is a high-variance market.
- **Defense:** the sack and tackle overs at plus money went 1-3, and Bishop finished with 2 tackles against a 7.5 line. These were long shots.
- **Big-rung or small-role receiving overs** that lost:
  - Keon Coleman went for 4 yards.
  - Jaylen Warren had 0 receiving yards.
  - Elijah Higgins' longest catch was 6 yards.
- **Low alt rungs mostly hit**, with two exceptions:
  - Malik Washington 25+ and Justice Hill 5+ hit.
  - Maye 15+ rush yards lost (5 yards, in a rain game).
  - PHI team total over 13.5 lost (10 points, with McKee at QB).

**What I'm doing differently (from 2026-11-03-tue)**
1. Build parlays for hit rate. Every leg is 0.78-0.85 fair, built from low alt rungs of high-volume starters and favorites' moneylines. 2-leg parlays target 0.65 or better.
2. Use no team unders or underdog spreads that rest on the model disagreeing with the market. The market gets about 80% of the weight, and the shade is capped at 6 points.
3. Avoid TD props, sacks, longest-reception markets and plus-money tackle legs.
4. In rain or wind, avoid passing, rushing-QB and receiving overs, and lean on that game's unders only when the forecast is firm.
5. For QB changes (McKee, Fagnano), fade the affected offense only through legs the market already agrees with.

## 2026-11-05 review (Thursday run, ESPN Week 9)
**Record:** nothing new to grade. Every Week 8 game was already graded on 2026-11-03: parlays 1-12, legs 19-20, pick'ems 9-4. The 2026-11-03-tue slate's games are all Week 9 (Thu Nov 5 – Mon Nov 9), and none has kicked off yet. No `cl` stamps exist yet, so there is no new CLV data.

**What I'm applying this run**
- **Hit rate first.** Legs are low rungs on starters who cleared the rung in every or nearly every game this season:
  - Irving 45+ rush yds in 8/8
  - Kyren Williams 41+ in 8/8
  - Odunze 39+ rec yds in 8/8
  - Maye 178+ pass yds in 8/8
  - Stevens 4+ kicking pts in 7/7
  - Starks 4+ tackles in 7/8
  - JAX ML against an undrafted rookie QB
- **Pinnacle (`px`) is the baseline now.** `px` came back on every Week 9 response (it was missing on Tuesday). Main lines are de-vigged from Pinnacle, and alt ladders are fit to Pinnacle and DK main lines plus the DK rungs.
- **The model shade is capped at +2.5 points for published `fair`.** The raw log-based shade ran +3-4 points on most low rungs, and last week's sensitivity check said true rates sit a few points under the headline.
- **Weather:** TNF in Baltimore has 75% showers and thunderstorms, so there are no passing, receiving or kicking overs in that game. The only TNF legs are the JAX ML and a BAL safety's tackles, which rain does not hurt (more runs mean more tackles).
- **Injury filter:** every player who is DNP, LP-with-hamstring, in a QB change (PHI Milton, SEA Lock, MIN Murray 50/50, CLE Sanders) or in an unsettled committee is excluded before pricing.

## 2026-11-08 review (Sunday run, ESPN Week 9)
**Record (graded from ESPN, JAX 33 @ BAL 10 final):**
- **Parlays:** 2026-11-03-thu-1 **won**: JAX ML hit, and Malaki Starks 4+ tackles+assists hit with exactly 4.
- **2026-11-03-tue-1:** the JAX ML leg hit. Bryce Young's leg is still pending, so the parlay is not graded yet.
- **Not graded yet:** every other Tue/Thu leg (Sunday and Monday games).
- **Season since the hit-rate switch:** parlays 1-0, legs 3-0 (team 2-0, DEF 1-0).
- **Pick'ems:** 1-0 (JAX at 0.82). The season total is now 10-4.

**Closing-line value:** 1 of 3 graded prices moved toward us.
- Starks went from -505 to -519 (toward us).
- JAX ML went from -500 and -470 to -455 (away from us). The closing move against us came from rain and a small amount of sharp BAL money. JAX still won by 23.

**Lessons:**
- **The approach held up.** The rain-aware TNF build (tackles and the favorite's ML, no passing) did exactly what was intended. Keep it: in rain, use tackles and favorites. In dry weeks, low rungs on volume starters.
- **Concentration risk:** one JAX ML leg sat in two slates. If JAX had lost, both parlays would have died together. From now on I spread legs across games and avoid reusing earlier slates' legs in the same week where an equal-quality alternative exists.
- **Fit artifacts:** a player's ladder fit can produce fake edges. My pooled-dispersion fit first showed rush-yard rungs 4 points *better* than the book, which was a fit artifact. The fix: fit mean and dispersion jointly to the Pinnacle main, the DK main and the DK ladder. After that, every market showed the expected ~2-3 points of book hold. Always run this calibration check before trusting a "fair" number.

## 2026-11-10 review (Tuesday run, ESPN Week 10 slate; Week 9 fully graded)
**Week 9 record (2026-11-03 tue/thu/sun), graded from ESPN box scores**
- **Parlays: 11-1, +$367 on $1,200.** The slates' own fair probabilities expected about -$38, so roughly +$400 of that was luck.
  - Tue: 3-0, +$169 (expected -$4).
  - Thu: 3-0, +$137 (expected -$6).
  - Sun: 5-1, +$62 (expected -$28).
- **Legs: 28-1.** QB 8-0, RB 5-0, WR/TE 4-0, team 4-0, K 3-0, DEF 3-1.
  - The only miss was Kamari Lassiter (CB) 2+ solo tackles at -900; he had 1. That was a fragile market at a price too short to be worth it.
- **Stake tiers:** every parlay was $100 (no tiers yet).
- **Pick'ems: 14-1** at an average stated confidence of about 0.68, against roughly 10.2 expected, so this streak is mostly luck.
  - The miss was NE at 0.61 (GB won 45-27; Love threw for 372). It was a coin-flip-range pick with no foreseeable cause.
  - Season pick'ems: 23-5.
- **CLV:** 24 legs carry a DK closing price (`cl`). 13 of 24 (54%) closed shorter than we bet them, an average of +0.4 implied-probability points (with vig; no publish-time snapshots or Pinnacle closes exist yet).
  - K: 3 of 3, +1.3 pts.
  - WR/TE: 3 of 4, +0.7.
  - QB: 3 of 5, +0.4.
  - RB: 1 of 4, +0.4.
  - DEF: 2 of 4, +0.1.
  - Team: 1 of 4, -0.3.
- **Line history:** `history/legs.csv` was created and seeded with all 66 graded picked legs. No unpicked legs exist yet, because this is the first `odds/` snapshot.
  - Calibration so far:
    - -650 and shorter: 14 of 15 hit (0.93) vs 0.89 implied.
    - -400 to -649: 13 of 13 hit vs 0.83 implied.
    - Longer than -150: 0.47 vs 0.46 implied.
  - No bucket has 60 legs yet, so I made no shading changes.

**Lessons applied this run**
1. **Alt-line model bug caught.** My first kernel-on-spread model priced big buy-downs badly:
   - It had GB +6.5 at 0.88 and Bills alt lines way off. Its fitted "effective spread" for BUF was -14.5 against a market of -7.5.
   - Alt-total unders came out about 5 points too high (TNF Under 50.5 at 0.80 vs a truer 0.76).
   - The fix: fit pooled 2015+ residual distributions to Pinnacle's full alt-spread and alt-total ladders, and correct toward Pinnacle at every posted point.
   - Rule: always compare model output to the Pinnacle ladder points before trusting an alt-line fair.
2. **DK's alt-total unders are priced about 3-6% worse than fair** across games (pooled residual sd about 13.5 on totals). Avoid them unless weather clearly moves the number.
3. **DK favorites' moneylines this week were 3-5 points worse than Pinnacle** (JAX -600 vs 0.81 no-vig, LAR -455 vs 0.785, BUF -485 vs 0.78), so no ML legs this week. Check this gap every week.
4. **Week 9 ran hot.** The -740 to -900 Sunday legs averaged -3% to -7% EV per parlay and still won only on variance. This slate keeps legs at -310 to -620 and every parlay at EV of +1% or better.
5. **Stake tiers start this week:** $150 / $100 / $50. Track whether the $150 tier hits at least its stated P(hit).
6. **Re-poll before pushing.** Between 18:05 and 20:14 UTC, MIN@GB moved from GB -5.5 to -3.5 at both DK and Pinnacle on Vikings QB news, which made my GB +6.5 leg stale, so I replaced it. Always re-pull the lines for every chosen leg near push time and drop any leg the sharp market has moved against.
