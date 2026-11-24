# Chessmes — asset attributions

## Chess piece artwork

- Set: Cburnett SVG chess pieces (`wK`, `wQ`, `wR`, `wB`, `wN`, `wP`, `bK`, `bQ`, `bR`, `bB`, `bN`, `bP`).
- Artist: Colin M. L. Burnett.
- Source: https://github.com/lichess-org/lila/tree/master/public/piece/cburnett
- License as distributed by Lichess: GNU General Public License v2.0 or later.
- License details and asset exceptions: https://github.com/lichess-org/lila/blob/master/COPYING.md

The SVG files are downloaded unmodified during the GitHub Pages build and stored under `pieces/`.

## Chess engine

Stockfish 16 browser build is distributed under GPL-3.0-or-later. Its license is included at `engine/STOCKFISH-LICENSE.txt`.

## Opening theory database

- Dataset: Lichess chess-openings, aggregated ECO opening names and move sequences.
- Source: https://github.com/lichess-org/chess-openings
- License: CC0 1.0 Public Domain Dedication.
- The GitHub Pages workflow builds a local FEN lookup from the dataset; no opening API is called by visitors.
