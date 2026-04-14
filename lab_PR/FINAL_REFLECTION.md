## Note for Peer Reviewers
If you came here from GitNotebooks, please find the link to run the app in the `README.md` on the root directory page.

| File | Description |
|------|-------------|
| `pokemon.ipynb` | Notebook code |
| `pokemon.py` | Copy of the program for Streamlit integration |
| `app.py` | Streamlit integration (only for running the app) |

---

## What Went Right
I tried to make every function as small as possible to make it clear what each function was doing, so they could be called in a predictable way.

This project taught me a lot about file handling, creating and reading JSON files, and creating a workflow with many interacting functions. Using dictionaries effectively was also an early obstacle, but I became more comfortable as the project progressed.

---

## What Went Wrong or Was Hard
Importing the data was significant upfront work to ensure all fields and names were compatible between the input files. One thing I would have done differently would be to use JSON earlier, which would have required less rewriting of the program once things were established.

---

## Algorithmic Lessons
In the end, the Gibbs algorithm I set out to implement turned into something more similar to a greedy hill-climbing algorithm rather than true Gibbs sampling. The output doesn't represent the whole distribution of Pokemon, but if it were run many times, it could generate a more complete picture of how all Pokemon rank in popularity and stats — more closely aligning with what we'd expect from Gibbs sampling.

---

## Future Directions
A more sophisticated scoring algorithm would have been useful. Something I didn't get to implement due to complexity, but which would be practical, would be an option to generate full teams that could use all HMs (moves required to traverse the overworld). I was concerned that filtering Pokemon further by requiring HMs would not be compatible with my single-swap method, as it would drastically restrict the available choices — which are already limited by filtering to fully-evolved Pokemon.

Of the ~1,100 Pokemon available across the 8 generations in the database, roughly 550 were selected after 10,000 team generations. Earlier generations had more eligible Pokemon, while later generations had many filtered out due to battle forms.

Additionally, better or supplemental datasets could support more recent generations or richer popularity information.

---

## Generative AI Disclosure (If Used)
Claude was also used to speed up the Streamlit integration to research options for layouts and formatting, as well as formatting of Markdown files.

---


## Datasets Used

**Complete Pokedex V1.1**
- [Kaggle](https://www.kaggle.com/datasets/joshuabetetta/complete-pokedex-v100?select=Complete+Pokedex+V1.1.csv)

**Pokemon Survey Results**
- [Reddit thread](https://www.reddit.com/r/pokemon/comments/1f3midv/update_everyone_is_someones_favorite_survey_20/)
- [Google Sheets data](https://docs.google.com/spreadsheets/d/1hvsP3GgXZaGBM1nOy6Px8qy-JhRIihjHrMaYTUnIvZ8/edit?gid=0#gid=0)

**Pokemon Sprites**
- [PokeAPI GitHub](https://github.com/PokeAPI/sprites)