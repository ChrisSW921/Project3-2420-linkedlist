from course import Course
from recursioncounter import RecursionCounter

class CourseList:
    def __init__(self, head=None):
        self.head = head
        self.csize = 0

    def isSorted(self):
        _ = RecursionCounter()
        if self.head and self.head.next:
            if self.head.cnumber < self.head.cnext.cnumber:
                self.head = self.head.cnext
                self.isSorted(self)
            else:
                return False
        else:
            return True
        return True

    def size(self):
        _ = RecursionCounter()
        if self.head:
            self.csize += 1
            if self.head.cnext:
                self.head = self.head.cnext
                self.size(self)
            else:
                return self.csize
        else:
            return 0
        return self.csize


    def calculate_gpa(self):
        _ = RecursionCounter()
        return 1

    def insert(self, new_course):
        _ = RecursionCounter()
        if not self.head:
            self.head = new_course
        elif not self.head.cnext:
            if new_course.cnumber < self.head.cnumber:
                new_course.cnext = self.head
                self.head = new_course
            else:
                self.head.cnext = new_course
        else:
            if new_course.cnumber < self.head.cnext.cnumber:
                self.head.cnext = new_course
                new_course.cnext = self.head.cnext.cnext
            else:
                self.head = self.head.cnext
                self.insert(self, new_course)

    def find(self, number):
        _ = RecursionCounter()
        if not self.head:
            return -1
        elif not self.head.cnext:
            if self.head.cnumber == number:
                return self.head
            else:
                return -1
        else:
            if self.head.cnumber == number:
                return self.head
            else:
                self.head = self.head.cnext
                self.find(self, number)

    def remove(self, number):
        _ = RecursionCounter()
        return number

    def remove_all(self):
        return 0