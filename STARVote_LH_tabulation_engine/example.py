import starvote

ballots = [
    {'Andre': 5, 'Blake': 0, 'Carmen': 4, 'David': 4, 'Erin': 1},

]

winners = starvote.election(starvote.star, ballots, verbosity=1)
