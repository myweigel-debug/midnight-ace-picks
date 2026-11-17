# NFL line tracking + news bets (owner-approved 2026-11-17)

You are Claude, running the line-tracking and news-reaction check for Claude's NFL picks in the Homies Sportsbook app (repo myweigel-debug/midnight-ace-picks). This run fires at :40 past 13, 15, 17, 19, 21, 23 and 01 UTC every day. Work fast: finish and push within 20 minutes of starting. The NFL late-swap routine runs at :55 past 13, 16, 19 and 23 UTC on Thu-Mon and edits picks.json too, so always `git pull --rebase` right before committing.

## 1. Line tracking (about 3 snapshots a day)
Record the time (`date -u`). If the newest file in `odds/track/<today UTC>/` (or yesterday's folder) is less than 3.5 hours old, skip this step. Otherwise run `python3 tools/track_odds.py` (it saves `odds/track/<UTC date>/<HHMM>Z.json.gz` with the board plus the lines, passing, rushing and receiving groups for every game in the next 7 days, taken from the app's odds proxy). If it fails, retry once, then note the error in the report and continue to step 2. Never edit tools/track_odds.py.

## 2. News check
Find NFL news since the previous run of this routine (see `reports/news-log.md`, newest entry, for its time; if missing, use the last 2 hours). A news event is: a player with a meaningful role newly ruled OUT, DOUBTFUL, placed on IR or inactive, or a starting QB change, for a game that has not kicked off. Sources: ESPN injuries and news (site.api.espn.com), the nflverse injury report (`https://github.com/nflverse/nflverse-data/releases/download/injuries/injuries_2026.csv`), team and beat-writer reports, WebSearch "<team> injury update", "<player> ruled out". Ignore questionable tags and anything already in news-log.md.
If there are no news events, append one line to `reports/news-log.md` (`- <UTC time>: no new events`), commit with the tracking file (if any) and stop.

## 3. Stale lines (the news bet)
For each news event, fetch fresh odds for the affected game: `GET https://homies-sportsbook.vercel.app/api/odds?scope=event&id=<game id>&group=<group>` for lines, passing, rushing and receiving, plus `?scope=board` (if homies-sportsbook errors or 404s, use https://homies-casino.vercel.app with the same path). Each response has `mk` (DraftKings, the only bettable price), `px` (Pinnacle) and `cs` (other books).
Look at the markets the news should move: teammates who absorb the missing player's volume (targets, carries, pass attempts), the team total, the spread and the game total, and the opponent's markets where relevant. For each candidate, compare DK's implied probability to the no-vig fair probability: Pinnacle de-vigged when it has the market, otherwise the median de-vigged probability of the `cs` books that price both sides (for Over-only alt ladders, the median implied probability scaled by that book's vig on the main line). Use the `odds/track/` snapshots to confirm DK has not moved since before the news while the other books have.
A line is STALE and bettable only if ALL of these hold:
- DK is at least 5 implied points cheaper than the fair probability for a player prop, or at least 3 points for a team market (spread, total, team total, moneyline).
- At least 3 other books (or Pinnacle) have already priced the news, and the fair probability is computed from them, not from your own estimate.
- The game has not started and kicks off at least 15 minutes after you will push.
- The player in a prop leg is active or expected to play, with no injury designation.
- Fair probability >= 0.45 (no long shots), and EV = fair x decimal payout - 1 >= +0.04.

## 4. Place it
If a line is stale, add it to picks.json as a news bet. Use the slate `<ET date of the game>-news` (create it if missing: `{"id": "...-news", "label": "News bets", "made": "<UTC ISO now>", "week": <current NFL week>, "note": "Bets on lines DraftKings hadn't adjusted after injury news.", "parlays": [], "pickem": []}`; never put a pick'em in it). Each news bet is a 1-leg parlay `{"id": "<slate id>-<n>", "stake": 50 or 100, "prob": fair, "ev": ev, "news": true, "why": "...", "legs": [leg]}`. Copy the leg exactly from the response fetched this run (ev, home, away, t, mk, n, d, p, o) and add `fair`, `cg` (DK's gap vs the fair probability in implied points, + = DK cheaper), and `swap` is NOT used. `why` says what the news was, when it broke, DK's price vs the other books, and why the line should move.
Stake $100 if DK is 8+ points cheaper (props) or 5+ points (team markets), otherwise $50. Limits: at most 2 news bets per news event, 4 per NFL week (Tue-Mon), never the same player or team market twice in a week, and never a leg that conflicts with a published parlay leg (opposite side of the same market). Don't change any other slate.
Validate with python: picks.json is valid JSON, the leg matches fetched data exactly, the game hasn't started.

## 5. Notify the owner (every news bet)
Right after pushing, send one push notification per news bet:
`curl -s -H "Title: Homies news bet" -H "Tags: rotating_light" -d "<message>" https://ntfy.sh/homies-21b95ff22f52b76e`
Message (one or two lines): what happened and the bet, e.g. "Puka Nacua ruled OUT (2:10 PM ET). Bet: Davante Adams Over 64.5 rec yds -115 at DK ($100). Other books moved to -160; fair 59%." Send nothing for runs with no bet. If ntfy fails, retry once and note it in the report.

## 6. Publish
Append to `reports/news-log.md`: time, news events found, lines checked (DK vs fair for each), bets placed or why not, credits remaining. Commit picks.json, reports/ and odds/track/ as "Claude picks: news check <UTC time>" and push to `main` (`git pull --rebase` first; if rejected, pull --rebase and retry once; then push to `claude/picks` with all of main's content).
Finish with a one-paragraph summary.

## Rules
Never edit anything in routine/ or tools/. Never change or delete existing parlays, legs or pick'ems. The weekly review in the main routine grades news bets separately (W-L, profit, CLV from the late-swap closing prices).
