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

## 2026-11-12 review (Thursday run, ESPN Week 10)
**Record:** nothing new to grade.
- Week 9 was fully graded on Tuesday: parlays 11-1, +$367; legs 28-1; pick'ems 14-1 (season 23-5).
- The 2026-11-10-tue slate's games start tonight at the earliest, so they aren't graded.
- `history/legs.csv` gained no rows: the only `odds/` snapshot (2026-11-10-tue) has no final games yet.

**Interim line movement on the Tuesday slate (DK at publish → DK Thursday, not CLV):** 3 legs moved toward us, 3 away, 1 flat.
- Toward us: Warren 39.5 (-415 → -505), Maye 199.5 (-503 → -553), Saints +9.5 (-530 → -560).
- Away from us: HOU +2.5 (-310 → -277; Deshaun Watson replaces Shedeur Sanders and both HOU RBs are hurt), J. Williams 24.5 (-620 → -581; Goff questionable), Higgins 39.5 (-660 → -650).
- Flat: SF +2.5.

**Lessons applied / learned this run**
1. **A second alt-spread bug, caught before publishing.**
   - My rebuilt spread model smoothed historical residuals with a Gaussian kernel. That smeared the key-number mass at 3, so DK's +1.5/+2.5 dog-side rungs on 3.5-4.5 favorites looked +3-4% EV (HOU +2.5, CIN +2.5, BAL +2.5).
   - The empirical P(favorite loses by exactly 3 | spread 3.5-5.5) is about 7.7%, and the kernel gave about 2%.
   - Rule: price alt spreads from the *unshifted* distribution of games with similar closing spreads (±1 pt). Never shift or smooth margins across key numbers.
   - After the fix, no alt spread near a key number showed an edge.
2. **Low receiving rungs need a dud-game allowance.**
   - Leave-one-out checks on 2026 logs: WR/TE games clear 15% of the player's average only 90% of the time and 25% only 87%. A gamma fit to the main line says 96% and 91%.
   - The props model now carries a small zero-inflation term (fit at about 3% for receiving yards). That removed the fake +5% EV on 9.5-yard rungs.
   - The legs I used (Lamb 49.5, Olave 39.5, Kelce 19.5) sit at 40-55% of the market mean, where the fit and the empirical rates agree.
3. **Consensus check.** For every chosen prop, DK's price was at or better than the raw median of the other books at the same rung. That is now a standing filter.
4. **Rain on TNF again.** No passing or receiving legs in WAS@NYG. The only TNF leg is the dog's big alt spread (WAS +11.5), which rain helps.

## 2026-11-15 review (Sunday run, ESPN Week 10)
**Record:** only TNF is final (WAS 24 @ NYG 21).
- **Legs:** WAS +11.5 (2026-11-10-thu-2) **hit**: Washington won outright. 1-0 (team). That parlay is still pending on Geno Smith 170+.
- **Parlays:** none fully graded yet. No new profit numbers; Week 9 stays at +$367 (expected -$38).
- **Pick'ems:** NYG at 0.56 **lost**, a coin-flip pick that leaned on the power model against a near-pick'em line. Season: 23-6. I haven't yet tracked calibration by confidence band; it starts next review.
- **CLV:** WAS +11.5 went from -470 to -494 at DK, but `clp` 0.809 is below the publish no-vig of 0.853, so it was -4.4 pts by our measure. As Thursday's swap report noted, most of that gap is a method mismatch (one-sided interpolation at publish vs a two-sided median at close).
  - Running CLV for graded legs with `clp`: 1 leg, 0% positive, -4.4 pts. Too small to read.
- **Moneyline-parlay scorecard:** no Sunday ML bonus has been graded yet.

**Line history (history/legs.csv):**
- Added 2,192 graded rows from the 2026-11-10 tue/thu snapshots for WAS@NYG (202 TD/longest or ungradable rows skipped).
- Unpicked legs in that one game:
  - -400 to -649: 99% hit vs 84% implied (n=96).
  - -650 and shorter: 97% vs 93% (n=217).
  - QB pass-yds and attempts Overs ran well above implied.
- **No shading change.** All of these rows come from a single rain game, so they are one correlated draw, not 60 independent legs. I need several games before the 2-SE rule can mean anything.

**Lessons applied / learned this run**
1. **The pooled "ratio" props model is too wide, and not only for QBs.** It scales a player's stat by his rolling 6-game mean.
   - Pass yds came out 10 pts under the market at low rungs, rec yds 4 pts, rush yds 3.5 pts. A noisy prior mean inflates the spread.
   - I now use only its *relative* signal: model minus market, minus that family's median bias, ×0.3, capped at -3/+1.5 pts.
   - The market baseline is the median of per-book power de-vigs at the exact rung, minus 0.5 pt for alt-ladder hold that the main-line exponent misses.
2. **DK low-rung alt prices often beat the other books' median by 3-5 pts** (Kelce 24.5, Henry 19.5, Flournoy 19.5). That is where the positive-EV legs came from this week, not from model shading.
3. **DK moneylines are 1.5-5 pts worse than Pinnacle for the third straight week** (JAX -700 vs 83.7% no-vig). So: no core ML legs, and the ML bonus can barely clear -10% EV. Out-of-sample situational check (2010-17 vs 2018-25):
   - Big favorites (>75%) beat the line by about 1 pt in both halves.
   - Divisional, rest, bye, road-favorite, cold and wind effects did not replicate.
4. **The 6th core parlay was forced at -2.8% EV and given $50.** If next week's pool is this thin again, publish 5 core parlays instead.
5. **Role filter:** I skipped Kaelon Black 15+ (+2.4% EV) because he is the backup behind CMC with a growing but unsettled role. I skipped Aaron Jones because his carries collapsed to 5 a game.

## 2026-11-17 review (Tuesday run, ESPN Week 11 slate; Week 10 fully graded)
**Week 10 record (2026-11-10 tue/thu/sun), graded from ESPN box scores (nflverse cross-check)**
- **Parlays: 11-6, +$215 on $1,450 staked** (core +$88, bonus +$128). The slates' own fair probabilities expected about +$21 (core +$27, bonus -$7), so roughly +$195 was luck, all of it on Sunday.
  - Tue: 1-2, -$113 (expected +$8). Thu: 1-2, -$89 (expected +$13). **Tue+Thu: 2-4, -$201.**
  - Sun core: 5-0, +$289 (expected +$6). Sun bonus: 2-1, +$128 (expected -$7): sun-6 lost only on Tyler Warren 20+ (1 yd); sun-7 (P 0.46) and the ML bonus sun-8 (P 0.26, +$123) both won.
- **Legs (unique):** Tue/Thu team 3-1 (avg implied 0.79), props 6-4 (avg implied 0.84). Sunday team 10-0 (0.80), props 10-1 (0.83). Counting repeats the owner's tally is Tue/Thu 9-5, Sunday 25-1.
- **Why the losses happened:**
  - Maye 48 pass yds: hurt early in Munich (feared fractured ankle). Not foreseeable; this is the injury risk a 6-day-old prop carries.
  - Warren 15 rush yds: his snap share had been sliding (97% → 58%) and was flagged at publish. Foreseeable; the role-change rule now excludes this kind of back.
  - HOU +2.5: lost by exactly 3 (24-27) to Deshaun Watson's 312 yds. Key-number loss; Watson replaced Sanders after we bet. Partly news risk.
  - Geno Smith 148 (169.5 needed) and Olave 30 (39.5): quiet games; Olave's was variance, Geno's was a low-volume 21-attempt game.
  - Tyler Warren 1 yd (bonus): variance at -800, a fragile low-volume TE rung.
- **Stake tiers (core):** $150: 2-1, +$2 (stated P ~0.69). $100: 4-1, +$149. $50: 1-2, -$64. Too few to change the tiers.
- **Pick'ems: 9-5** (14 games; NYG was already graded) vs 9.3 expected → calibrated. Season **32-10**.
  - By band: ≥0.80: 3-0. 0.60-0.79: 5-2 (exp ~4.6). Near coin flips 0.50-0.58: 1-3 (exp ~2.2; NYG, GB, NO lost — all were the market favorite or the power lean). Running coin-flip tally: Week 10 1-3.
  - Underdog picks: none.
- **Moneyline-parlay scorecard:** sun-8 won (5-0). No pick differed from Pinnacle by more than 3 pts, so nothing to add to the fade/underdog tally yet (0 entries).
- **CLV (28 graded legs with `clp`):** 0 of 28 positive by the `clp` − publish no-vig measure, average -3.3 pts (team -2.1, props -4.2). But DK's own price moved toward us on 18 of 28 (avg +0.3 implied pts). Same method mismatch as before: publish `mkt` came from one-sided ladder fits/interpolation, which runs higher than the two-sided closing median. **Fix this run:** publish `mkt` now blends the ladder fit with a per-book power de-vig at the exact rung (the same family of method the close uses), so next week's CLV should be comparable.
- **Early-week vs Sunday tally (running):** Week 10 Tue/Thu props 6-4 at 0.84 implied (−24 pts), Sunday props 10-1 at 0.83. Only one week; keep counting.

**Line history (history/legs.csv): +33,738 graded rows** (every rung in the three Week 10 snapshots; 433 TD-scorer/longest/void rows skipped; ESPN box scores primary, nflverse fallback for players with no box-score line, snap counts used to grade 0s).
- Deduped across snapshots (20,143 legs) with player-game cluster-robust errors, **short-priced player-prop Overs hit well below DK's implied probability:** -150..-249 56% vs 65%, -250..-399 66% vs 76%, -400..-649 77% vs 83%, -650+ 85% vs 92% (cluster z -2.4 to -3.1). Against the no-vig market the gap is about 3-5 pts.
- Team spreads/totals were much closer to implied (-0.3 to -6 pts, no bucket beyond 2 SE once clustered); alt totals actually ran slightly above.
- Picked legs: 101 graded, hit 73.3% vs fair 72.1% → not overconfident.
- **Change made (rule 0b.4):** prop Over fair probabilities get a **-1.5 pt calibration haircut** (half the measured no-vig gap, because all of it comes from one week of 14 games and game-level shocks aren't fully captured by player clustering). Re-measure next week; move to the full gap if it persists.

**Lessons applied this run**
1. **Consensus de-vig method matters.** Proportional de-vig of other books' two-sided alt rungs ran 3-7 pts below my Pinnacle-anchored model at -400 to -700 prices; a power de-vig closes that to 0-2 pts. Use power de-vig for alt ladders (it allocates more vig to the long side).
2. **Big-dog alt spreads need a total check.** Empirically (2010+), 7.5-10 pt favorites win by 21+ about 17% with totals ≤44 and 18-21% with higher totals. TEN +20.5 (total 54.5) gets only half the power-model shade.
3. **Tuesday pool was thin:** with the haircut, every eligible prop is -1.5% to -3% EV and the best sides are about break-even, so all three parlays clear the floor at 0.971-0.979 and are staked $50. No stake above $50 until props or sides show a real edge.
4. **No leg reuse across parlays this slate**, and every parlay's legs are in different games (concentration lesson from Week 9).

## 2026-11-19 review (Thursday run, ESPN Week 11)
**Record:** nothing new to grade. Week 10 was fully graded on Tuesday (parlays 11-6, +$215; pick'ems 9-5, season 32-10). The 2026-11-17-tue slate's games start tonight (IND@HOU) at the earliest, and `history/legs.csv` gained no rows, because no snapshot in `odds/` has a final game that isn't already graded. No `-news` slates exist yet (the tracking routine logged no bets).

**Tuesday slate, interim line movement (DK at publish → DK 17:40Z Thursday, not CLV):** 2 toward us, 4 away, 1 flat.
- Toward us: Cousins 17.5 completions (-610 → -660), SF +6.5 (-451 → -455, consensus also firmer).
- Away from us: CAR +8.5 (-577 → -472), TEN +20.5 (-506 → -475), PIT +6.5 (-620 → -596), Chase 59.5 (-463 → -451).
- Flat: Chase Brown 49.5 (-497).
- The CAR move came from DK alone. The other books' median implied stayed at about 0.87 throughout, so DK is now about 4.5 pts *cheaper* than the market on that ladder. It is not a sharp move against Carolina.
- Early-week vs Sunday tally: no change (Week 11 not graded).

**Lessons applied / learned this run**
1. **Use the tracking snapshots to tell DK-only moves from market moves.** The 3b check now compares DK's price path with the other books' median at the same rung. A DK price drifting cheaper while the rest of the market holds (CAR +9.5: -630 → -512 vs a steady 0.877 median) counts as a buy signal, not a warning.
2. **Cap the power-model shade at 2.5 prob pts per leg.** Converting a sub-1-pt power shift with the empirical margin density near key numbers (3, 7) can add 4+ pts at some rungs (CAR +6.5 came out at +4.1). Capping it keeps published `fair` within the "trust the market" spirit. The power ratings also compress big spreads (best-fit scale 1.5×), so I scale the model before taking the gap.
3. **Big-spread alt lines need a wider, shifted sample.** The unshifted ±1-pt window has too few games at spreads of 15-16, and the model drifted 10+ pts from the consensus (MIA +21.5). For |spread| ≥ 8 I now use favorite-folded games within ±3 pts, shifted by whole points. That brought the model back within about 2 pts of the consensus.
4. **4b vs the 60% team-leg rule:** a 7-leg Tue/Thu slate can't satisfy both (3 required props leave 4/7 = 57% team legs). Like Tuesday, I keep the variety minimum and use exactly 3 props, one per parlay.
5. **Prop haircut held at -1.5 pts** (no new graded rows to re-measure).
6. **Waiting for Thursday's practice reports paid off.** Mayfield was limited Thursday, Tuten was off to the side, and none of the chosen players were affected. Between 18:05Z and 20:13Z, DK moved CAR +9.5 from -512 to -584 (toward the other books) and JT 9.5 rec yds from -354 to -394, both in our direction. Those legs carry less EV now but already have positive line movement. Track their CLV at close.

## 2026-11-22 review (Sunday run, ESPN Week 11)
**Record:** only TNF is final (IND 3 @ HOU 26).
- **Legs:** Jonathan Taylor 10+ rec yds (2026-11-17-thu-2) **lost**: 4 catches for 6 yards on 5 targets. **Parlay thu-2 lost: -$50** (its JAX +2.5 leg no longer matters). Expected profit at publish was about $0, so this was -$50 of bad luck on one leg.
  - Why: the Colts scored 3 points and Daniel Jones threw for 144. The script we wanted (Indy trailing and checking down) happened, but every RB catch was a short dump-off (long gain 5 yards). Mostly variance on a low-yardage rung. It also shows a news risk the Tue/Thu rules point at: the Colts released Jones the next day.
- **Early-week vs Sunday tally (running):** Week 11 Tue/Thu props so far 0-1 (JT). Week 10 Tue/Thu props 6-4 at 0.84 implied. Sunday props Week 10: 10-1. Keep counting. Tuesday will grade 13 more games.
- **Pick'ems:** HOU (0.86) **won**. Week 11: 1-0. Season: 33-10.
- **CLV:** JT 9.5 went from -394 to -384 at DK. `clp` 0.759 vs publish no-vig 0.794 gives **-3.5 pts**. Running CLV for graded legs with `clp`: 0 of 29 positive, average -3.3 pts. The method mismatch from earlier weeks still explains most of that gap: the publish `mkt` came from one-sided ladder fits. This slate's `mkt` uses the same per-book power de-vig as the close, so these legs will be the first fair test.
- **Moneyline-parlay scorecard:** no Week 11 ML bonus graded yet. Today's ML picks within 3 pts of Pinnacle: BUF, CHI. More than 3 pts off (the power shade): DAL +2.6, JAX +2.5, CIN +2.5. Track whether `cl` moves toward them.
- **News bets (`-news` slates):** none placed this week; the tracker found nothing at the 5-pt (props) / 3-pt (team) thresholds.

**Line history:** +1,917 graded rows for IND@HOU from the 2026-11-17 tue/thu snapshots (447 TD, longest-reception and DNP rows skipped).
- In this one game, short-priced prop Overs hit far below implied (deduped: -250..-399 26% vs 76%, -400..-649 54% vs 84%, -650+ 82% vs 92%). Team markets: -650+ 88% vs 94%.
- That is the same direction as Week 10's 14 games, but it is one 26-3 game, so it is a single correlated draw. **The prop haircut stays at -1.5 pts.** I'll re-measure Tuesday with all 13 Week 11 games, and move to the full measured gap (about -3 pts) if it holds.

**Lessons applied this run**
1. **Watch DK-only drifts vs whole-market moves.** Using the tracking snapshots, I dropped legs where the whole market moved away: Ollie Gordon 40+ (other books' median 0.80 to 0.73), Gibbs 50+ (0.93 to 0.89) and Sutton 10+ (0.92 to 0.89). I kept legs where only DK drifted cheaper while the other books held: Flournoy -600 to -373 (median 0.84 to 0.83), Purdy, Jameson Williams.
2. **Concentration across the week:** no leg identical to an open Tue/Thu leg (Bills -3.5 and Chase Brown 50+ were avoided). The Thu-2 parlay is already lost, so its JAX +2.5 leg adds no exposure to today's Jaguars ML legs.
3. **Weather:** heavy rain and wind in Chicago and light rain at MetLife. No passing, receiving or kicking overs in either game. In those games I used the Bears team-total under, Swift's and Skattebo's rush+rec yards, and Jacksonville sides.
4. **The 60%-team-legs vs 4b conflict again:** 14 core legs, with 2 QB, 2 RB and 2 WR/TE props required. That leaves 8 team legs (57%), exactly one prop per parlay.
5. **Bonus parlays keep at most one leg shorter than -700**, the same as core. That forced me to choose between the Chiefs and Bills MLs for the ML bonus.

## 2026-11-24 review (Tuesday run, ESPN Week 12 slate; Week 11 fully graded)
**Week 11 record (2026-11-17 tue/thu/sun), graded from ESPN box scores (nflverse cross-check)**
- **Parlays: 5-10, -$538 on $1,250 staked.** The slates' own fair probabilities expected about +$8, so this was a -$546 swing. That is far outside one week's noise for these stakes, and the line-history and CLV numbers below say part of it was our pricing, not just luck.
  - Tue: 1-2, -$82 (expected -$4). Thu: 2-1, +$19 (expected +$3). **Tue+Thu: 3-3, -$63.**
  - Sun core: **0-6, -$550** (expected +$9). Sun bonus: 2-1, +$75 (expected $0): sun-7 and sun-8 (5-leg prop/team) won; the ML bonus sun-9 lost on JAX and CIN.
- **Legs (unique):** Tue/Thu team 6-2 (avg implied 0.84), props 3-3 (0.83). Sunday team 7-4 (0.82), props 9-2 (0.82). In the backtest's -150..-500 cost bucket, team legs went 2-7 (0.76 implied) and props 6-11 (0.81).
- **Why the losses happened:**
  - **Upsets and near-misses on sides:** NYG beat JAX 23-18 (JAX ML lost twice, JAX +2.5 lost); WAS beat CIN 22-20 (CIN ML lost twice); TB +9.5 lost by exactly 10 (key number); TEN +20.5 lost by exactly 21; MIN +11.5 lost by 25 (Kyler Murray out, blowout). The ML losses were plain upsets of 0.72-0.75 favorites. The 10 and 21 losses were bad beats, but we chose rungs one point short of a cover in both.
  - **Props:** Chase 31 yds (59.5 needed) and Chase Brown 36 (49.5) in a 22-20 game where Cincinnati scored 20; Flournoy 11 (19.5); Skattebo 48 (49.5, by 2 yards); Jonathan Taylor 6 (9.5). Mostly variance, but Tue/Thu props are now 9-7 over two weeks at about 0.83 implied.
- **Stake tiers (core):** $150: 0-1, -$150. $100: 1-3, -$261. $50: 2-5, -$202. **Two weeks of tiers:** $150 2-2 (-$148, stated P ~0.69), $100 5-4 (-$112), $50 3-7 (-$266). The bigger tiers are not beating their stated P(hit). One more week before the 3-week rule applies; this slate is all $50 anyway.
- **Pick'ems: 9-4** (newest pick before kickoff; HOU from Thursday, the rest from Sunday). Misses: PIT (0.66), LAC (0.61), JAX (0.74), CIN (0.75). Expected about 9.4. **Season 41-14.** Near coin flips (0.50-0.58): CAR 0.58 won → running 2-3. Underdog picks: none.
- **Moneyline-parlay scorecard (running):** sun-9 lost. The three ML picks shaded ~2.5 pts above Pinnacle went 1-2: DAL won (close moved slightly away, -344 → -336); JAX lost (close moved toward us, -255 → -265); CIN lost (flat). Tally: shaded/fade ML picks 1-2; closing moves 1 toward, 1 away, 1 flat. Too early for the 6-8 Sunday rule.
- **CLV (36 graded legs with `clp`, all three Week 11 slates):** 4 of 36 positive, average **-2.7 pts** (team -2.5, props -2.9; Tue -2.3, Thu -3.8, Sun -2.5). DK's own price moved toward us on 23 of 36 (+0.5 implied pts). Last week I blamed a method mismatch and switched the publish `mkt` to a per-book power de-vig. It didn't close the gap. The remaining gap is real: the power de-vig plus model blend ran about 2.5-3 pts above the close's proportional/Pinnacle measure. **Fix this run:** the publish `mkt` now uses exactly the close's method (Pinnacle proportional de-vig when it has both sides, else the median proportional de-vig of the `cs` books excluding DK and BetOnline; Over-only ladders scaled by each book's main-line overround). Next week's CLV is like-for-like.
- **Early-week vs Sunday tally (running):** Tue/Thu parlays W10 2-4 (-$201), W11 3-3 (-$63) → **5-7, -$264**. Tue/Thu props W10 6-4, W11 3-3 → **9-7 at ~0.83 implied** (about 56% hit). Tue/Thu team legs W10 3-1, W11 6-2 → 9-3. Sunday parlays W10 7-1 (+$417), W11 2-7 (-$475). The gap the owner asked about is clearest in Tue/Thu props, so this Tuesday slate uses none (see below). One more week before the 3-week rule; if Tue/Thu props stay this far under implied, they stay out.
- **Leg-cost check (first week):** Week 11 picked legs in the -150..-500 bucket: team 2/7 (0.76 implied, backtest cost -2..-3%), props 6/11 (0.81 implied, backtest cost -7..-9%). Too small to read alone; keep the running tally.
- **News bets:** none placed in Week 11 (the tracker found nothing at its thresholds).

**Line history (history/legs.csv): +28,058 graded rows** for the 12 Week 11 games in the tue/thu/sun snapshots (4,120 TD-scorer/longest rows and 242 ungradable rows, mostly DNPs, skipped).
- Week 11 alone repeated Week 10. Deduped prop Overs hit **60.9% vs 65.4% implied** (-150..-249), **67.3% vs 75.7%** (-250..-399), **78.2% vs 83.2%** (-400..-649), **87.8% vs 92.2%** (-650+). Team legs were 3-5 pts under implied in every bucket (61.2/71.0/78.0/90.8 vs 65.4/75.5/83.1/93.8).
- Weeks 10+11 combined (26 games, 476-622 player-game clusters per prop bucket): prop Overs trail DK implied by 5.7-9.2 pts and the logged no-vig `mkt` by 1.4-6.7 pts. Team legs trail implied by 2.5-4.5 pts and sit within about 2.5 pts of `mkt` (under it at -650 and longer, over it at -650 and shorter). Proportional de-vig of DK's own ladder (about 4.5% overround) lands close to the actual prop hit rates at -400 and shorter, and 2-5 pts high at -150..-399.
- **Picked legs: 137 graded, hit 72.3% vs stated fair 74.8%.** That's 2.5 pts overconfident on 60+ legs, so rule 0b.4 applies.
- **Changes made:** (1) market baseline switched to proportional de-vig (above); (2) prop Over haircut is now -2 pts *below the proportional consensus*, which is about -4 to -5 pts below last week's power baseline; (3) the power-rating shade is halved (cap 1 prob pt on sides) and the empirical-history shade is capped at 25% of its gap and ±1.5 pts; (4) the empirical alt-spread lookup now conditions on the total (±3.5) as well as the spread, because a 47.5-total game's margins are wider than a 40.5's.

**Lessons applied this run**
1. **Honest prices leave almost nothing above break-even on a Tuesday.** With the new baseline, every Tue-eligible prop (QB with no injuries, lead backs, 84%+ snap receivers) priced at -3% to -8% EV, even where DK was 3-4 pts cheaper than the other books. No prop-carrying parlay could reach the 0.97 profit floor. Variety never overrides the floor, so this slate has no props and only the minimum 2 parlays.
2. **Stale power ratings:** the EPA model liked the Rams by 3 more points than the market, but Puka Nacua (MCL surgery, out for the season) played most of those games and Micah Parsons debuts for Green Bay on Wednesday. I set the Rams/Packers power shade to 0. Always check whether a model gap is just news the ratings haven't seen.
3. **Concentration:** no two parlays share a game. Only pairs involving the Rams' or Chiefs' alt spreads cleared the floor, so I split them across the two parlays rather than stacking both in one.
4. **DK moneylines are still 2-7 pts worse than Pinnacle** (DAL -469 vs 0.779 no-vig, CIN -610 vs 0.815) for the fourth straight week. No ML legs.
