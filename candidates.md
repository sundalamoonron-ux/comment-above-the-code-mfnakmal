# Candidates — The Comment Above the Code

Judged on the house brief, in order: (1) funny comment about fragile legacy
code, (2) honesty stings — names a real, recognisable failure, (3) economical,
punchline lands on the last few words, (4) fresh angle, (5) reads like a real
codebase comment. Every pair was judged in both orders (A/B swapped).

| # | chars | line |
|---|-------|------|
| C1 | 91 | // TODO: remove this before anyone finds out it is the only thing holding payments together |
| C2 | 79 | // do not refactor. the last person who tried now works in a different industry |
| C3 | 71 | // this function works. nobody knows why. if you touch it, it will know |
| C4 | 66 | // yes, it is a 400-line if statement. no, we do not talk about it |
| C5 | 86 | // changing this line once took down prod for 3 hours. the line is still here. so am I |
| C6 | 85 | // I wrote this at 3am. I have never forgiven myself. it has never forgiven me either |
| C7 | 63 | // the tests pass because the tests are scared of this file too |
| C8 | 89 | // if this breaks, check the config. then check the other config. then update your resume |
| C9 | 65 | // this was a temporary fix in 2019. it now has a retirement plan |
| C10 | 68 | // do not delete. the database believes this comment is load-bearing |
| C11 | 76 | // the original author left the company. the code left with him, spiritually |
| C12 | 69 | // this works only on Tuesdays. do not ask why. we have all asked why |

## Tournament results (wins / games played)

- **C9: 11/11 — WINNER.** The "temporary fix that became permanent" is the most
  universally recognised legacy-code truth here; "retirement plan" is a tight,
  fresh turn that lands on the last two words, and it is the most economical
  of the top lines (65 chars). Beat C2, C5, C10, C1, C8, C3, C4, C6, C7, C11,
  C12 — mostly by a hair (margin 1), margin 2 over C8, C11, C12.
- C2: 10/11 (lost only to C9). "Now works in a different industry" is the
  biggest single laugh, but slightly less sting than C9's universal truth.
- C5: 9/11 (lost to C9, C2). Concrete incident stings, but the "so am I" tail
  is a beat longer than C9's turn.
- C10: 8/11 (lost to C9, C2, C5). Fresh "load-bearing" image; slightly less
  universal than the top three.
- C1: 7/11. High-stakes sting (payments), but the setup runs longer.
- C8: 6/11. Escalation works, but 89 chars for a three-beat joke.
- C3: 5/11. "It will know" is funny; the middle sags a little.
- C7: 4/11. Cute, but the sting is thin — tests being scared is a quip, not a
  failure named.
- C6: 3/11. "3am code" is a familiar trope; the turn is good but not fresh.
- C4: 2/11. Recognisable, but "400-line if" is a well-worn image.
- C11: 1/11. Too close to the "who wrote this" cliche the brief warns about.
- C12: 0/11. Quirky, but the weakest sting — no failure is actually named.

## Winner (verbatim, 65 characters)

```
// this was a temporary fix in 2019. it now has a retirement plan
```
