#!/usr/bin/python3
'''a script that lists a specific State object from a database'''

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    usrname = sys.argv[1]
    pswrd = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    eng_link = f'mysql+mysqldb://{usrname}:{pswrd}@localhost/{dbname}'

    engine = create_engine(eng_link, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()
    states = session.query(State).filter_by(name=state_name)

    for state in states:
        print(state.id)
        sys.exit(0)
    else:
        print('Not found')
