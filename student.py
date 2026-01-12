def student_details(id, name, age, course):
    return (
        f"id: {id}\n"
        f"name: {name}\n"
        f"age: {age}\n"
        f"course: {course}\n"
    )

    return result


if __name__ == "__main__":
    student_id = 183
    name = "Prajwal"
    age = 19
    course = "CS"   

    print(student_details(student_id, name, age, course))
