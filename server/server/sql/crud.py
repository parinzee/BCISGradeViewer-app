from sqlalchemy.orm import Session
from . import models, schemas
from ..security import encryptor
from ..scraper.student import Student


# Gets the user.
def get_user(db: Session, username: str, student: bool):
    if student:
        user = (
            db.query(models.Student).filter(models.Student.username == username).first()
        )
    else:
        user = (
            db.query(models.Parent).filter(models.Parent.username == username).first()
        )
    if user is None:
        return None

    if user.password:
        decryptedPassword = encryptor.decrypt(user.password)
    else:
        decryptedPassword = None
    user.password = decryptedPassword.decode("utf-8")
    return user


def create_parent(db: Session, parent: schemas.ParentCreate):
    # Encrypt password before storing in db.
    encryptedPassword = encryptor.encrypt(parent.password.encode("utf-8"))
    dbUser = models.Parent(username=parent.username, password=encryptedPassword)
    db.add(dbUser)
    db.commit()
    db.refresh(dbUser)
    return dbUser


def _handle_student(student: schemas.StudentCreate):
    scraper = Student(student.username, student.password)
    encryptedPassword = encryptor.encrypt(student.password.encode("utf-8"))
    return models.Student(
        username=student.username,
        password=encryptedPassword,
        student_id=scraper.get_studentIDs(),
    )


def create_student(db: Session, student: schemas.StudentCreate):
    dbUser = _handle_student(student)
    db.add(dbUser)
    db.commit()
    db.refresh(dbUser)
    return dbUser


def update_student(db: Session, student: schemas.StudentCreate):
    dbUser = _handle_student(student)
    if student.username and student.password:
        encryptedPassword = encryptor.encrypt(student.password.encode("utf-8"))
        db.query(models.Student).filter(
            models.Student.student_id == student.student_id
        ).update(
            {
                models.Student.username: student.username,
                models.Student.password: encryptedPassword,
            }
        )
    db.commit()
    db.refresh(dbUser)
    return dbUser


def update_parent(db: Session, parent: schemas.ParentCreate):
    encryptedPassword = encryptor.encrypt(parent.password.encode("utf-8"))
    dbUser = (
        db.query(models.Parent)
        .filter(models.Parent.username == parent.username)
        .update({models.Student.password: encryptedPassword})
    )
    db.commit()
    db.refresh(dbUser)
    return dbUser


# No delete statement due to us not actually being the provider of the database. We're merely webscraping.
