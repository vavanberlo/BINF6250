import streamlit as st
import pandas as pd
from pokemon import build_pokedex, filter_by_gen, build_team, sampler, score_team, choose_poke

st.set_page_config(layout="wide")

@st.cache_resource
def load_pokedex():
    #st.write("Pokedex Loaded!")
    return build_pokedex(force_rebuild = True)

#st.write("Welcome!")
full_pokedex = load_pokedex()

st.sidebar.write("What generation(s) to use?")
# selected_gens = st.sidebar.multiselect(
#     "Select Generations",
#     options=list(range(1, 9)),
#     default=[1]
# )

selected_gens = []
for gen in range(1, 9):
    if st.sidebar.toggle(f"Generation {gen}", value=False):
        selected_gens.append(gen)

if not selected_gens:
    st.sidebar.warning("Please select at least one generation.")
    st.stop()

if "selected_gens" not in st.session_state:
    st.session_state.selected_gens = None

# If gens changed, reset the team
if selected_gens != st.session_state.selected_gens:
    st.session_state.selected_gens = selected_gens
    st.session_state.team = None
    st.session_state.score = None

filtered_pokedex = filter_by_gen(selected_gens, full_pokedex)

# make this nicer
selected_gens.sort()
#st.sidebar.write(f"You picked {selected_gens} gens")

pokedex = filter_by_gen(selected_gens, full_pokedex)


# Build team
if "team" not in st.session_state:
    st.session_state.team = None

# Generate team buttons
if st.sidebar.button("Generate Team"):
    team, score = build_team(pokedex)
    st.session_state.team = team
    st.session_state.score = score


# Display team cards
if st.session_state.team:
    cols = st.columns(6)
    for i, name in enumerate(st.session_state.team):
        with cols[i]:
            with st.container(height=260):
                # display a pic
                dex_num = pokedex[name]["dex"]
                sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{dex_num}.png"
                st.image(sprite_url)
                # pokemon info
                st.write(f"**{name}**")
                st.write(pokedex[name]["type1"])
                if pokedex[name]["type2"]:
                    st.write(pokedex[name]["type2"] or " ")

            # stats - takes up a lot of space so it's collapsed by default
            # might remove. if False, doesn't appear
            if False:
                with st.expander("Stats"):
                    stat_labels = {
                        "hp": "HP",
                        "attack": "ATK",
                        "defense": "DEF",
                        "special_attack": "SpATK",
                        "special_defense": "SpDEF",
                        "speed": "SPD"
                    }
                    stats = ["hp", "attack", "defense", "special_attack", "special_defense", "speed"]
                    for stat in stats:
                        value = pokedex[name][stat]
                        st.write(f"{stat_labels[stat]}: {value}")
                        st.progress(value / 255)
                    
            # reroll button                    
            if st.button("Reroll", key=f"reroll_{i}"):
                new_poke = choose_poke(st.session_state.team, pokedex)
                st.session_state.team[i] = new_poke
                st.rerun()

    # Display team statistics
    if st.session_state.team:
        team_pop, stat_bonus, type_score = score_team(st.session_state.team, pokedex)
        total = team_pop + stat_bonus + type_score

        st.divider()
        st.subheader("Team Score Breakdown")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Popularity", round(team_pop, 2))
        with col2:
            st.metric("Stat Balance Bonus", stat_bonus)
        with col3:
            st.metric("Type Coverage", round(type_score, 2))
        with col4:
            st.metric("Total", round(total, 2))