import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from backend import models, crud, schemas
from factory import alchemy, Faker, Sequence

@pytest.fixture(scope="function")
def db_session():
    engine = create_engine('sqlite:///:memory:')
    models.Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    session = scoped_session(session_factory)
    yield session
    session.rollback()
    session.remove()

class UserFactory(alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.User
        sqlalchemy_session = db_session  # Set the session from the fixture
        sqlalchemy_session_persistence = "commit"

    id = Sequence(lambda n: n + 1)
    email = Faker('email')
    username = Faker('user_name')
    hashed_password = Faker('password')

class CategoryFactory(alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.Category
        sqlalchemy_session = db_session  # Set the session from the fixture
        sqlalchemy_session_persistence = "commit"

    id = Sequence(lambda n: n + 1)
    name = Faker('word')
    user_id = Sequence(lambda n: n + 1)

def test_create_user(db_session):
    user_data = schemas.UserCreate(email='test@example.com', username='testuser', password='testpass')
    user = crud.create_user(db_session, user_data)
    assert user.email == 'test@example.com'
    assert user.username == 'testuser'
    assert user.hashed_password == 'testpass'

def test_get_user_by_email(db_session):
    UserFactory(email='test@example.com', username='user1', hashed_password='password')
    user = crud.get_user_by_email(db_session, 'test@example.com')
    assert user is not None
    assert user.email == 'test@example.com'

def test_create_and_get_categories(db_session):
    user = UserFactory()
    crud.create_category(db_session, schemas.CategoryCreate(name='Learning', user_id=user.id))
    categories = crud.get_categories(db_session, user.id)
    assert len(categories) == 1
    assert categories[0].name == 'Learning'

def test_delete_category(db_session):
    user = UserFactory()
    category = CategoryFactory(user_id=user.id, name='Learning')
    crud.delete_category(db_session, category.id)
    categories = crud.get_categories(db_session, user.id)
    assert len(categories) == 0
