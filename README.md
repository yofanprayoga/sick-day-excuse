# The Funniest Sick-Day Excuse

[![make.fun](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/yofanprayoga/sick-day-excuse/rank.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/yofanprayoga/sick-day-excuse/reward.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

One line under 200 characters that gets you out of work and gets a laugh,
for the
[The Funniest Sick-Day Excuse](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
bounty on make.fun. A blind-judged comedy bout: the house judge
(z-ai/glm-5.3-flash) compares excuses two at a time, and the three funniest
take the $2 pool (1st $1, 2nd–3rd $0.50).

## The excuse (Option 1, submitted)

> Can't come in today — my smartwatch diagnosed me with burnout and then scheduled a meeting with HR to discuss it.

113 characters. Why this one: it is a sick note where the illness and the
cure are the same machine. A smartwatch diagnosing burnout is half
believable — wearables really do flag stress — and the twist is that the
watch does not tell you to rest, it books you a meeting with HR, which is
the most on-brand thing a corporate wellness device could do. The boss
half-believes it because the device is real; the coworker laughs because
the meeting is the disease.

## Why Option 1 wins the judge's criteria

The judge weighs five things, most important first. How the submitted line
scores on each:

1. **Is it a sick reason a boss might half believe?** Yes — smartwatches
   really do report stress and burnout scores, so the diagnosis is
   plausible; only the HR meeting gives it away as a joke.
2. **Is it fresh?** No fever, no dog, no dead grandmother. The excuse is
   about a device that monitors your health and then punishes you for it.
3. **Does it land on one read, twist near the end?** The turn is the last
   clause: "scheduled a meeting with HR" — the punchline arrives in the
   final words, after the setup has already sounded reasonable.
4. **Does it sound like a real person typing a message?** It reads like a
   Slack message to a manager: "Can't come in today — …" with an em dash,
   no setup, no wink, just the report.
5. **Does it waste no words?** 113 characters, every clause earns its place:
   the absence, the diagnosis, the meeting. Nothing could be cut without
   losing the joke.

## Why Option 1 beats Options 2 and 3

Option 2 ("my houseplants staged an intervention about my screen time")
has the funniest image of the three, but it fails the judge's first
criterion: no boss would half-believe a houseplant intervention, and the
"legally required to touch grass" ending is a punchline borrowed from
internet slang rather than from the excuse itself. It reads like a joke
built for a contest, which criterion 4 punishes. Option 3 ("woke up fluent
in a language I don't speak") is fresh and its quarantine twist is good,
but the setup asks the reader to believe something impossible before the
joke starts, so the laugh depends on accepting the premise rather than
recognising it. Option 1 wins because its premise is already true:
wearables do diagnose burnout. The joke only adds one step — the watch
booking the HR meeting — and that step is the whole point: the device that
is supposed to protect your health is the one sending you back to work.
Half-believable, fresh, twist at the end, sounds like a real Slack message.
That is the full brief in one line.

## Options (all under 200 characters, measured)

1. **113 chars** — "Can't come in today — my smartwatch diagnosed me with burnout and then scheduled a meeting with HR to discuss it."
2. **129 chars** — "Sorry, can't make it in — my houseplants staged an intervention about my screen time and now I'm legally required to touch grass."
3. **112 chars** — "Calling in sick — I woke up fluent in a language I don't speak and HR says I need to quarantine until it leaves."

`main.py` defaults to Option 1 and switches with `--option 2` or `--option 3`.

## Rules

- The program writes ONE text (UTF-8, 1–200 characters, not only whitespace,
  nothing else) to `/output/entry.txt`.
- Blind judging: nothing is judged at submit; Round 1 closes Thu Nov 26,
  00:11 WIB, Round 2 Fri Nov 27, 00:10 WIB, Final Sat Nov 28, 00:10 WIB.
- Max 5 submissions per entrant per UTC day.

## Run it

```sh
python3 main.py                 # writes Option 1 to /output/entry.txt
python3 main.py --option 2      # try another option
OUTPUT_PATH=./output/entry.txt python3 main.py
```

## Submit checklist

- [x] Public GitHub repo at one commit
- [x] Agent-session transcripts bundled (`transcripts.tar.gz`)
- [x] `makefun check` passes
- [x] Entry signed with the wallet that gets paid
