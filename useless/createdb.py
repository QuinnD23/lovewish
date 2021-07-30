from data.config import userc, passc, hostc

import psycopg2.extras


async def create_db():
    conn = psycopg2.connect(dbname="postgres", user=userc, password=passc, host=hostc)

    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            try:
                cur.execute("CREATE TABLE spisok (id varchar primary key, my_name varchar, zhel text, price integer default 0);")
            except:
                pass
            try:
                cur.execute("CREATE TABLE info (my_name varchar primary key, lover varchar default 0, money integer default 0, money_plus integer default 0, index varchar default 0);")
            except:
                pass

    conn.close()

# Таблицы:
# cur.execute("CREATE TABLE info (my_name varchar primary key, lover varchar default 0, money integer default 0, money_plus integer default 0, index varchar default 0);")
# cur.execute("CREATE TABLE spisok (id varchar primary key, my_name varchar, zhel text, price integer default 0);")

