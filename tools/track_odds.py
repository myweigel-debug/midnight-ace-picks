#!/usr/bin/env python3
"""Snapshot the NFL board and main prop markets for line-movement tracking.

  python3 tools/track_odds.py            # writes odds/track/<UTC date>/<HHMM>Z.json.gz

Fetches through the Homies Sportsbook proxy (homies-sportsbook, falling back to homies-casino):
the board (spreads/ML/totals) plus the lines, passing, rushing and receiving groups for every game
kicking off in the next 7 days. Costs roughly 1 Odds API credit per market returned (~25-35 per game).
Prints a one-line summary with credits remaining.
"""
import datetime as dt
import gzip
import json
import os
import subprocess
import sys
import time

HOSTS = ['https://homies-sportsbook.vercel.app', 'https://homies-casino.vercel.app']
GROUPS = ['lines', 'passing', 'rushing', 'receiving']
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get(path):
    last = None
    for host in HOSTS:
        for i in range(3):
            out = subprocess.run(['curl', '-sS', '-m', '40', host + path], capture_output=True)
            try:
                data = json.loads(out.stdout)
                if 'error' not in data:
                    return data
                last = data['error']
            except ValueError:
                last = out.stderr.decode()[:200] or 'bad response'
            time.sleep(2 ** i)
    raise RuntimeError(f'{path}: {last}')


def main():
    now = dt.datetime.now(dt.timezone.utc)
    board = get('/api/odds?scope=board')
    games, remaining = [], board['meta'].get('remaining')
    for g in board['games']:
        t = dt.datetime.fromisoformat(g['t'].replace('Z', '+00:00'))
        if not (now - dt.timedelta(hours=4) < t < now + dt.timedelta(days=7)):
            continue
        rec = {k: g[k] for k in ('id', 'home', 'away', 't')}
        rec['groups'] = {'board': {k: g.get(k) for k in ('mk', 'bk', 'px', 'cs')}}
        if t > now:  # pre-game only: live prices aren't comparable
            for grp in GROUPS:
                try:
                    d = get(f'/api/odds?scope=event&id={g["id"]}&group={grp}')
                    rec['groups'][grp] = {k: d['game'].get(k) for k in ('mk', 'bk', 'px', 'cs')}
                    remaining = d['meta'].get('remaining', remaining)
                except RuntimeError as e:
                    rec['groups'][grp] = {'error': str(e)}
        games.append(rec)
    folder = os.path.join(ROOT, 'odds', 'track', now.strftime('%Y-%m-%d'))
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, now.strftime('%H%M') + 'Z.json.gz')
    with gzip.open(path, 'wt') as f:
        json.dump({'at': now.strftime('%Y-%m-%dT%H:%M:%SZ'), 'games': games}, f, separators=(',', ':'))
    print(f'saved {os.path.relpath(path, ROOT)}: {len(games)} games, {os.path.getsize(path) // 1024} KB, credits remaining {remaining}')


if __name__ == '__main__':
    main()
