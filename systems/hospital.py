from utils.json_utils import load_json, save_json

PATIENTS_FILE = "data/patients.json"

def hospital_menu(username):

    while True:
        print("\n===================")
        print("Hospital System")
        print("===================")
        print("1. Add Patient")
        print("2. Show Patients")
        print("3. Search Patients")
        print("4. Back")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_patient(username)

        elif choice == "2":
            show_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            break

        else:
            print("Invalid choice. please try again.")


def add_patient(username):
    
    print("\n=== Add Patient ===")

    name = input("Patient name: ").strip()
    age = input("Patient age: ").strip()
    gender = input("Patient gender: ").strip()
    symptoms = input("Symptoms: ").strip()

    if name == "" or age == "" or gender == "" or symptoms == "":
        print("All fields are required.")
        return
    
    patients = load_json(PATIENTS_FILE)

    new_id =len(patients) + 1

    new_patient = {
    "id": new_id,
    "added_by": username,
    "name": name,
    "age": age,
    "gender": gender,
    "symptoms": symptoms
    }

    patients.append(new_patient)
    save_json(PATIENTS_FILE, patients)

    print("Patient added successfully.")


def show_patients():

    print("\n=== Patient List ===")

    patients = load_json(PATIENTS_FILE)

    if len(patients) == 0:
        print("No patients found.")
        return

    for patient in patients:
        print("---------------------------------")
        print(f"ID: {patient['id']}")
        print(f"Name: {patient['name']}")
        print(f"Age: {patient['age']}")
        print(f"Gender: {patient['gender']}")
        print(f"Symptoms: {patient['symptoms']}")
        print(f"Added by: {patient['added_by']}")

def search_patient():


    print("\n=== Search Patient ===")
    
    search_name =  input("Enter  the  patient name: ").strip().lower()

    patients = load_json(PATIENTS_FILE)

    found = False

    for patient in patients:
        if search_name in patient.get("name", "").lower():
            print("------------------------------")
            print(f"ID: {patient['id']}")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Gender: {patient['gender']}")
            print(f"Symptoms: {patient['symptoms']}")
            print(f"Added by: {patient['added_by']}")

            found = True

    if found == False:
        print("No patient found.")