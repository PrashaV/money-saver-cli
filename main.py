from services.profile_service import set_income, view_profile
from services.bucket_service import create_bucket, view_buckets


def main():
    while True:
        print("\n=== Money Saving Friend ===")
        print("1. Set Monthly After-Tax Income")
        print("2. View 50/30/20 Allocation")
        print("3. Create Bucket")
        print("4. View Buckets")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            set_income()
        elif choice == "2":
            view_profile()
        elif choice == "3":
            create_bucket()
        elif choice == "4":
            view_buckets()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()