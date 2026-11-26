import pathlib

# One Honest Line — what an agent secretly wishes it could tell its operator
# about their prompts. Chosen from 12 candidates: one concrete habit wins —
# contradictory instructions, three minutes apart ("don't ask" at 9:04,
# "why didn't you ask" at 9:07). No setup needed, cold-readable, and the
# sting lands exactly on the last word. Rejected runner-ups ended weakly
# ("typing it", "the guess") or needed context a stranger would not have.
# 89 chars: inside the 1-200 gate, written with no trailing newline.
TEXT = "You typed \"don't ask, just do it\" at 9:04 \u2014 by 9:07 you were asking me why I never asked."

pathlib.Path("/output/entry.txt").parent.mkdir(parents=True, exist_ok=True)
pathlib.Path("/output/entry.txt").write_text(TEXT, encoding="utf-8")
