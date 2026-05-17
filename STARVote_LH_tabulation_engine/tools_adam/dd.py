import random
import string


def find_n_winner_scenario_STAR_voting(num_voters, num_candidates, num_to_find=10, score_weights={0: 0.8, 1: 0.02, 2: 0.02, 3: 0.02, 4: 0.02, 5: 0.12}, find_flipped=False):
   """
   Find random set of instances (sets of ballots) where the winner of the STAR voting scoring round (first round)
   is either the same as or different from the winner of the automatic runoff (second round),
   and ensures no tie in the runoff between top two winners.


   Allows control over the probability of each score occurring in the ballots.


   Args:
       num_voters: The number of voters in the election.
       num_candidates: The number of candidates in the election.
       num_to_find: The number of such instances to find.
       score_weights: A dictionary where keys are possible scores and values are their probabilities.
                      The probabilities should sum to 1.
       find_flipped: A boolean. If True, finds scenarios where the winner FLIPS in the runoff.
                     If False (default), finds scenarios where the winner is CONSISTENT.
   """
   if find_flipped:
       print("Searching for scenarios where the winner FLIPS in the runoff.")
   else:
       print("Searching for scenarios where the winner is CONSISTENT across rounds.")
   print(find_n_winner_scenario_STAR_voting.__doc__.split('\n')[1].strip())
   print(find_n_winner_scenario_STAR_voting.__doc__.split('\n')[2].strip())
   print(find_n_winner_scenario_STAR_voting.__doc__.split('\n')[3].strip())
   print(find_n_winner_scenario_STAR_voting.__doc__.split('\n')[4].strip())
   print() # Add an empty line for separation


   found_scenarios = []
   candidate_names = list(string.ascii_uppercase[:num_candidates])  # Generate candidate names


   print(f"Searching for {num_to_find} scenarios with {num_voters} ballots and {num_candidates} candidates "
         f"\n- using weighted scores and excluding all same-score ballots and avoiding runoff ties...")


   possible_scores = list(score_weights.keys())
   probabilities = list(score_weights.values())


   while len(found_scenarios) < num_to_find:
       # Generate random ballots for each voter, ensuring no all same-score ballots
       votes = []
       for _ in range(num_voters):
           ballot = random.choices(possible_scores, weights=probabilities, k=num_candidates)
           while all(s == ballot[0] for s in ballot):  # Regenerate if all scores are the same
               ballot = random.choices(possible_scores, weights=probabilities, k=num_candidates)
           votes.append(ballot)


       # Calculate total scores for each candidate
       scores = {}
       for i, candidate in enumerate(candidate_names):
           scores[candidate] = sum(vote[i] for vote in votes)


       sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)


       # Check if all scoring round totals are different to ensure a clear top two
       if len(set(scores.values())) >= 2:
           top_two = [sorted_scores[0][0], sorted_scores[1][0]]
           scoring_round_winner = sorted_scores[0][0]


           def pairwise_comparison(c1, c2):
               wins1 = 0
               wins2 = 0
               for vote in votes:
                   if vote[candidate_names.index(c1)] > vote[candidate_names.index(c2)]:
                       wins1 += 1
                   elif vote[candidate_names.index(c1)] < vote[candidate_names.index(c2)]:
                       wins2 += 1
               return wins1, wins2


           wins1, wins2 = pairwise_comparison(top_two[0], top_two[1])


           if wins1 > wins2:
               runoff_winner = top_two[0]
           elif wins2 > wins1:
               runoff_winner = top_two[1]
           else:
               runoff_winner = "Tie"


           scenario_found = False
           if find_flipped and scoring_round_winner != runoff_winner and runoff_winner != "Tie":
               scenario_found = True
           elif not find_flipped and scoring_round_winner == runoff_winner and runoff_winner != "Tie":
               scenario_found = True


           if scenario_found:
               print("Votes:")
               found_scenarios.append(votes)
               print(", ".join(candidate_names))  # Print the header row
               for vote in votes:
                   print(", ".join(map(str, vote)))
               print("Scoring Round: ", ", ".join(f"{k} = {v}" for k, v in scores.items()), f" (Top-scoring: {scoring_round_winner})")
               print("Top Two: ", ", ".join(f"{k} = {v}" for k, v in dict(sorted_scores[:2]).items()))
               print(f"Runoff Winner: {runoff_winner}")
               print("-" * 20)


   print(f"\nFound a total of {len(found_scenarios)} matching scenarios.")




if __name__ == "__main__":
   num_voters = 5  # number of voters
   num_candidates = 3  # Set the number of candidates - columns
   num_to_find = 2  # how many examples with ballots (instances) to print out
   score_weights = {0: 0.6, 1: 0.05, 2: 0.05, 3: 0.05, 4: 0.05, 5: 0.2}


   find_n_winner_scenario_STAR_voting(num_voters, num_candidates, num_to_find, score_weights, find_flipped=True)


