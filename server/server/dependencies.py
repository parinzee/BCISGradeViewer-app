from .sql.database import sessionLocal

# Dependency to get session for each request.
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
