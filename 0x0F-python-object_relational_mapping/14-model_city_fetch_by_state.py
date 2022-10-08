#!/usr/bin/python3
'''a script that lists all State objects from a databas'''

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    usrname = sys.argv[1]
    pswrd = sys.argv[2]
    dbname = sys.argv[3]

    eng_link = f'mysql+mysqldb://{usrname}:{pswrd}@localhost/{dbname}'

    engine = create_engine(eng_link, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()
    cities = session.query(City).join(State).order_by(State.id, City.id)

    for city in cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')
