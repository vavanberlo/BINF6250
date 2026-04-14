import csv
import random
from pprint import pprint
import statistics
import os
import json


def fetch_stats(filename, pokedex):
    '''Adds stats information to Pokedex.
    Params: filename (str) - name of csv file to read
            pokedex (dict): Pokedex
    Return: none
    '''
    count = 0
    with open(filename, mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
        #print(csv_reader.fieldnames)  
        
        for row in csv_reader:
            name = row['pokemon_name']
            count += 1
            pokedex[name] = {
                "dex":              int(row['pokedex_number']),
                "type1":            row['type_1'],
                "type2":            row['type_2'],
                "hp":               int(row['hit_points']),
                "attack":           int(row['attack']),
                "defense":          int(row['defense']),
                "special_attack":   int(row['special_attack']),   
                "special_defense":  int(row['special_defense']),  
                "speed":            int(row['speed']),
                "can_evolve":       to_bool(row['can_evolve']), # might include megas or something
                "evolves_from":     row['evolves_from'], # used for calculating popularity
                "final_evolution":  to_bool(row['final_evolution']), # We want these
                "mega_evolution":   to_bool(row['mega_evolution']), # filter these out
                "mythical":         to_bool(row['mythical']), # filter these out
                "is_default":       to_bool(row['is_default']), # filter out battle forms
                "legendary":        to_bool(row['legendary']),
                "normal_dmg":       float(row['against_normal']),
                "fire_dmg":         float(row['against_fire']),
                "water_dmg":        float(row['against_water']),
                "electric_dmg":     float(row['against_electric']),
                "grass_dmg":        float(row['against_grass']),
                "ice_dmg":          float(row['against_ice']),
                "fight_dmg":        float(row['against_fighting']),
                "poison_dmg":       float(row['against_poison']),
                "ground_dmg":       float(row['against_ground']),
                "flying_dmg":       float(row['against_flying']),
                "psychic_dmg":      float(row['against_psychic']),
                "bug_dmg":          float(row['against_bug']),
                "rock_dmg":         float(row['against_rock']),
                "ghost_dmg":        float(row['against_ghost']),
                "dragon_dmg":       float(row['against_dragon']),
                "dark_dmg":         float(row['against_dark']), 
                "steel_dmg":        float(row['against_steel']), 
                "fairy_dmg":        float(row['against_fairy']),
                "generation":       int(row['generation']), # for user selection
            }
            
    print(f"Read in {count} pokemon's stats")


def to_bool(value):
    '''Fixes non-boolean values when reading in files'''
    return value.strip().lower() == 'true'

    
def fetch_pop(filename, pokedex):
    '''Adds popularity information to Pokedex. There are more Pokemon in this file than we need so we will only update the Pokemon existing in our Pokedex.
    Note that 0 is not popular at all. Higher numbers indicate very popular Pokemon.
    Params: filename (str) - name of csv file to read
    pokedex (dict): Pokedex
    Return: none'''
    with open(filename, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
        #print(csv_reader.fieldnames)  

        count = 0
        for row in csv_reader:
            name = row['Name']
            name = name.replace('♀', 'F').replace('♂', 'M')  # Fix for Nidorans
            name = name.replace('Victreebell', 'Victreebel') # Fix for two other Pokemon who were misnamed in file
            name = name.replace('Primape', 'Primeape') 
            if name in pokedex:
                pokedex[name].update({"pop_rank": int(row["Weighted Total"])})
                count += 1
    print(f"Read in {count} pokemon's popularities")


def build_json(filename, pokedex):
    ''' Build json file of pokedex dictionary
    Params: filename (str): json file
            pokedex (dict): Pokedex
    Return: filename (str): name of file wrote to
    '''
    with open(filename, "w") as json_file:
        json.dump(pokedex, json_file, indent=4)
    
    return filename


def load_json(filename):
    ''' Load json file containing pokedex dictionary
    Params: filename (str): json file
    Return: pokedex (dict): Pokedex
    '''
    with open(filename , "r") as json_file:
        pokedex = json.load(json_file)

    return pokedex


def build_pokedex(force_rebuild=False):
    '''If pokedex.json not already built, build it. Otherwise, load it into our program.
    Params: force_rebuild (bool): If true, force rebuild of json file, for testing purposes
    Return: pokedex (dict): Pokedex'''

    # File locations
    #stats_file = "./data/Complete Pokedex V1.1.csv"
    #pop_file = "./data/Pokemon Survey Results - Sheet.csv"
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    stats_file = os.path.join(base_dir, "data", "Complete Pokedex V1.1.csv")
    pop_file = os.path.join(base_dir, "data", "Pokemon Survey Results - Sheet.csv")
    json_file = os.path.join(base_dir, "pokedex.json")
    
    if os.path.exists(json_file) and not force_rebuild:
        pokedex = load_json(json_file)
        print("Loaded pokedex.json")
        print(f"{len(pokedex)} Pokemon loaded")
    else:
        pokedex = {}
        fetch_stats(stats_file, pokedex)
        fetch_pop(pop_file, pokedex)
        build_json(json_file, pokedex)
        print("Built pokedex from data files")
    return pokedex


def filter_by_gen(gens, pokedex):
    ''' Function to filter the pokedex by generation chosen by the user
    Params: gens (list): generation(s) to include
            pokedex (dict): Pokedex
    Return: filtered_dex (dict): Filtered Pokedex
    '''
    return {name: data for name, data in pokedex.items() 
        if data['generation'] in gens}


def print_poke(name, pokedex):
    '''Prints one Pokemon's information
    Params: name (str) : Pokemon name to access
            pokedex (dict) : whole pokedex
    Return: none
    '''
    print(name)
    for key, value in pokedex[name].items():
        print(f"{key} : {value}")


def choose_poke(team, pokedex):
    '''Chooses a pokemon
    Params: team (list): names of pokemon that are already in the team
            pokedex (dict): pokedex
    Return: choice (string): name of pokemon to add to the team
    '''
    poke = False
    while poke == False:
        try_poke = random.choice(list(pokedex.keys()))
        #print(f'Trying {try_poke}')

        # Do not choose duplicate team members
        if try_poke in team:
            #print(f'{try_poke} is already in team')
            pass            
        # Do not choose unevolved pokemon
        elif not pokedex[try_poke]["final_evolution"]:
            pass
        # Do not choose mythical - usually only available in timed events
        elif pokedex[try_poke]["mythical"]:
            pass
        # Do not choose mega evolutions - these are only accessible during battle
        elif pokedex[try_poke]["mega_evolution"]:
            pass
        # Do not choose battle forms
        elif not pokedex[try_poke]["is_default"]:
            pass
        else:
            poke = try_poke
            #print(f'{poke} is good!')
            
    return poke


def score_pop(name, pokedex):
    '''score one pokemon's popularity
    Params: name (string): dictionary subset only containing that pokemon's stats
            pokedex (dict): pokedex
    Return: score (float): score for popularity metric'''

    # Population bin weights, these may change
    popular = -0.5
    uncommon = 0.5
    unloved = 1
    legendary = -0.5

    # Account for pre-evolution popularity
    cum_score = pokedex[name].get("pop_rank", 0)
    #print(f"Pokemon: {name}, score: {cum_score}")
    pre_evo = pokedex[name]["evolves_from"]

    while pre_evo and pre_evo in pokedex:
        cum_score += pokedex[pre_evo].get("pop_rank", 0)
        #print(f"Pre-evo: {pre_evo}, score: {cum_score}")
        pre_evo = pokedex[pre_evo]["evolves_from"]
        
    if cum_score < 50:
        score = unloved
    elif cum_score < 100:
        score = uncommon
    else:
        score = popular
    # an unpopular legendary should get a chance to be picked
    if pokedex[name]["legendary"] == True:
        score = max(score, legendary)
    #print(f'Scored {name} at {score}')
    
    return(float(score))


def score_team_types(team, pokedex):
    '''All 6 pokemon will be scored as a team on type distribution
    Params: team (list): names of pokemon in the team
            pokedex (dict): pokedex 
    Return: score (int): type coverage score'''

    type_counts = {}
    for poke in team:
        # count number of times each type appears
        type1 = pokedex[poke]["type1"]
        type2 = pokedex[poke]["type2"]

        for poke_type in [type1, type2]:
            if poke_type:
                type_counts[poke_type] = type_counts.get(poke_type, 0) + 1

    #pprint(type_counts)
    # score distribution
    # Weights
    first = 1
    second = 0.5
    more = -1

    type_score = 0
    for types, count in type_counts.items():
        #print(f'{types} : {count}')
        if count == 1:
            type_score += first
        elif count == 2:
            type_score += second
        else:
            type_score += more
    #print(f'Team type coverage score is {type_score}')
    return type_score


def score_team_stats(team, pokedex):
    '''All 6 pokemon will be scored on their team stat distribution
    Params: team (list) : names of pokemon in the team
            pokedex (dict): Pokedex
    Return: score (double): stat distribution score
    '''

    # dictionary of stat totals for ease of access
    stat_totals = {}
    stats = ["hp", "attack", "defense", "special_attack", "special_defense", "speed"]

    for stat in stats:
        stat_totals[stat] = sum((pokedex[poke][stat]) for poke in team)
    #pprint(stat_totals)
    # In general, the stdev will be between 0-100. Lower score = lower deviation = more balanced team
    stdev = statistics.stdev(list(stat_totals.values()))
    
    return stdev


def score_team(team, pokedex):
    '''All 6 pokemon will be scored as a team based on all 3 metrics.
    Calls score_pop(), score_team_stats(), and score_team_types()
    Params: team (list) : names of pokemon in the team
            pokedex (dict): Pokedex
    Return: team_pop (double): team popularity score
            stat_bonus (double): team stat distribution bonus
            type_score (double): team type distribution score
    '''
    
    # Score popularity
    team_pop = 0
    for poke in team:
        team_pop += score_pop(poke, pokedex)
    #print(f'Team popularity is {team_pop}')
    
    # Score stat distribution
    stat_score = score_team_stats(team, pokedex)
    #print(f'Team stat distribution stdev is {stat_score}')
    if stat_score < 50:
        #print(f'Giving bonus of 2 to well-distributed team stats.')
        stat_bonus = int(2)
    else:
        #print(f'No bonus for stat distribution.')
        stat_bonus = int(0)
    
    # Score type coverage
    type_score = score_team_types(team, pokedex)
    #print(f'Team type score is {type_score}')

    #return team_pop, stat_bonus, type_score
    return team_pop, stat_bonus, type_score


def build_team(pokedex):
    '''
    Build team
    Params: pokedex (dict): Pokedex
    Return: team (list): Pokemon chosen for the team
            total (float): team score
    '''

    # Build first team
    team = []
    total = 0
    for i in range(6):
        team.append(choose_poke(team, pokedex))
    #print("We generated this team to start:")
    #print(team)
    
    total = sum(score_team(team, pokedex))
    #print(f"Team score: {total}")
            
    return team, total


def swap_teammate(team, pokedex, to_swap = None):
    ''' Swap one team mate
    Params: team (list): Pokemon already on the team
            pokedex (dict): Pokedex
            to_swap (int): Index of pokemon on team to be swapped.
                If not supplied, random number will be generated (below).
    Return: new_team (list): Updated team
    '''

    if to_swap is None:
        to_swap = random.randint(0, 5)
    
    #print(f"Swapping index {to_swap}: {team[to_swap]}")

    new_poke = choose_poke(team, pokedex)
    #print(f"We chose {new_poke} to add in.")

    new_team = team.copy()
    new_team[to_swap] = new_poke
    #print(f"New team: {new_team}")

    return new_team


def sampler(curr_team, curr_total, pokedex, to_swap = None):
    ''' Swaps one team mate, rescores, repeat
    Params: curr_team (list): Current team
            curr_total (float): Current team score
            pokedex (dict): Pokedex
            to_swap (int): index of Pokemon we want to swap, this will be passed to swap_teammate()
    Return: new_team (list): New team
            new_total (float): New team score
    '''

    # If we are making a directed swap, we want to force a change even if the score goes down.
    if to_swap is not None:
        curr_team = swap_teammate(curr_team, pokedex, to_swap)
        curr_total = sum(score_team(curr_team, pokedex))
        #print()
        #print(f"We made a directed swap. The new score is {curr_total}")
        #print("The first new team after the directed swap is ")
        #print(curr_team)
    # The program will then continue to swap that slot out as usual.
    
    # We will run until we make x swaps that do not improve the team score.
    x = 0
    while x < 20:
        # Swap in a pokemon
        new_team = swap_teammate(curr_team, pokedex, to_swap)
        # Score the new team
        new_total = sum(score_team(new_team, pokedex))
        #print(f"Generated a new team with score: {new_total}: {new_team}")
        #print(new_team)

        # If the new team is worse, discard
        if new_total <= curr_total:
            #print(f"The new team was not better: {new_total} vs {curr_total}")
            x += 1
            #print(f"We looked at {x} consecutive swaps that did not improve the score.")
        else:
            #print(f"The new team was better: {new_total} vs {curr_total}")
            curr_total = new_total
            curr_team = new_team
            x = 0
            #print(f"Updated team: {curr_team}")
            #print("Resetting score check count")

    #print(f"New team has score: {curr_total}")
    #print(curr_team)

    return curr_team, curr_total
