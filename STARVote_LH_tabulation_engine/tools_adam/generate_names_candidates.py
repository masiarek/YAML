"""
generate_names_candidates.py

Generate a complete, ready-to-run STAR election YAML with a random (and
deliberately silly) theme: 3-8 candidates and 3-10 ballots of random scores.

Examples:
    python generate_names_candidates.py                  # random everything
    python generate_names_candidates.py -t foods         # pick a theme
    python generate_names_candidates.py -n 5 -b 7        # 5 candidates, 7 ballots
    python generate_names_candidates.py -o myvote.yaml    # write to a file
    python generate_names_candidates.py --seats 2         # multi-winner (Bloc)

By default the YAML is printed AND written into ../elections_illustrations/ with a
generated filename. Use --no-write to only print.
"""

import argparse
import datetime
import random
import secrets
from pathlib import Path

try:
    from faker import Faker

    _fake = Faker()
except ImportError:  # faker is optional; only the "people" theme needs it
    _fake = None

MAX_SCORE = 5

# Each theme: whimsical election titles, positions, and a pool of choices.
THEMES = {
    "colors": {
        "elections": [
            "The Great Color Referendum",
            "Hue of the Year 2026",
            "Official Crayon Convention",
        ],
        "positions": ["Color of the Year", "Supreme Shade", "Most Vibrant Vibe"],
        "items": [
            "Crimson",
            "Teal",
            "Goldenrod",
            "Indigo",
            "Coral",
            "Olive",
            "Magenta",
            "Slate",
            "Amber",
            "Periwinkle",
            "Chartreuse",
            "Maroon",
            "Turquoise",
            "Lavender",
        ],
    },
    "foods": {
        "elections": [
            "World Street-Food Championship",
            "The Ultimate Lunch Ballot",
            "Midnight Snack Primary",
        ],
        "positions": ["Best Bite", "Snack Supreme", "People's Plate"],
        "items": [
            "Tacos",
            "Sushi",
            "Ramen",
            "Pizza",
            "Falafel",
            "Dumplings",
            "Burritos",
            "Pho",
            "Curry",
            "Waffles",
            "Gnocchi",
            "Empanadas",
            "Pierogi",
            "Shawarma",
        ],
    },
    "icecream": {
        "elections": [
            "The Great Flavor Vote 2026",
            "Summer Scoop Selection",
            "Frozen Treat Championship",
        ],
        "positions": ["Flavor of the Year", "Chief Scoop Officer", "Best in Cone"],
        "items": [
            "Vanilla",
            "Chocolate",
            "Pistachio",
            "Mango",
            "Stracciatella",
            "Matcha",
            "Salted Caramel",
            "Mint Chip",
            "Rocky Road",
            "Ube",
            "Hazelnut",
            "Black Cherry",
            "Lemon",
            "Tiramisu",
        ],
    },
    "animals": {
        "elections": [
            "Cutest Critter Caucus",
            "Animal Kingdom Assembly",
            "Spirit Animal Selection",
        ],
        "positions": ["Mascot of the Year", "Chief Critter", "Top Beast"],
        "items": [
            "Red Panda",
            "Octopus",
            "Narwhal",
            "Axolotl",
            "Capybara",
            "Pangolin",
            "Quokka",
            "Otter",
            "Sloth",
            "Platypus",
            "Lemur",
            "Hedgehog",
            "Wombat",
            "Fennec Fox",
        ],
    },
    "mythical": {
        "elections": [
            "Council of Legendary Beasts",
            "The Mythical Mandate",
            "Fantasy Realm Election",
        ],
        "positions": ["Guardian of the Realm", "Beast Supreme", "Legend of Legends"],
        "items": [
            "Dragon",
            "Griffin",
            "Phoenix",
            "Kraken",
            "Unicorn",
            "Basilisk",
            "Chimera",
            "Hydra",
            "Pegasus",
            "Minotaur",
            "Sphinx",
            "Wyvern",
            "Cyclops",
            "Banshee",
        ],
    },
    "space": {
        "elections": [
            "Galactic Capital Referendum",
            "Solar System Showdown",
            "Cosmic Destination Poll",
        ],
        "positions": [
            "Capital of the Galaxy",
            "Best Place to Colonize",
            "Cosmic Champ",
        ],
        "items": [
            "Mars",
            "Europa",
            "Titan",
            "Andromeda",
            "Pluto",
            "Kepler-186f",
            "Ganymede",
            "Proxima B",
            "Enceladus",
            "Trappist-1e",
            "Ceres",
            "Neptune",
            "Vega",
            "Io",
        ],
    },
    "superpowers": {
        "elections": [
            "Superpower Draft 2026",
            "The Heroic Mandate",
            "Ultimate Ability Election",
        ],
        "positions": ["Most-Wanted Power", "Hero's Choice", "Supreme Ability"],
        "items": [
            "Invisibility",
            "Flight",
            "Telepathy",
            "Time Travel",
            "Super Speed",
            "Teleportation",
            "Shapeshifting",
            "Telekinesis",
            "Healing",
            "Invulnerability",
            "Mind Control",
            "Super Strength",
            "Phasing",
            "Precognition",
        ],
    },
    "people": {  # uses faker if available, else a built-in name list
        "elections": [
            "Annual General Election",
            "Neighborhood Council Selection",
            "Community Choice Showdown",
        ],
        "positions": ["President", "Chairperson", "Lead Representative", "Treasurer"],
        "items": [
            "Amara",
            "Bo",
            "Chen",
            "Diego",
            "Esi",
            "Farah",
            "Gio",
            "Hana",
            "Ivan",
            "Juno",
            "Kira",
            "Liam",
            "Mira",
            "Noa",
        ],
    },
}


def pick_candidates(theme, num):
    """Return `num` unique candidate labels for the theme."""
    if theme == "people" and _fake is not None:
        names = set()
        while len(names) < num:
            names.add(_fake.first_name())
        return list(names)
    pool = THEMES[theme]["items"]
    return random.sample(pool, num)


def build_yaml(theme, candidates, ballots, election, position, seats):
    method = "star" if seats == 1 else "bloc"
    header = "# Election: {}\n# Position: {}\n".format(election, position)
    legend = "".join(f"#   {c}\n" for c in candidates)

    cand_row = ",".join(candidates)
    ballot_lines = "\n".join("  " + ",".join(str(s) for s in row) for row in ballots)

    return (
        f"{header}{legend}"
        f"num_winners: {seats}\n"
        f"voting_method: {method}\n\n"
        "options:\n"
        "  show_matrix: false\n"
        "  show_condorcet: true\n"
        "  show_score_counts: true\n\n"
        "ballots: |-\n"
        f"  {cand_row}\n"
        f"{ballot_lines}\n"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-t", "--theme", choices=list(THEMES) + ["random"], default="random"
    )
    parser.add_argument(
        "-n", "--num", type=int, default=None, help="candidates (default: random 3-8)"
    )
    parser.add_argument(
        "-b", "--ballots", type=int, default=None, help="ballots (default: random 3-10)"
    )
    parser.add_argument(
        "--seats", type=int, default=1, help="winners; >1 runs Bloc STAR"
    )
    parser.add_argument("-o", "--output", default=None, help="output .yaml path")
    parser.add_argument(
        "--no-write", action="store_true", help="print only, don't write a file"
    )
    args = parser.parse_args()

    theme = random.choice(list(THEMES)) if args.theme == "random" else args.theme
    num = args.num if args.num is not None else random.randint(3, 8)
    num = max(3, min(num, len(THEMES[theme]["items"])))  # clamp to pool size
    n_ballots = args.ballots if args.ballots is not None else random.randint(3, 10)
    seats = max(1, args.seats)

    candidates = pick_candidates(theme, num)
    ballots = [
        [random.randint(0, MAX_SCORE) for _ in candidates] for _ in range(n_ballots)
    ]
    election = random.choice(THEMES[theme]["elections"])
    position = random.choice(THEMES[theme]["positions"])

    yaml_text = build_yaml(theme, candidates, ballots, election, position, seats)
    print(yaml_text)

    if not args.no_write:
        if args.output:
            out = Path(args.output)
        else:
            stamp = datetime.datetime.now().strftime("%H%M%S")
            suffix = secrets.token_hex(2)
            out = (
                Path(__file__).resolve().parent.parent
                / "elections_illustrations"
                / f"gen_{theme}_{stamp}_{suffix}.yaml"
            )
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(yaml_text, encoding="utf-8")
        print(f"# wrote: {out}")
