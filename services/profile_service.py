from utils.file_handler import load_json, save_json

PROFILE_PATH = "data/profile.json"


def set_income():
    profile = load_json(PROFILE_PATH)

    name = input("Enter your name: ").strip()
    income = float(input("Enter your monthly after-tax income: "))

    needs = round(income * 0.50, 2)
    wants = round(income * 0.30, 2)
    savings = round(income * 0.20, 2)

    profile = {
        "name": name,
        "monthly_income": income,
        "allocations": {
            "needs": needs,
            "wants": wants,
            "savings": savings
        }
    }

    save_json(PROFILE_PATH, profile)

    print("\nProfile saved successfully.")
    print(f"Needs   (50%): ${needs}")
    print(f"Wants   (30%): ${wants}")
    print(f"Savings (20%): ${savings}")


def view_profile():
    profile = load_json(PROFILE_PATH)

    if not profile:
        print("No profile found. Please set income first.")
        return

    print("\n=== Profile ===")
    print(f"Name: {profile['name']}")
    print(f"Monthly Income: ${profile['monthly_income']}")
    print("Allocations:")
    print(f"  Needs: ${profile['allocations']['needs']}")
    print(f"  Wants: ${profile['allocations']['wants']}")
    print(f"  Savings: ${profile['allocations']['savings']}")