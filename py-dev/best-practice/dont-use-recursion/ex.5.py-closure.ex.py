students = {
    'Alice': 98,
    'Bob': 67,
    'Chris': 85,
    'David': 75,
    'Ella': 54,
    'Fiona': 35,
    'Grace': 69
}


def make_student_classifier(lower_bound, upper_bound):
    def classify_student(exam_dict):
        return {k: v for (k, v) in exam_dict.items() if lower_bound <= v < upper_bound}
    return classify_student


grade_A = make_student_classifier(80, 100)
grade_B = make_student_classifier(70, 80)
grade_C = make_student_classifier(50, 70)
grade_D = make_student_classifier(0, 50)
