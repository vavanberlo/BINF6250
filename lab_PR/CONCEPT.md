# Concept Plan 

# 1.	Recap of Project (Short) 
•	Summary of:  
•	The research question. 
•	The chosen algorithm and algorithm class. 
•	The type of data you plan to use. 
•	This should be concise enough that a reader can understand the rest of the document without opening PROPOSAL.md. 

I will be building a team generator for the video game series Pokemon. This generator will focus on the generation 1 games to start, with possibility of expansion. This tool will differ from other Pokemon team generators in its focus: teams should be generated to create unique, memorable playthroughs that encourage creativity in developing strategy with the generated Pokemon during the game. Specifically, the tool will focus on creating semi-random teams where Pokemon are weighted by their popularity and individual statistics to promote use of under-utilized team lineups. 

I will be utilizing a randomized algorithm, specifically Gibbs sampling, in order to “randomly” choose Pokemon to add to the team. The team will be scored, and substitutions that increase the team’s “uniqueness” will be swapped in until a suitable team has been generated. 

There are relevant data sets available on Kaggle and elsewhere that I will be utilizing. These datasets about the Pokemon include information I plan on using for the scoring as well as returning information about the chosen team to the user, including Pokemon types, stats, popularity, and other characteristics.  


# 2.	Inputs, Outputs, and Assumptions 
•	Precisely define:  
•	The expected input(s) to your algorithm (including data types and formats). 
•	The expected output(s) (what you return or produce). 
•	State key assumptions (e.g., “All sequences are uppercase A/C/G/T,” “Graph is simple and directed,” “Emission probabilities are normalized”).

I have currently identified two datasets I will require to start: one found on Google Sheets and one on Kaggle. The required information from these datasets will be collected into the Pokemon dictionary objects. These datasets are in csv format. My previous idea for this program would be that the user would download the required datasets and the program should handle input. However, during my research during this section, I have found that pre-generating the Pokedex (dictionary) into a .json data file would be a better strategy. This way, the user will not have to find and download datasets that may or may not exist anymore, or have since been updated. This will require the user only to enter desired options for the program. The initial implementation of this program will start by creating the dictionary from the dataset files, and later will be updated to use the .json data file instead.

The output will be a team lineup and report including stat distribution and type matchup coverage.

The input files should be scrubbed and input data properly generated before the program is complete and so no assumptions of inputs will be made of the user/data.


# 3.	Detailed Pseudocode 
•	Provide pseudocode that:  
•	Has clear function signatures or step headings. 
•	Explicitly describes main loops, conditionals, and data structures. 
•	Handles at least one non-trivial edge case (e.g., empty input, unexpected characters, disconnected graph). 
•	Use code-style formatting (indented blocks, consistent naming) so that another student could implement it in Python or another language. 

The pseudocode for the first section of my program below is for the first iteration of my program. Eventually I will seek to implement the .json input file, which will replace the database input steps.


Get parameters from user from notebook/command line, or GUI
    Generation, etc

Pokemon data to be stored in nested dictionary format (simplified example):
{Pokemon_name: 	{dex#: #},
	{type:Grass},
    ...
	}

Read in data from datasets: fetch_stats():
	For each line in stats dataset: 
		If gen 1: 
Check for/fix name data (eg Nidoran♀)
Fill dictionary with info (type, stats, name, dex number)

For each line in popularity dataset: fetch_pop():
    Check and fix valid inputs (some of the Pokemon names have typos)
    If pokemon already in dictionary:
        Add new popularity weight data in nested dictionary

Eventually: read_json():
    Read in pokemon information from json file to replace above 2 functions at run time.
    
Build one initial team: build_team():
    Sample: choose_poke():
        Randomly choose 6 unique pokemon, excluding unevolved forms
    Score: score_team():
        Calculate team score using score_pop(), score_team_types(), score_team_stats()

Gibbs sample: sampler(): 
    until some threshold (tbd):
        swap_teammate(): 
            chooses a new pokemon to try to swap in
        score_team() for both old and new possible team
        choose which team is better, loop until threshold is met

User-directed swap: 
    After team is generated, user can choose to swap a specific pokemon. 
    Force a swap using optional sampler() parameter to swap only one specific pokemon in team
			

Report Output Goals:
Individuals: Pokemon name, number, type(s)
Team: spider graph of stat distribution, any double weaknesses
	Reroll button for whole team, or individual teammate keeping rest


# 4.	Complexity and Bottlenecks 
•	Analyze the time and space complexity of your algorithm in terms of relevant parameters (e.g., sequence length, number of reads, number of states). 
•	Identify the most expensive parts of the algorithm and discuss:  
•	When performance might become a problem. 
•	Any ideas you have for mitigating performance issues (e.g., pruning, indexing, approximate methods). 

I do not anticipate any large complexity problems with the algorithm. The datasets are relatively small, and each iteration of the program will require a finite number of computations. If multiple generations are added to the pool, it may require more iterations.

# 5.	Validation and Testing Plan 
•	Describe how you plan to test your implementation:  
•	At least one small, hand-crafted example where you know or can reason about the correct answer. 
•	At least one synthetic or real dataset for stress testing. 
•	Explain:  
•	What results you expect on these tests. 
•	What would constitute evidence that the algorithm is behaving incorrectly. 
•	Outline the kinds of automated tests you will implement (e.g., unit tests for subfunctions, end-to-end tests, property/invariant checks). 

I will craft several subsets of the data. These will include sets of artificially created Pokemon that specifically test the weighing algorithm for a single comparison each: popularity, stat distribution, and type matching. If the algorithm isn’t working correctly, I will expect to see many popular Pokemon added to the teams, or wildly uneven stat distributions, or a narrow range of type coverages.

I will also test the algorithm to check for general convergence trends, since I don’t want it to select one “best” team, rather, a diverse set of teams. I plan to do this with one or more metrics including number of times swaps are resulting in improved team scores over time and “quality” of team score over time. The team score should improve, but still provide a varied set of teams across many runs. 

# 6.	Updated Pitfall and Risk Log 
•	Revisit the pitfalls from Part 1:  
•	Which ones still seem relevant? 
•	Which new pitfalls have emerged as you wrote the pseudocode? 
•	For each risk, add a brief note on how your design (or upcoming implementation) will address it. 

There is still the problem of if the program is expanded to include new Pokemon. Using these two datasets, any generation of Pokemon could have a team generated for it by changing the generation desired as a parameter. I have reviewed the databases I intend to use and there are some mismatches in input that will have to be rectified. Increasing the number of inputs would require more scrubbing of typos or non-alphanumeric characters. This will need to be done manually.
Stat weighing might still be a problem. The exact weights for each metric will require fine tuning as I observe the program’s behavior. 

The biggest pitfall I have yet to address is my plan for the user interface. I will attempt to have a GUI, but want to get the bones of the program working before researching how to implement this. Cursory research suggests I may be able to use Streamlit for building a simple GUI so I may try to work with that. It is able to connect and run directly off the GitHub repo so the code can be peer reviewed while being user-friendly.

For the initial conception of this project I was considering adding more output information that would require more databases to be loaded in. This may be feasible still, I will just have to seek the information. As of writing, I did not find suitable readily available databases for things like Pokemon location and would become a much harder task if more generations are added, and it does not add value to the scoring/sampling function which is the main goal of the program. Including a picture of each Pokemon on the team may still be feasible, depending on the final output as text or in a GUI.

# 7.	Generative AI Disclosure (If Used) 
•	If you used generative AI to help with pseudocode or explanations:  
•	Add an appendix titled Generative AI Usage. 
•	Include tool/version, full prompts, how it influenced your pseudocode, and why you chose to use it. 
 
Generative AI (Claude 4.6) was used for brainstorming and validating ideas. No content was taken directly from the AI. 
