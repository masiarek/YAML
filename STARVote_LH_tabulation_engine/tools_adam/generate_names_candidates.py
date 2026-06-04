import argparse
import string
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# A-Z list of ice cream and dessert flavors
ICE_CREAM_FLAVORS = [
    "Amaretto",
    "Apple Pie",
    "Almond",
    "Butter Pecan",
    "Black Cherry",
    "Banana",
    "Chocolate",
    "Caramel",
    "Cookie Dough",
    "Dulce de Leche",
    "Dark Chocolate",
    "Espresso",
    "Eggnog",
    "French Vanilla",
    "Fudge",
    "Green Tea",
    "Gelato",
    "Hazelnut",
    "Honeycomb",
    "Irish Cream",
    "Ice Milk",
    "Jamoca",
    "Jelly Bean",
    "Key Lime",
    "Kiwi",
    "Lemon",
    "Lavender",
    "Mint Chocolate Chip",
    "Mango",
    "Neapolitan",
    "Nutella",
    "Oreo",
    "Orange Sherbet",
    "Pistachio",
    "Peanut Butter",
    "Quince",
    "Quark",
    "Rocky Road",
    "Raspberry",
    "Strawberry",
    "Salted Caramel",
    "Tiramisu",
    "Toffee",
    "Ube",
    "Vanilla",
    "Vanilla Bean",
    "Walnut",
    "Watermelon",
    "Xocolatl",
    "Yuzu",
    "Yogurt",
    "Zabaglione",
]

# Random election names for people
ELECTION_NAMES = [
    "Annual General Election",
    "Special Spring Primary",
    "Board of Directors Assembly",
    "Student Government Association Vote",
    "Municipal By-Election",
    "Neighborhood Council Selection",
    "Global Steering Committee Poll",
    "Midterm Leadership Vote",
    "Corporate Governance Election",
    "Community Choice Showdown",
]

# Random offices or positions for people
OFFICES = [
    "President",
    "Vice President",
    "Secretary",
    "Treasurer",
    "Executive Director",
    "Chairperson",
    "Lead Representative",
    "Operations Director",
    "Sergeant-at-Arms",
]

# Random election names for ice cream
ICECREAM_ELECTION_NAMES = [
    "Pick Favorite Ice Cream in Year 2026",
    "Summer Scoop Selection 2026",
    "Annual Dessert Showdown 2026",
    "Supreme Gelato Gala 2026",
    "The Great Flavor Vote 2026",
    "National Ice Cream Day Primary 2026",
    "Frozen Treat Championship 2026",
]

# Random offices or positions for ice cream
ICECREAM_OFFICES = [
    "Flavor of the Year",
    "Chief Scoop Officer",
    "Best in Cone",
    "Ultimate Sundae Topping",
    "Grand Champion Flavor",
    "President of Desserts",
]


def generate_alphabetical_candidates(num_candidates, theme="names"):
    """Generates a list of fake candidate names, progressing through the alphabet."""
    candidates = []
    alphabet = string.ascii_uppercase

    for i in range(num_candidates):
        letter = alphabet[i % 26]

        if theme == "icecream":
            # Filter flavors that start with the target letter and pick one
            valid_flavors = [
                f for f in ICE_CREAM_FLAVORS if f.upper().startswith(letter)
            ]
            flavor = (
                random.choice(valid_flavors)
                if valid_flavors
                else f"{letter} - Unknown Flavor"
            )
            candidates.append(f"{letter} - {flavor}")
        else:
            # Generate a first name starting with the target letter
            first_name = ""
            while not first_name.upper().startswith(letter):
                first_name = fake.first_name()

            # Generate a last name starting with the target letter
            last_name = ""
            while not last_name.upper().startswith(letter):
                last_name = fake.last_name()

            candidates.append(f"{letter} - {first_name} {last_name}")

    return candidates


if __name__ == "__main__":
    # Set up command-line arguments
    parser = argparse.ArgumentParser(
        description="Generate alphabetically prefixed fake candidate names or flavors, with randomized election metadata."
    )
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        default=5,
        help="Number of candidates to generate (default: 16)",
    )
    parser.add_argument(
        "-t",
        "--theme",
        type=str,
        choices=["names", "icecream", "random"],
        default="random",
        help="Theme for the generated candidates (default: random)",
    )
    args = parser.parse_args()

    # Determine the actual theme if 'random' is selected
    actual_theme = (
        random.choice(["names", "icecream"]) if args.theme == "random" else args.theme
    )

    # Randomize the election metadata based on the actual theme
    if actual_theme == "icecream":
        random_election = random.choice(ICECREAM_ELECTION_NAMES)
        random_office = random.choice(ICECREAM_OFFICES)
    else:
        random_election = random.choice(ELECTION_NAMES)
        random_office = random.choice(OFFICES)

    # Generate the candidates
    results = generate_alphabetical_candidates(args.num, theme=actual_theme)

    # Print the output
    print("========================================")
    print(f" Election: {random_election}")
    print(f" Position: {random_office}")
    print("========================================")
    print(f"--- Generating {args.num} Candidates ({actual_theme}) ---")

    for candidate in results:
        print(candidate)