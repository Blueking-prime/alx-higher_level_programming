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

    # Update state in database
    session = Session()

    state_2 = session.query(State).filter_by(id=2).first()
    state_2.name = 'New Mexico'

    session.commit()
