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

    session = Session()
    state = session.query(State).order_by(State.id).first()

    if state is not None:
        print(f'{state.id}: {state.name}')
    else:
        print('Nothing')
