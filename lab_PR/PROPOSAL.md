# Project Title

Pokemon Team Generator


# Research Question

I want to build a tool that generates teams for creating memorable playthroughs of Pokemon that are still varied and viable teams. The tool should create one or more teams that are balanced in stats and type coverage, while weighing against Pokemon that are typically overrepresented in playthroughs such as starter Pokemon, legendaries, and the top popular Pokemon. Initially, it is my goal that the tool will focus on Generation 1 with potential for other gens to be added.

I researched other Pokemon team generator tools available. I found many generators that operated totally randomly. Some generators had options to filter out legendaries and unevolved Pokemon, but no generators had options to weigh by popularity nor for type coverage. 

I have wanted to use a tool like this in the past but it did not exist to my specifications.


# Algorithm and Algorithm Class

This tool will primarily utilize a randomized algorithm, specifically Gibbs Sampling, in order to sample Pokemon to be added to the team, checking for compatibility each time. Instead of simply randomly choosing 6 Pokemon, Gibbs Sampling will allow the tool to continually update the team to create a balanced overall list based on the set criteria.


# Data Plan

I have identified public datasets for Pokemon stats and images that are available on Kaggle under CC0 1.0 Universal or GNU General Public License, version 2. A dataset for popularity is available from a Reddit survey, available through Google Sheets and permission is given for its use in the original Reddit post. If I expand the tool, more public datasets are available on Kaggle.

For training and debugging, I will be starting with a pared down dataset curated to have good coverage of both similar and dissimilar Pokemon by the metrics that the tool will analyze. This will directly translate to the larger dataset of each generation implemented.


# Success Criteria

When the tool finishes a run, I intend it to return the following:
The 6 Pokemon and an image of each Pokemon
Each Pokemon's type, and possibly stats and catch location
Effectivity report: Which types are not represented in the team, types against which the team will not have STAB (Same Attack Type Bonus) coverage.
If data collection option is enabled, data on teams generated should be stored in a file for analysis of overall trends.

I also hope to implement a simple UI for making choices of parameters and desired filters as well as showing results, however, I have not done research in this direction yet.

I will consider the tool a success if it can return sets of teams that meet the criteria set by the weighing system. One way of checking this will be with a report of choices made over many many runs to determine if the algorithm is correctly deprioritizing legendary, starter, unevolved, and popular Pokemon, and not choosing only from a very small pool over time.


# Pitfall Scan

Data Related Issues:

Since the data will be coming from several sources, I will need to be able to read in multiple data formats in order to build the models. If I choose to increase the number of generations represented, new data may be in a different format. 

Algorithmic Issues:

Though this will use Gibbs Sampling, I do not think it will utilize Position Frequency Matrices as we used in the class project. Instead I will need to develop another metric for comparison of team scores

I also suspect that weighing teams by overall stat balance may trend towards choosing indvidual pokemon with evenly balanced stats, rather than choosing Pokemon that complement weaknesses in team mates' stats. I will need to keep an eye on this, and de-prioritize stat weighing if appropriate.

I expect it will take at least as many iterations as Pokemon included in the tool to come to a consensus on a team, which will naturally increase complexity if the tool is upgraded to work for more games/generations. Additionally, there may need to be extra distinction made between generation and specific game, as one generation can have different Pokemon sets depending on the game. 

Evaluation Issues:

There will not be a specific threshold to determine if the function works, and, ideally, no best answer. Therefore I will attempt to use a combination of manual inspection of results using a team score, and stored results from many runs that should reveal biases for or against specific Pokemon, intended or not. 


# Planned Repository Structure (Initial Sketch)

A python notebook will contain the UI features. Python files will contain the required functions. Data files will not be provided but will be used to train the algorithm and scores will be built into the tool.


# Generative AI Disclosure (If Used)

Generative AI was not used in the implementation of this tool.
