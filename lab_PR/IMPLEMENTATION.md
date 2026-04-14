# Project Snapshot

---

## Project Overview

**A short recap of:<br>
Research question.<br>
Algorithm.<br>
Current implementation status.**

This is a team builder for the Pokemon games. This team generator is unique because it takes into account popularity in addition to stat and type distribution to create interesting teams for memorable Pokemon play throughs.

### Algorithm

Pokemon data is stored in nested dictionary format (abbreviated example):
```
{Pokemon_name:  {dex#: #},
                {type: Grass},
                ...
}
```

**`fetch_stats()`** - Read in data from stats dataset:
- For each line in stats dataset:
  - If Gen 1:
    - Check for/fix name data (e.g. Nidoran♀)
    - Fill dictionary with info (type, stats, name, dex number)

**`fetch_pop()`** - For each line in popularity dataset:
- Check and fix valid inputs (some Pokemon names have typos)
- If Pokemon already in dictionary:
  - Add new popularity weight data in nested dictionary

**`read_json()`** - *(planned)*:
- Read in Pokemon information from JSON file to replace the above two functions at run time
- Not yet implemented

**`build_team()`** - Build one initial team:
- `choose_poke()`: Randomly choose 6 unique Pokemon, excluding unevolved forms
- `score_team()`: Calculate team score using `score_pop()`, `score_team_types()`, `score_team_stats()`

**`sampler()`** - Gibbs sample until threshold (threshold testing ongoing):
- `swap_teammate()`: Chooses a new Pokemon to try to swap in
- `score_team()` for both old and new possible team
- Choose which team is better, loop until threshold is met

**User-directed swap:**
- After team is generated, user can choose to swap a specific Pokemon
- Force a swap using optional `sampler()` parameter to swap only one specific Pokemon in team

**Implementation status:** Team generation, scoring, and shuffling is working, but lacks some intended scoring features. Not yet implemented: generation expansion, JSON format simplification, and UI.

---

## What Is Implemented

**Describe what parts of your pseudocode are fully implemented, partially implemented, or still missing. If there are deviations from your pseudocode (e.g., additional steps, different data structures), explain why.** 

Currently, the program can generate a team, score it, and make swaps to improve the team score. It can also be directed to swap a specific Pokemon of the user's choice, which will be part of the final implementation UI.

Not yet implemented: the JSON data file functions that will replace the need for the user to download the datasets.

---

## Prototype Demo Description

**Describe a minimal “prototype run”:<br>
Which script or notebook to run?<br>
Which input files does it expect (from data/).<br>
What output does it produce and where?<br>
Include one small example of expected behavior or output (e.g., a snippet of console output, a summary of results, a short description of what you see).**

A minimal run filters the provided datasets to only the Generation 1 Pokemon, which includes 150 Pokemon. These files can be downloaded from the databases or will be provided temporarily for this peer review. It currently outputs results directly into the output cell of the notebook. The program is still in the development phase and so the driver cell runs through several test types and reports results.

Currently, the driver code generates a team and score, makes swaps to improve the score, and reports back the new team and score. It also shows the implementation for a directed swap of the user's choice. Final implementation will only show the final team and ask for a directed swap. It might also have type information and Pokemon images.

**Sample output:**
```
This is our first team:
['Victreebel', 'Charizard', 'Clefable', 'Lapras', 'Dewgong', 'Golduck']
8.5

This is our new team:
['Persian', 'Venomoth', 'Mr. Mime', 'Fearow', 'Dewgong', 'Golem']
17.5

This is the team after swapping Persian:
['Electrode', 'Venomoth', 'Mr. Mime', 'Fearow', 'Dewgong', 'Golem']
19.0
```

---

## Data Documentation

**Explain:<br>
The nature and origin of your test data.<br>
Any preprocessing steps you applied (normalization, filtering, sampling).<br>
What you consider “ground truth” (if any) or how you are currently interpreting the outputs.**<br>

The data comes from two datasets: one from Kaggle which is sourced from the Pokemon video games, and a popularity dataset on Google Sheets which was the result of a survey of Reddit users. The program requires some small amount of formatting on input of the data to correct inconsistencies in naming as well as removal of non-unicode characters.

The former file is fairly "truthful" as it comes from the source Pokemon material. The latter is highly subjective, as it represents a relatively small userbase of self-reported information. Links to the data can be found in `requirements.txt`, as well as temporarily hosted in the `data/` folder until the JSON implementation is finished.

---

## Initial Observations

**Summarize what you have learned from the prototype so far:<br>
Does the algorithm behave as expected on simple examples?<br>
Did you observe surprising behavior (e.g., instability, runtime, unexpected outputs)?<br>
Note any preliminary performance measurements or simple comparisons (even if informal).**

One thing that was not behaving as initially intended was the popularity scorer. I realized that I need to include popularity of pre-evolutions when evaluating team candidates. This will be implemented in the next update. I noticed this by generating plots that tracked how often each Pokemon was being chosen over many runs, and that some Pokemon were being chosen more often than expected.

I have also been continuing to tweak the popularity thresholds as I go, somewhat based on those generated plots. Increasing the threshold for swaps until stabilization slightly increases work done but not appreciably. Adding more generations may require more swaps but memory will not be affected.

---

## Reflection on Changes and Challenges

**Discuss:<br>
Where your implementation diverged from your original plan in Part 2.<br>
Key challenges faced (e.g., data issues, debugging difficulties, design changes).<br>
Decisions you made to keep the project manageable (e.g., simplifying the model, reducing input size).**

I had some extra ideas that I haven't decided whether to implement, including HM move options, catch locations, and a type weakness scorer. Most likely to be implemented would have been the weakness scorer, but it is probably redundant to the type scorer. The other two options are probably not reasonable to implement over the given timeline, as they would require drastic expansions to the datasets for each generation. To reduce the size of the JSON I might end up commenting out unused Pokedex fields such as the weaknesses and unused evolution indicators.

When considering expanding the scope to more generations, I realized that for higher generation Pokemon there are some unused fields such as `mega_evolution` that I need to review to ensure these Pokemon are not being chosen by the generator, since they are battle forms and would add extra entries that would skew results. I'll need to review this carefully, possibly adding in more fields to filter these Pokemon out.

I also had to implement `os.path` file handling last minute because I realized I had hard coded paths for Windows only.

---

## Next Steps

**Outline what you still need to do for the final part:<br>
Additional features or refactoring.<br>
More robust testing or validation.<br>
Documentation and Quick Start preparation.**

I still need to implement the JSON file storage to replace the need to download the datasets. During testing and reporting of choices made by the program, I realized that the current implementation does not take into account popularity of pre-evolved forms when choosing Pokemon, skewing results that might choose popular Pokemon whose final evolution forms are not very popular. I may need to continue to fine tune the scoring and sampler thresholds after implementing this change.

After that, my next step will be to implement generation controls, allowing a user to choose one or more generations to pull from. I will need to make sure the expanded Pokemon list does not have any further naming inconsistencies and that data coverage is sufficient.

I have not yet started looking at the graphical UI via Streamlit, including any extra information I want to include for visualization of the final team. I expect this will take a bit of time and need to plan ahead.


## Generative AI Disclosure (If Used)

**If you used generative AI at this stage (e.g., for debugging or code scaffolding):<br>
Add an appendix Generative AI Usage.<br>
Include tool/version, prompts, and a transparent account of how the tool influenced the implementation.<br>**

For the `fetch_stats()` function I had Claude 4.6 help generate the input dictionary where it would otherwise have been very tedious to type out each of the commands. Type casting was done by hand and validated.