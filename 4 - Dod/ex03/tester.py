#!/usr/bin/env python3
from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)
print("\n--------Bad input test--------")
student = Student(name="Edward", surname="agle", id="toto")
print(student)
