from task_1.connection import db_connect

try:
    with db_connect() as conn:
        with  conn.cursor() as cursor:
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS "users" (
                id SERIAL  PRIMARY KEY,
                fullname VARCHAR(100)  NOT NULL,
                email VARCHAR(100) NOT NULL,
                CONSTRAINT unique_email UNIQUE (email)
            );
              
            CREATE TABLE IF NOT EXISTS "status" (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) CHECK (name in ('new', 'in progress', 'completed'))
            );    
            
            CREATE TABLE IF NOT EXISTS "tasks" (
                id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                description TEXT,
                status_id INT NOT NULL,
                user_id INT NOT NULL,
            CONSTRAINT fk_status
                FOREIGN KEY (status_id) 
                REFERENCES status (id)
                ON DELETE CASCADE,
            CONSTRAINT fk_user
                FOREIGN KEY (user_id)
                REFERENCES users (id)
                ON DELETE CASCADE
            );
            '''

            cursor.execute(create_table_query)
            conn.commit()
            print("Tables created successfully.")

except Exception as error:
    print(f"Error: {error}")