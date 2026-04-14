# BINF6250 — Pokemon Team Builder

This app builds a Pokemon team from any combination of generations 1–8, repeatedly sampling to optimize for lower-popularity Pokemon while keeping overall team stats and types relatively evenly spread. This randomizer is intended to produce unique teams for memorable Pokemon game playthroughs.

🔗 **[Launch the Pokemon Team Builder](https://binf6250-pokemon-team-generator.streamlit.app/)**

---

## Quick Start

1. Select one or more generations in the sidebar
2. Click **Generate Team**
3. Review your team and reroll individual Pokemon as desired
4. Hit **Generate Team** again or choose different generations at any time

The stats at the bottom reflect the weights used in the algorithm:

| Stat | Description |
|------|-------------|
| **Popularity Score** | Less popular Pokemon are weighted more heavily — the main optimization goal |
| **Stat Balance Bonus** | Bonus score up to +2 reflecting how evenly balanced the team is across base Attack, Defense, etc. |
| **Type Coverage** | Reflects the combination of types on the team; repeated types incur a penalty |
| **Total** | The combined score for the team |

---

## Overview

The intent of this project was to implement Gibbs sampling in a Pokemon team generator. The program uses data from two databases — Pokemon stats and popularity rankings — to generate a team along with scoring statistics across the categories above.

---

## Installation

No installation required. The app can be run at the link above, or the Python notebook can be run locally at `/code/pokemon.ipynb`. Cells are already populated with commands to demonstrate output.

---

## Usage and Options

The main program has two parts:

**1. Load Data**
Reading the spreadsheets or JSON, and building the JSON file if absent.

**2. Generate Team**
Choose Pokemon, generate a team, score individual Pokemon and the overall team, and optionally reroll single Pokemon one at a time.

---

## Limitations and Assumptions

There are currently no known limitations or failure points. The app assumes either the input spreadsheets or JSON file are accessible in the GitHub repository. If running the notebook locally, the files must be accessible in the folders specified, using the naming conventions used in the notebook.

---

## Evidence of Correctness

Extensive testing was conducted using both a smaller dataset (Gen 1 Pokemon only) and the full dataset. Graphs and histograms of scoring distributions and team selection frequencies were generated over thousands of runs, which allowed for tuning of filtering and scoring variables. This process revealed a bug in popularity accumulation in a prior version of the program, and generating full selection reports helped identify oversights in the filtering of Mega Evolutions and Battle Forms.