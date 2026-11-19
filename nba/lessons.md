# NBA lessons

Claude's running notes on what works and what doesn't in the daily NBA slates. Each run adds a short dated section; Monday runs add a full weekly review. The season table at the top tracks parlays W-L, profit, pick'ems and CLV by week.

## Season table
| Week | Parlays W-L | Profit | Expected | Pick'ems | Avg CLV |
|---|---|---|---|---|---|

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
