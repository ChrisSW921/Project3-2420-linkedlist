"""Main module"""

from courselist import CourseList
from course import Course

def main():
    """Main Function"""
    course_list = CourseList()
    number, name, credit, grade = range(4)
    with open("data.txt") as file:
        for line in file:
            data = line.strip().split(",")
            course_list.insert(Course(int(data[number]), data[name], float(data[credit]), float(data[grade])))

    print("Current List: (" + str(course_list.size()) + ")")
    print(course_list)
    print()
    print(f"Cumulative GPA: {course_list.calculate_gpa():.3f}")
    print()


if __name__ == "__main__":
    main()
