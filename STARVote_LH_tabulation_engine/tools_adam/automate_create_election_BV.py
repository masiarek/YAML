import os
import string
import argparse
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

def smart_click(page, locator):
    """Executes a pure JS native DOM click to bypass animation and layout issues."""
    locator.wait_for(state="attached", timeout=10000)
    locator.evaluate("el => el.scrollIntoView({block: 'center', inline: 'center'})")
    page.wait_for_timeout(600)
    locator.evaluate("""el => {
        if (el.tagName.toUpperCase() === 'LABEL') {
            const input = el.querySelector('input');
            if (input) { input.click(); return; }
        }
        el.click();
    }""")
    page.wait_for_timeout(300)

def automate_voting_wizard(num_candidates):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = (
            browser.new_context(storage_state=STATE_FILE)
            if os.path.exists(STATE_FILE)
            else browser.new_context()
        )
        page = context.new_page()

        print("Navigating to BetterVoting wizard...")
        page.goto("https://bettervoting.com/#wizard")

        if not os.path.exists(STATE_FILE):
            print("\n🛑 ACTION REQUIRED: MANUAL LOGIN 🛑...")
            page.wait_for_timeout(60000)
            context.storage_state(path=STATE_FILE)

        # Wait for form to exist before modifying DOM
        page.wait_for_selector("text=Which term best describes your situation?")

        # SURGICAL CSS: Only hide the navigation bar that causes the pointer interception
        page.add_style_tag(
            content="""
            header, .MuiAppBar-root {
                display: none !important;
            }
        """
        )

        print(f"\nStarting automation sequence...")

        # Use smart_click for everything
        print("Selecting 'Election'...")
        smart_click(page, page.locator("label").filter(has_text="Election").first)

        print("Selecting 'Just one'...")
        smart_click(page, page.locator("label").filter(has_text="Just one").first)

        # Step 3: Title
        test_title = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Entering title: {test_title}")
        title_field = page.get_by_label("Elected Office Title")
        title_field.focus()
        title_field.press_sequentially(test_title, delay=10)
        title_field.blur()

        # Step 3.5: Description
        print("Entering Description...")
        desc_field = page.locator("textarea").first
        desc_field.focus()
        desc_field.press_sequentially("BVSchema Test Library", delay=10)
        desc_field.blur()

        # Step 4: Voting Method
        print("Selecting Voting Method...")
        sw_label = page.locator("label").filter(has_text="Single-Winner").first
        if not sw_label.is_visible():
            smart_click(page, page.get_by_text("Voting Method").first)
            page.wait_for_timeout(1000)
        smart_click(page, sw_label)
        smart_click(page, page.locator("label").filter(has_text="STAR Voting").first)

        # --- HANDOFF TO MANUAL CONTROL ---
        print("\n⏸️ Automation paused. The script has handed control to you.")
        print("You can now enter candidates and finish the setup in the browser.")
        input("Press ENTER in this console when you are finished to close the browser...")

        print("\nClosing browser...")
        context.close()
        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", type=int, default=5)
    args = parser.parse_args()
    automate_voting_wizard(args.candidates)