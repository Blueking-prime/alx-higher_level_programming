#!/usr/bin/python3
'''a script that lists the first State objects from a database'''


if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    usrname = sys.argv[1]
    pswrd = sys.argv[2]
    dbname = sys.argv[3]

    eng_link = f'mysql+mysqldb://{usrname}:{pswrd}@localhost/{dbname}'

    engine = create_engine(eng_link, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    # Delete state in database
    session = Session()

    states = session.query(State).\
        filter(State.name.ilike('%a%')).order_by(State.id)

    for state in states:
        session.delete(state)

    session.commit()
