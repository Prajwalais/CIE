def student_details(id, name, age, course):
    return (
        f"id: {id}\n"
        f"name: {name}\n"
        f"age: {age}\n"
        f"course: {course}\n"
    )


if __name__ == "__main__":
    import sys
    _, id, name, age, course = sys.argv
    print(student_details(id, name, age, course))
