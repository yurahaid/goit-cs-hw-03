from pymongo import MongoClient
from faker import Faker
from bson import ObjectId

# Connecting to MongoDB
client = MongoClient("mongodb://localhost:27017/", username='mongo_user', password='password')
db = client['cat_database']
collection = db['cats']

fake = Faker('en_US')


def generate_and_insert_cats(n):
    """Generate and insert several cat documents using Faker."""
    cats = []
    for _ in range(n):
        cat = {
            "_id": ObjectId(),
            "name": fake.first_name().lower(),
            "age": fake.random_int(min=1, max=15),
            "features": [fake.sentence(nb_words=2).replace('.', ''), fake.sentence(nb_words=3).replace('.', ''),
                         fake.word()]
        }
        cats.append(cat)

    try:
        collection.insert_many(cats)
        print(f"{n} cat(s) successfully inserted.")
    except Exception as e:
        print(f"Error while inserting records: {e}")


def read_all_cats():
    """Print all records from the collection."""
    try:
        return collection.find()
    except Exception as e:
        print(f"Error while reading records: {e}")


def read_cat_by_name(name):
    """Print cat information by name."""
    try:
        return collection.find_one({"name": name})
    except Exception as e:
        print(f"Error while reading record: {e}")


def update_cat_age(name, new_age):
    """Update cat age by name."""
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count:
            print("Cat age successfully updated.")
        else:
            print("Cat with this name not found.")
    except Exception as e:
        print(f"Error while updating record: {e}")


def add_cat_feature(name, new_feature):
    """Add a new feature to the cat's features list by name."""
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.modified_count:
            print("Feature successfully added.")
        else:
            print("Cat with this name not found.")
    except Exception as e:
        print(f"Error while updating record: {e}")


def delete_cat_by_name(name):
    """Delete a record from the collection by animal's name."""
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print("Record successfully deleted.")
        else:
            print("Cat with this name not found.")
    except Exception as e:
        print(f"Error while deleting record: {e}")


def delete_all_cats():
    """Delete all records from the collection."""
    try:
        collection.delete_many({})
        print("All records successfully deleted.")
    except Exception as e:
        print(f"Error while deleting records: {e}")


from termcolor import colored


def print_cat(cat):
    print("-" * 40)
    print(colored(f"ID: {cat['_id']}", "cyan"))
    print(colored(f"Name: {cat['name']}", "cyan"))
    print(colored(f"Age: {cat['age']}", "cyan"))
    print(colored(f"Features: {', '.join(cat['features'])}", "cyan"))
    print("-" * 40)


def print_table(cats):
    if cats:
        print(f"{'ID':<24} {'Name':<10} {'Age':<3} {'Features'}")
        print("-" * 60)
        for cat in cats:
            print(f"{str(cat['_id']):<24} {cat['name']:<10} {cat['age']:<3} {', '.join(cat['features'])}")
    else:
        print(colored("No cats found in the database.", "red"))


if __name__ == "__main__":
    while True:
        print(colored("Choose an option:", "blue"))
        print(colored("generate: Generate and insert cats", "green"))
        print(colored("read-all: Read all cats", "green"))
        print(colored("read: Read cat by name", "green"))
        print(colored("update: Update cat age", "green"))
        print(colored("add-feature: Add cat feature", "green"))
        print(colored("delete: Delete cat by name", "green"))
        print(colored("delete-all: Delete all cats", "green"))
        print(colored("exit: Exit", "red"))

        choice = input(colored("Enter your choice: ", "yellow")).strip().lower()

        if choice == 'generate':
            n = int(input(colored("Enter number of cats to generate and insert: ", "yellow")))
            generate_and_insert_cats(n)
        elif choice == 'read-all':
            cats = read_all_cats()
            print_table(cats)
        elif choice == 'read':
            name = input(colored("Enter the name of the cat: ", "yellow"))
            cat = read_cat_by_name(name)
            if cat:
                print_cat(cat)
            else:
                print(colored("Cat not found.", "red"))
        elif choice == 'update':
            name = input(colored("Enter the name of the cat: ", "yellow"))
            new_age = int(input(colored("Enter the new age of the cat: ", "yellow")))
            update_cat_age(name, new_age)
        elif choice == 'add-feature':
            name = input(colored("Enter the name of the cat: ", "yellow"))
            new_feature = input(colored("Enter the new feature to add: ", "yellow"))
            add_cat_feature(name, new_feature)
        elif choice == 'delete':
            name = input(colored("Enter the name of the cat: ", "yellow"))
            delete_cat_by_name(name)
        elif choice == 'delete-all':
            delete_all_cats()
        elif choice == 'exit':
            print(colored("Exiting the program.", "red"))
            break
        else:
            print(colored("Invalid choice. Please choose a valid option.", "red"))
