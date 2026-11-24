# Chessmes

Chessmes is a mobile-friendly chess game replay and analysis page.

## Features

- Load a PGN or retrieve a public Chess.com game using the player's username and game URL.
- Flip the board to the entered player's side.
- Step through a finished game one half-move at a time with the left and right arrows. The recorded game is never modified.
- Analyze every move sequentially with Stockfish 16 NNUE in a browser Web Worker.
- Show move-quality labels and the engine's preferred alternative.

## GitHub Pages

The workflow in `.github/workflows/pages.yml` builds a Pages artifact and downloads the pinned Stockfish 16.0.0 browser engine files. In the repository settings, open **Pages** and select **GitHub Actions** as the deployment source. New pushes to `main` then trigger deployment.

## Third-party software

- Stockfish.js 16.0.0: https://github.com/nmrugg/stockfish.js — GPL-3.0. The full license is published at `engine/STOCKFISH-LICENSE.txt` on the deployed site.
- chess.js 0.10.3: https://github.com/jhlywa/chess.js — BSD-2-Clause, loaded from cdnjs.

Stockfish is used unmodified and communicates with the page through the UCI Web Worker interface.
