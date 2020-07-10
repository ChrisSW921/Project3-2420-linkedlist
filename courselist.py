from course import Course
from recursioncounter import RecursionCounter

class CourseList:
    def __init__(self, head=None):
        self.head = head
        self.csize = 0
        self.amISorted = False
        self.classToSearch = -1

    def is_sorted_helper(self, temp_head):
        if temp_head and temp_head.next:
            if temp_head.cnumber <= temp_head.next.cnumber:
                temp_head = temp_head.next
                self.is_sorted_helper(temp_head)
            elif temp_head.cnumber > temp_head.next.cnumber:
                self.amISorted = False
        self.amISorted = True

    def isSorted(self):
        _ = RecursionCounter()
        if self.head and self.head.next:
            temp_head = self.head
            self.is_sorted_helper(temp_head)
            return self.amISorted
        else:
            return True

    def size_helper(self, temp_head):
        _ = RecursionCounter()
        self.csize += 1
        if not temp_head.next:
            return
        else:
            temp_head = temp_head.next
            self.size_helper(temp_head)


    def size(self):
        if self.head:
            temp_head = self.head
            self.size_helper(temp_head)
            return self.csize
        else:
            return 0

    def calculate_gpa(self):
        _ = RecursionCounter()
        return 1

    def insert_helper(self, new_course, temp_head):
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
                self.new_course.next = temp_head
                self.head = self.new_course
            else:
                temp_head = temp_head.next
                self.insert_helper(new_course, temp_head)

    def insert(self, new_course):
        if not self.head:
            self.head = new_course
        else:
            temp_head = self.head
            self.insert_helper(new_course, temp_head)


    def find_helper(self, temp_head, number):
        _ = RecursionCounter()
        if not temp_head.next:
            if temp_head.cnumber == number:
                self.classToSearch = temp_head
            else:
                self.classToSearch = -1
        else:
            if temp_head.cnumber == number:
                self.classToSearch = temp_head
            else:
                temp_head = temp_head.next
                self.find_helper(temp_head, number)

    def find(self, number):
        self.classToSearch = -1
        if self.head:
            temp_head = self.head
        else:
            return -1
        self.find_helper(temp_head, number)
        return self.classToSearch


    def remove_helper(self, temp_head, prev, number):
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
        _ = RecursionCounter()
        if not self.head:
            return
        else:
            temp_head = self.head
            self.remove_helper(temp_head, None, number)


    def remove_all(self, number):
        while self.find(number) != -1:
            self.remove(number)

cl = CourseList()

cl.insert(Course(1410, "1410 class", 3.0, 2.9))
cl.insert(Course(1400, "1400 class", 3.0, 2.8))
cl.insert(Course(1400, "1400 class", 3.0, 2.8))
cl.insert(Course(1400, "1400 class", 3.0, 2.8))
cl.insert(Course(1400, "1400 class", 3.0, 2.8))
cl.insert(Course(2420, "2420 class", 4.0, 2.5))



print(cl.head)
print(cl.head.next)
print(cl.head.next.next)
print(cl.head.next.next.next)
print(cl.head.next.next.next.next)
print(cl.head.next.next.next.next.next)

cl.remove_all(2420)
print(cl.size())
