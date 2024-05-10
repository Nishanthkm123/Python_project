# Define a class representing a patient
class Patient:
    def __init__(self, name, age, gender, condition):
        # Initialize patient attributes
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition
        self.appointment_time = None  # Initialize appointment time to None
        self.next = None  # Reference to the next patient in the queue

# Define a class representing a hospital queue
class HospitalQueue:
    def __init__(self):
        # Initialize the front and rear of the queue
        self.front = self.rear = None

    def is_empty(self):
        # Check if the queue is empty
        return self.front is None

    def enqueue(self, patient):
        # Add a patient to the queue
        if not isinstance(patient, Patient):
            raise ValueError("Invalid patient object.")

        if len(self.get_queue_list()) < 5:  # Check if the number of patients is less than 5
            if self.is_empty():
                self.front = self.rear = patient
            else:
                self.rear.next = patient
                self.rear = patient
            print(f"{patient.name} has been added to the queue.")
        else:
            print("Queue is full. Cannot add more patients.")

    def dequeue(self):
        # Remove and return the front patient from the queue
        if self.is_empty():
            return None
        removed_patient = self.front
        self.front = removed_patient.next

        if self.front is None:
            self.rear = None

        return removed_patient

    def display_queue(self):
        # Display information about all patients in the queue
        current = self.front
        while current:
            appointment_info = f", Appointment Time: {current.appointment_time}" if current.appointment_time else ""
            print(f"Name: {current.name}, Age: {current.age}, Condition: {current.condition}{appointment_info}")
            current = current.next

    def get_queue_list(self):
        # Get a list of patients in the queue
        current = self.front
        queue_list = []
        while current:
            queue_list.append(current)
            current = current.next
        return queue_list

    def schedule_appointment_by_name(self, patient_name):
        # Schedule an appointment for a patient by name
        current = self.front
        while current:
            if current.name == patient_name:
                appointment_time = input(f"Enter appointment time for {patient_name}: ")
                current.appointment_time = appointment_time
                print(f"{patient_name}'s appointment has been scheduled for {appointment_time}.")
                return
            current = current.next

        print(f"Patient with name '{patient_name}' not found in the queue.")

# Function to register a new patient
def register_patient():
    try:
        name = input("Enter patient's name: ")
        age = int(input("Enter patient's age: "))
        gender = input("Enter patient's gender: ")
        condition = input("Enter patient's condition: ")
        return Patient(name, age, gender, condition)
    except ValueError:
        print("Invalid input. Please enter a valid age.")

# Main function implementing the hospital management system
def main():
    hospital_queue = HospitalQueue()

    while True:
        print("\n Hospital Management System")
        print("Maximum number of patients in the queue is 5 ")
        print("1. Register Patient (Insert)")
        print("2. Schedule Appointment by Name")
        print("3. Serve Next Patient (Delete)")
        print("4. Display Queue (Display)")
        print("5. Check Available Seats")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            new_patient = register_patient()
            hospital_queue.enqueue(new_patient)

        elif choice == '2':
            patient_name_to_schedule = input("Enter the patient's name to schedule an appointment: ")
            hospital_queue.schedule_appointment_by_name(patient_name_to_schedule)

        elif choice == '3':
            processed_patient = hospital_queue.dequeue()
            if processed_patient:
                print(f"Serving patient: {processed_patient.name}, Condition: {processed_patient.condition}")
            else:
                print("No patients in the queue. Available seats.")

        elif choice == '4':
            print("\nCurrent Hospital Queue:")
            hospital_queue.display_queue()

        elif choice == '5':
            available_seats = 5 - len(hospital_queue.get_queue_list())
            if available_seats > 0:
                print(f"Number of available seats: {available_seats}")
            else:
                print("No available seats. Queue is full.")

        elif choice == '6':
            print("Exiting the system. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
