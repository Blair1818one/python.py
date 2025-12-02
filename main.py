#Bank assignment 
class BankQueue:
    def __init__(self):
        self.queue = []

    # Add a customer to the queue
    def enqueue(self, customer):
        self.queue.append(customer)
        print(f"{customer} joined the queue.")

    # Remove a customer when served
    def dequeue(self):
        if self.is_empty():
            print("No customers to serve. Queue is empty.")
            return None
        served = self.queue.pop(0)
        print(f"{served} has been served and left the queue.")
        return served

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Get number of customers currently in queue
    def queue_size(self):
        return len(self.queue)

    # Display current queue
    def display_queue(self):
        print(f"Current queue ({self.queue_size()} customers): {self.queue}")


# ---------------------------------------------------------
# SIMULATION OF REQUIRED EVENTS
# ---------------------------------------------------------

if __name__ == "__main__":
    bank = BankQueue()

    print("\n--- Simulation Start ---\n")

    # 1. Three customers arrive
    bank.enqueue("Customer 1")
    bank.enqueue("Customer 2")
    bank.enqueue("Customer 3")
    bank.display_queue()

    print("\n--- First customer served ---\n")

    # 2. First customer is served
    bank.dequeue()
    bank.display_queue()

    print("\n--- Another customer arrives ---\n")

    # 3. Another customer arrives
    bank.enqueue("Customer 4")
    bank.display_queue()

    print("\n--- Simulation Complete ---")




#African leaders number

# 1. Create the lists
west_african_leaders = [
    "Kwame Nkrumah",
    "Léopold Sédar Senghor",
    "Modibo Keita",
    "Félix Houphouët-Boigny",
    "Ahmed Sékou Touré",
    "Tafawa Balewa",
    "Hamani Diori",
    "Sir Abubakar Tafawa Balewa"
]

east_african_leaders = [
    "Julius Nyerere",
    "Jomo Kenyatta",
    "Milton Obote",
    "Haile Selassie",
    "Aboud Jumbe",
    "Hassan Gouled Aptidon",
    "Ali Hassan Mwinyi",
    "Siad Barre"
]

# 2. Remove duplicates
def remove_duplicates(names_list):
    return list(dict.fromkeys(names_list))

west_african_leaders = remove_duplicates(west_african_leaders)
east_african_leaders = remove_duplicates(east_african_leaders)

# 3. Function to count surname occurrences
def leader_count(surname, group):
    count = 0
    for full_name in group:
        # compare last name
        if surname.lower() == full_name.lower().split()[-1]:
            count += 1
    return count

# 4. Use the function
surname = "Nyerere"
count_west = leader_count(surname, west_african_leaders)
count_east = leader_count(surname, east_african_leaders)

if count_west > 0:
    print("Nyerere belongs to the West African Leaders list.")
elif count_east > 0:
    print("Nyerere belongs to the East African Leaders list.")
else:
    print("Nyerere does not belong to any list.")

# 5. Function to check if a name exists in both lists
def is_in_both_lists(name):
    return name in west_african_leaders and name in east_african_leaders

# Example
print(is_in_both_lists("Julius Nyerere"))






#2024 no 1 a
# ----- QUEUE IMPLEMENTATION -----

queue = []

def enqueue(item):
    queue.append(item)
    print("After enqueue:", queue)

def dequeue():
    if not is_empty():
        removed = queue.pop(0)
        print("After dequeue:", queue)
        return removed
    return "Queue is empty"

def peek():
    if not is_empty():
        return queue[0]
    return "Queue is empty"

def is_empty():
    return len(queue) == 0


# ----- TEST QUEUE WITH AT LEAST 3 ELEMENTS -----

enqueue(10)
enqueue(20)
enqueue(30)

print("Front element:", peek())
print("Dequeued:", dequeue())
print("Is the queue empty?", is_empty())



#2024 no 1 b

# ----- STACK IMPLEMENTATION -----

stack = []

def push(item):
    stack.append(item)
    print("After push:", stack)

def pop_item():
    if not is_empty_stack():
        removed = stack.pop()
        print("After pop:", stack)
        return removed
    return "Stack is empty"

def peek_stack():
    if not is_empty_stack():
        return stack[-1]
    return "Stack is empty"

def is_empty_stack():
    return len(stack) == 0


# ----- TEST STACK WITH AT LEAST 3 ELEMENTS -----

push(5)
push(15)
push(25)

print("Top element:", peek_stack())
print("Popped:", pop_item())
print("Is the stack empty?", is_empty_stack())


#2024 no 2 part a 
# ----------------- BINARY SEARCH -----------------

patient_ids = [101, 112, 130, 145, 157, 190, 205]

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test
print("Binary search for 157:", binary_search(patient_ids, 157))
print("Binary search for 999:", binary_search(patient_ids, 999))


#Question 2 2024 part b
# ----------------- LINEAR SEARCH -----------------

patient_ids = [101, 112, 130, 145, 157, 190, 205]

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

# Test
print("Linear search for 145:", linear_search(patient_ids, 145))
print("Linear search for 777:", linear_search(patient_ids, 777))


#Question 2 2024 part c
# ----------------- QUICK SORT -----------------

medical_record_numbers = [145, 101, 190, 157, 130, 205, 112]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

# Test
sorted_records = quick_sort(medical_record_numbers)
print("Sorted medical record numbers:", sorted_records)



#2024 question 3
# ----------------- STUDENT MANAGEMENT SYSTEM -----------------

# a) Declare and initialize names and scores
students = ["John", "Mary", "Alice", "Brian", "Eva", "Chris", "Diana", "Mark", "Paul", "Nancy"]
scores = [78, 92, 65, 88, 73, 90, 55, 81, 69, 95]

# b) Function to analyze scores
def analyze_scores(names, scores):
    avg = sum(scores) / len(scores)
    
    highest = max(scores)
    lowest = min(scores)
    
    highest_student = names[scores.index(highest)]
    lowest_student = names[scores.index(lowest)]
    
    above_avg = sum(1 for s in scores if s > avg)
    
    print("Average score:", avg)
    print("Highest score:", highest, "->", highest_student)
    print("Lowest score:", lowest, "->", lowest_student)
    print("Number of students above average:", above_avg)

# c) Sort students in descending order of scores
def sort_descending(names, scores):
    combined = list(zip(names, scores))
    combined.sort(key=lambda x: x[1], reverse=True)
    
    print("Sorted records (name, score):")
    for record in combined:
        print(record[0], "->", record[1])

# d) Search for student's score by name
def search_student(names, scores, target_name):
    for i in range(len(names)):
        if names[i].lower() == target_name.lower():
            return scores[i]
    return "Student not found"

# ------- TESTING -------
analyze_scores(students, scores)
sort_descending(students, scores)

print("Score for Alice:", search_student(students, scores, "Alice"))
print("Score for Tom:", search_student(students, scores, "Tom"))


