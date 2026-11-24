#!/usr/bin/env python3
"""Build a compact FEN-to-opening lookup from the CC0 Lichess opening dataset."""
import csv
import io
import json
from pathlib import Path

import chess
import chess.pgn

source = Path("chess-openings/dist/all.tsv")
target = Path("dist/openings/openings.json")
target.parent.mkdir(parents=True, exist_ok=True)
lookup = {}

with source.open("r", encoding="utf-8", newline="") as handle:
    for row in csv.DictReader(handle, delimiter="\t"):
        pgn = row.get("pgn", "").strip()
        if not pgn:
            continue
        game = chess.pgn.read_game(io.StringIO(pgn))
        if game is None:
            continue
        board = game.board()
        ply = 0
        for move in game.mainline_moves():
            board.push(move)
            ply += 1
            # FEN's first four fields identify the position, including castling and en-passant rights.
            key = " ".join(board.fen().split()[:4])
            candidate = {"eco": row.get("eco", ""), "name": row.get("name", ""), "ply": ply}
            previous = lookup.get(key)
            if previous is None or (candidate["ply"], len(candidate["name"])) > (previous["ply"], len(previous["name"])):
                lookup[key] = candidate

target.write_text(json.dumps(lookup, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"Built {len(lookup)} named opening positions -> {target}")
