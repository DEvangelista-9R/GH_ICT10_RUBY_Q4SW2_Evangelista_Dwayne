from js import document  # type: ignore


class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return (
            f"Hello! My name is {self.name}. "
            f"I am from Section {self.section}, "
            f"and my favorite subject is {self.favorite_subject}."
        )


classmates = [
    Classmate("Kaitlyn", "Ruby", "Math"),
    Classmate("Aisha", "Ruby", "Science"),
    Classmate("Zipporah", "Ruby", "English"),
    Classmate("Jade", "Ruby", "Social Studies"),
    Classmate("Koby", "Ruby", "Homeroom")
]


def show_classmates():
    output = document.getElementById("output")

    text = "<h2>Classmate Introductions</h2>"

    for student in classmates:
        text += f"<p>{student.introduce()}</p>"

    output.innerHTML = text


def add_classmate(event=None):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    favorite_subject = document.getElementById("favorite_subject").value

    if name.strip() == "" or favorite_subject.strip() == "":
        return

    classmates.append(
        Classmate(name, section, favorite_subject)
    )

    show_classmates()

    document.getElementById("name").value = ""
    document.getElementById("section").value = "Ruby"
    document.getElementById("favorite_subject").value = ""


show_classmates()