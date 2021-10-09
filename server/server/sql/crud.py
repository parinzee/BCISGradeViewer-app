from sqlalchemy.orm import Session
from . import models, schemas
from ..security import encryptor


# Gets the user.
def get_user(db: Session, username: str, student: bool):
    if student:
        return (
            db.query(models.Student).filter(models.Student.username == username).first()
        )
    else:
        return (
            db.query(models.Parent).filter(models.Parent.username == username).first()
        )


def create_parent(db: Session, parent: schemas.ParentCreate):
    # Encrypt password before storing in db.
    encryptedPassword = encryptor.encrypt(parent.password.encode("utf-8"))
    dbUser = models.Parent(username=parent.username, password=encryptedPassword)
    db.add(dbUser)
    db.commit()
    db.refresh(dbUser)
    return dbUser


def _handle_student(student: schemas.StudentCreate):
    if student.username and student.password:
        encryptedPassword = encryptor.encrypt(student.password.encode("utf-8"))
        return models.Student(
            username=student.username,
            password=encryptedPassword,
            student_id=student.student_id,
            parent=student.parent,
            classes=student.classes,
        )
    else:
        return models.Student(
            student_id=student.student_id,
            parent=student.parent,
            classes=student.classes,
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
                models.Student.parent: student.parent,
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


# No delete statement due to us not actually being the provider of the API
