class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self):
        passing_score = 40
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        if name not in self.students:
            self.students[name] = Student(name, scores)
        else:
            print(f"Student {name} already exists.")

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)

    def display_student_performance(self):
        for student in self.students.values():
            avg_score = student.calculate_average()
            passing_status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"{student.name}: Average = {avg_score:.2f}, Status = {passing_status}")


def get_student_data():
    name = input("Enter student's name: ")
    scores = []
    for subject in ["Math", "Science", "English"]:
        while True:
            try:
                score = int(input(f"Enter {subject} score: "))
                scores.append(score)
                break
            except ValueError:
                print("Invalid input. Please enter a valid score (integer).")
    return name, scores


def main():
    tracker = PerformanceTracker()

    while True:
        name, scores = get_student_data()
        tracker.add_student(name, scores)

        more_students = input("Do you want to add another student? (yes/no): ").strip().lower()
        if more_students != "yes":
            break

    tracker.display_student_performance()
    class_avg = tracker.calculate_class_average()
    print(f"\nClass Average: {class_avg:.2f}")


if __name__ == "__main__":
    main()
