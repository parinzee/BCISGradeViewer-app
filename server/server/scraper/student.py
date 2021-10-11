from .parent import Parent


# Student inherits most properties from the parents. Except the few are changed below
class Student(Parent):
    def __init__(
        self,
        username: str,
        password: str,
    ) -> None:
        """
        Takes in Username and Password of a students account. Inherits from Parent.
        """
        # Inherits from parents but instead passes PARENTSWEB-STUDENT
        super().__init__(username, password, "PARENTSWEB-STUDENT")
