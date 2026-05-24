import os
import string
import argparse
import re
from datetime import datetime
from playwright.sync_api import sync_playwright
from faker import Faker

# Initialize Faker
fake = Faker()

STATE_FILE = "auth_state.json"


def generate_alphabetical_candidates(num_candidates):
    candidates = []
    alphabet = string.ascii_uppercase
    for i in range(num_candidates):
        letter = alphabet[i % 26]

        first_name = ""
        while not first_name.upper().startswith(letter):
            first_name = fake.first_name()

        last_name = ""
        while not last_name.upper().startswith(letter):
            last_name = fake.last_name()

        candidates.append(f"{letter} - {first_name} {last_name}")

    return candidates


def automate_voting_wizard(num_candidates):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # 1. Handle Authentication State
        if os.path.exists(STATE_FILE):
            print(f"Loading saved login state from '{STATE_FILE}'...")
            context = browser.new_context(storage_state=STATE_FILE)
        else:
            print("No saved login state found. Starting fresh...")
            context = browser.new_context()

        page = context.new_page()

        print("Navigating to BetterVoting wizard...")
        page.goto("https://bettervoting.com/#wizard")

        if not os.path.exists(STATE_FILE):
            print("\n🛑 ACTION REQUIRED: MANUAL LOGIN 🛑\nPlease log in within 60s...")
            page.wait_for_timeout(60000)
            context.storage_state(path=STATE_FILE)
            print("✅ Login state saved!")

        print(f"\nStarting automation sequence ({num_candidates} candidates)...")

        print("Selecting 'Election'...")
        page.get_by_label("Election", exact=True).check(force=True)

        print("Selecting 'Just one'...")
        page.get_by_label("Just one", exact=True).check(force=True)

        # Step 3: Title
        compact_time = datetime.now().strftime("%m/%d %H:%M")
        test_title = f"Test - {compact_time}"
        print(f"Entering title: {test_title}")
        title_field = page.get_by_label("Elected Office Title")
        title_field.focus()
        title_field.press_sequentially(test_title, delay=10)
        title_field.blur()

        # Step 3.5: Enter Description
        print("Entering Description...")
        try:
            desc_field = page.locator("textarea").first
            desc_field.wait_for(state="visible", timeout=3000)
            desc_field.focus()
            desc_field.press_sequentially(
                "BVSchema Test Library - create JSON and StrictYAML test files automatically",
                delay=10,
            )
            desc_field.blur()
        except Exception as e:
            print(f"Warning: Could not locate Description box. Details: {e}")

            # Step 4: Voting Method
            print("Locating 'Voting Method' section...")
            star_label = page.locator("label").filter(has_text="STAR Voting").first

            # Helper to scroll and clear sticky header
            def scroll_into_view_with_offset(locator, offset=100):
                # Scroll the element into view
                locator.scroll_into_view_if_needed()
                # Adjust the window scroll Y position to account for sticky header
                page.evaluate(f"window.scrollBy(0, -{offset})")

            if not star_label.is_visible():
                print("Expanding 'Voting Method' accordion...")
                accordion_header = page.get_by_text(
                    re.compile(r"^Voting Method$", re.IGNORECASE)
                ).first
                scroll_into_view_with_offset(accordion_header)
                accordion_header.click()
                page.wait_for_timeout(1000)

            single_winner_label = (
                page.locator("label").filter(has_text="Single-Winner").first
            )
            if single_winner_label.is_visible():
                print("Selecting 'Single-Winner'...")
                scroll_into_view_with_offset(single_winner_label)
                if not single_winner_label.locator("input[type='radio']").is_checked():
                    single_winner_label.click()
                page.wait_for_timeout(300)

            print("Selecting 'STAR Voting'...")
            scroll_into_view_with_offset(star_label)
            if not star_label.locator("input[type='radio']").is_checked():
                star_label.click()
            page.wait_for_timeout(500)

        # Step 7: Candidates Accordion
        print("Locating 'Candidates' section...")

        # Helper function to count visible textboxes on screen
        def count_visible_textboxes():
            return len([b for b in page.get_by_role("textbox").all() if b.is_visible()])

        if count_visible_textboxes() <= 2:
            print("Candidates accordion is closed. Expanding it now...")
            page.get_by_text(re.compile(r"^Candidates$", re.IGNORECASE)).first.click(
                force=True
            )
            page.wait_for_timeout(1000)
        else:
            print("Candidates accordion is already open.")

        # Step 8: Enter Candidates
        selected_candidates = generate_alphabetical_candidates(num_candidates)
        print("\n=== SELECTED CANDIDATES ===")

        for i, candidate in enumerate(selected_candidates, 1):
            print(f"Entering Candidate {i}: {candidate}")

            target_field = None
            all_textboxes = page.get_by_role("textbox").all()

            for box in all_textboxes:
                if not box.is_visible() or box.get_attribute("id") == "contact_email":
                    continue

                if box.input_value().strip() == "":
                    target_field = box
                    break

            if target_field:
                target_field.focus()
                target_field.press_sequentially(candidate, delay=10)
                target_field.press("Tab")
                page.wait_for_timeout(300)
            else:
                print(
                    f"Error: Could not locate an empty candidate field for {candidate}!"
                )

        print("===========================\n")

        # Click the page background to ensure absolutely all final React states are saved
        page.locator("body").click()
        page.wait_for_timeout(500)

        # Step 9: Click NEXT
        print("Clicking 'NEXT'...")
        try:
            next_button = page.get_by_role(
                "button", name=re.compile(r"^next$", re.IGNORECASE)
            ).first
            next_button.wait_for(state="attached", timeout=5000)
            next_button.click(
                force=True
            )  # Force true is safe here to bypass the sticky header overlap
        except Exception:
            next_button = page.get_by_text(re.compile(r"^next$", re.IGNORECASE)).first
            next_button.wait_for(state="attached", timeout=5000)
            next_button.click(force=True)

        # Step 10: Handle the optional "Publish?" Modal
        print("Checking for 'Publish?' modal...")
        page.wait_for_timeout(1500)  # Give the page time to transition or pop the modal

        try:
            see_more_btn = page.get_by_role(
                "button", name=re.compile(r"see more options", re.IGNORECASE)
            ).first
            see_more_btn.wait_for(state="visible", timeout=3000)
            see_more_btn.click()
            print("Successfully clicked 'SEE MORE OPTIONS'.")
        except Exception:
            try:
                see_more_btn = page.get_by_text(
                    re.compile(r"see more options", re.IGNORECASE)
                ).first
                see_more_btn.wait_for(state="visible", timeout=3000)
                see_more_btn.click()
                print("Successfully clicked 'SEE MORE OPTIONS'.")
            except Exception:
                print("Modal bypassed or not present. Proceeding...")

        # Step 11: "Just a few more questions..." Page (Restricted settings)
        print("Waiting for the 'Restricted?' election settings...")

        try:
            no_radio_label = (
                page.locator("label")
                .filter(has_text=re.compile(r"^No$", re.IGNORECASE))
                .first
            )
            no_radio_label.wait_for(state="visible", timeout=10000)
            print("Selecting 'No' (Unrestricted Election)...")
            if not no_radio_label.locator("input[type='radio']").is_checked():
                no_radio_label.click()
        except Exception as e:
            print(f"Warning: Could not select 'No' for Restricted. Details: {e}")

        page.wait_for_timeout(500)

        # Click "CONTINUE"
        print("Clicking 'CONTINUE'...")
        try:
            continue_btn = page.get_by_role(
                "button", name=re.compile(r"continue", re.IGNORECASE)
            ).first
            continue_btn.click()
        except Exception:
            continue_btn = page.get_by_text(
                re.compile(r"continue", re.IGNORECASE)
            ).first
            continue_btn.click()

        # Step 12: Choose Voters (Authentication Method)
        print("Waiting for Voter Authentication options...")
        page.wait_for_timeout(1000)

        try:
            multi_vote_label = (
                page.locator("label")
                .filter(
                    has_text=re.compile(
                        r"Allows? multiple votes per device", re.IGNORECASE
                    )
                )
                .first
            )
            multi_vote_label.wait_for(state="visible", timeout=10000)
            print("Selecting 'Allows multiple votes per device'...")
            if not multi_vote_label.locator("input[type='radio']").is_checked():
                multi_vote_label.click()
            print("Successfully clicked 'Allows multiple votes per device'.")
        except Exception as e:
            print(f"Warning: Could not click multiple votes option. Details: {e}")

        print("\nAutomation complete. Keeping browser open for 15 seconds...")
        page.wait_for_timeout(15000)

        context.close()
        browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", type=int, default=5)
    args = parser.parse_args()
    automate_voting_wizard(args.candidates)
