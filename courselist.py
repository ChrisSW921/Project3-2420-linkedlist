"""Course list module"""
from course import Course
from recursioncounter import RecursionCounter

class CourseList:
    """Course list class"""
    def __init__(self, head=None):
        self.head = head
        self.csize = 0
        self.am_i_sorted = False
        self.class_to_search = -1

    def __next__(self):
        """Next function"""
        if self.node is None:
            raise StopIteration
        else:
            course = self.node
            self.node = self.node.next
            return course

    def __iter__(self):
        """Iter function"""
        self.node = self.head
        return self

    def is_sorted_helper(self, temp_head):
        """Sorted helper function"""
        _ = RecursionCounter()
        if temp_head and temp_head.next:
            if temp_head.cnumber <= temp_head.next.cnumber:
                temp_head = temp_head.next
                self.is_sorted_helper(temp_head)
            elif temp_head.cnumber > temp_head.next.cnumber:
                self.am_i_sorted = False
        self.am_i_sorted = True

    def is_sorted(self):
        """Sorted function"""
        if self.head and self.head.next:
            temp_head = self.head
            self.is_sorted_helper(temp_head)
            return self.am_i_sorted
        else:
            return True

    def size_helper(self, temp_head):
        """Size helper function"""
        _ = RecursionCounter()
        self.csize += 1
        if not temp_head.next:
            return
        else:
            temp_head = temp_head.next
            self.size_helper(temp_head)

    def size(self):
        """Size function"""
        if self.head:
            temp_head = self.head
            self.size_helper(temp_head)
            return self.csize
        else:
            return 0

    def get_grades(self, node):
        """GPA helper function"""
        _ = RecursionCounter()
        if node is None:
            return 0.0
        return (node.credit_hr() * node.grade()) + self.get_grades(node.next)

    def get_credits(self, node):
        """GPA helper function"""
        RecursionCounter()
        if node is None:
            return 0.0
        return node.credit_hr() + self.get_credits(node.next)

    def calculate_gpa(self):
        """GPA function"""
        grades = self.get_grades(self.head)
        if grades == 0.0:
            return 0.0
        all_credits = self.get_credits(self.head)
        if all_credits == 0.0:
            return 0.0
        return grades / all_credits

    def insert_helper(self, new_course, temp_head):
        """Insert helper function"""
        _ = RecursionCounter()
        if not temp_head.next:
            if new_course.cnumber < temp_head.cnumber:
                new_course.next = temp_head
                self.head = new_course
            else:
                temp_head.next = new_course
        else:
            if new_course.cnumber < temp_head.next.cnumber:
                new_course.next = temp_head.next
                temp_head.next = new_course
            elif new_course.cnumber < temp_head.cnumber:
                new_course.next = temp_head
                self.head = new_course
            else:
                temp_head = temp_head.next
                self.insert_helper(new_course, temp_head)

    def insert(self, new_course):
        """Insert function"""
        if not isinstance(new_course, Course):
            raise ValueError
        if not self.head:
            self.head = new_course
        else:
            temp_head = self.head
            self.insert_helper(new_course, temp_head)


    def find_helper(self, temp_head, number):
        """Find helper function"""
        _ = RecursionCounter()
        if not temp_head.next:
            if temp_head.cnumber == number:
                self.class_to_search = temp_head
            else:
                self.class_to_search = -1
        else:
            if temp_head.cnumber == number:
                self.class_to_search = temp_head
            else:
                temp_head = temp_head.next
                self.find_helper(temp_head, number)

    def find(self, number):
        """Find function"""
        if not isinstance(number, int):
            raise ValueError
        self.class_to_search = -1
        if self.head:
            temp_head = self.head
        else:
            return -1
        self.find_helper(temp_head, number)
        return self.class_to_search


    def remove_helper(self, temp_head, prev, number):
        """Remove helper function"""
        _ = RecursionCounter()
        if temp_head.cnumber == number and not prev:
            self.head = self.head.next
        elif temp_head.cnumber != number and not prev:
            prev = temp_head
            temp_head = prev.next
            self.remove_helper(temp_head, prev, number)
        elif temp_head.cnumber == number and prev:
            if not temp_head.next:
                prev.next = None
            else:
                prev.next = temp_head.next
                temp_head.next = None
        elif temp_head.cnumber != number and prev:
            if temp_head.next:
                prev = temp_head
                temp_head = temp_head.next
                self.remove_helper(temp_head, prev, number)

    def remove(self, number):
        """Remove function"""
        if not isinstance(number, int):
            raise ValueError
        if not self.head:
            return
        else:
            temp_head = self.head
            self.remove_helper(temp_head, None, number)


    def remove_all(self, number):
        """Remove all function"""
        if not isinstance(number, int):
            raise ValueError
        while self.find(number) != -1:
            self.remove(number)

    def __str__helper(self, node):
        """Str helper function"""
        RecursionCounter()
        if node is None:
            return '\n'
        return str(node) + '\n' + self.__str__helper(node.next)

    def __str__(self):
        """Str function"""
        return self.__str__helper(self.head)


# cl = CourseList()
# cl.insert(Course(1000))
# for _ in range(20):
#     cl.insert(Course(1200))
# cl.insert(Course(1800))
# print(cl.size())
# cl.remove_all(1200)
# print(cl.size())
