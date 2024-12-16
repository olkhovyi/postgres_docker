import psycopg2

class DatabasePage:
    def __init__(self, connection_settings):
        self.conn = psycopg2.connect(**connection_settings)
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS test_table (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                value INT NOT NULL
            );
            """
        )
        self.conn.commit()

    def insert_record(self, name, value):
        self.cur.execute("INSERT INTO test_table (name, value) VALUES (%s, %s);", (name, value))
        self.conn.commit()

    def update_record(self, old_name, new_name):
        self.cur.execute("UPDATE test_table SET name = %s WHERE name = %s;", (new_name, old_name))
        self.conn.commit()

    def delete_record(self, name):
        self.cur.execute("DELETE FROM test_table WHERE name = %s;", (name,))
        self.conn.commit()

    def select_record(self, name):
        self.cur.execute("SELECT * FROM test_table WHERE name = %s;", (name,))
        return self.cur.fetchone()

    def select_all_records(self):
        self.cur.execute("SELECT * FROM test_table;")
        return self.cur.fetchall()

    def drop_table(self):
        self.cur.execute("DROP TABLE IF EXISTS test_table;")
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

