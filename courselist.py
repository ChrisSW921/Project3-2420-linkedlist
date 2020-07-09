from course import Course
from recursioncounter import RecursionCounter

class CourseList:
    def __init__(self, head=None):
        self.head = head
        self.head_after_operation = None
        self.csize = 0
        self.previous_head_for_removal = None


    def is_sorted_helper(self, temp_head):
        if temp_head and temp_head.cnext:
            if temp_head.cnumber <= temp_head.cnext.cnumber:
                temp_head = temp_head.cnext
                self.is_sorted_helper(self, temp_head)
            elif temp_head.cnumber > temp_head.cnext.cnumber:
                return False
        return True

    def isSorted(self):
        _ = RecursionCounter()
        if self.head and self.head.next:
            temp_head = self.head
            self.is_sorted_helper(temp_head)
        else:
            return True

    def size_helper(self, temp_head):
        _ = RecursionCounter()
        self.csize += 1
        if temp_head.cnext:
            temp_head = temp_head.cnext
            self.size_helper(self, temp_head)
        else:
            return self.csize


    def size(self):
        if self.head:
            temp_head = self.head
            self.size_helper(temp_head)
        else:
            return 0



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
            elif new_course.cnumber < self.head.cnumber:
                self.new_course.cnext = self.head
                self.head = self.new_course
            else:
                self.head = self.head.cnext
                self.insert(self, new_course)

    def find_helper(self, temp_head, number):
        _ = RecursionCounter()
        if not temp_head.cnext:
            if temp_head.cnumber == number:
                return temp_head
            else:
                return -1
        else:
            if temp_head.cnumber == number:
                return temp_head
            else:
                temp_head = temp_head.cnext
                self.find_helper(self, temp_head, number)

    def find(self, number):
        if self.head:
            temp_head = self.head
        else:
            return -1
        self.find_helper(temp_head, number)

    def remove(self, number):
        _ = RecursionCounter()
        if not self.head:
            return
        elif self.head.cnumber == number and not self.head.cnext:
            self.head = None
        elif self.head.cnumber == number and not self.previous_head_for_removal:
            self.new_head = self.head.cnext
            self.head.cnext = None
            self.head = self.new_head
        elif self.head.cnumber == number and self.previous_head_for_removal:
            self.previous_head_for_removal.cnext = self.head.next
            self.head.next
        elif self.head.cnumber != number:
            self.previous_head_for_removal = self.head
            self.head = self.head.cnext

    def remove_all(self):
        return 0