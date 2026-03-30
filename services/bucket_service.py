from utils.file_handler import load_json, save_json

BUCKET_PATH = "data/buckets.json"
PROFILE_PATH = "data/profile.json"


def create_bucket():
    profile = load_json(PROFILE_PATH)
    buckets = load_json(BUCKET_PATH)

    if not profile:
        print("Please set your income first.")
        return

    print("\nChoose bucket type:")
    print("1. Needs")
    print("2. Wants")
    print("3. Savings")

    choice = input("Enter choice: ")

    if choice == "1":
        bucket_type = "needs"
    elif choice == "2":
        bucket_type = "wants"
    elif choice == "3":
        bucket_type = "savings"
    else:
        print("Invalid choice.")
        return

    name = input("Enter bucket name: ").lower()
    amount = float(input("Enter amount to allocate: "))

    total_allowed = profile["allocations"][bucket_type]
    current_total = sum(buckets[bucket_type].values())

    if current_total + amount > total_allowed:
        print("Allocation exceeds allowed limit.")
        return

    buckets[bucket_type][name] = amount
    save_json(BUCKET_PATH, buckets)

    print(f"{name} bucket created successfully.")


def view_buckets():
    buckets = load_json(BUCKET_PATH)

    print("\n=== Your Buckets ===")

    for bucket_type, items in buckets.items():
        print(f"\n{bucket_type.upper()}:")
        if not items:
            print("  No buckets yet.")
        for name, amount in items.items():
            print(f"  {name}: ${amount}")