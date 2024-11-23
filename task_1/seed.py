from faker import Faker
from task_1.connection import db_connect

fake = Faker()
users_count = 10

try:
    with db_connect() as conn:
        with  conn.cursor() as cursor:
            # Insert data into users table
            for _ in range(users_count):
                cursor.execute(
                    '''
                    INSERT INTO users (fullname, email)
                    VALUES (%s, %s)
                    RETURNING id;
                    ''',
                    (fake.name(), fake.unique.email()),
                )

            # Insert data into status table
            for status in ['new', 'in progress', 'completed']:
                cursor.execute(
                    '''
                    INSERT INTO status (name)
                    VALUES (%s);
                    ''',
                    (status,),
                )

            conn.commit()

            cursor.execute('SELECT id FROM users')
            user_ids = [row[0] for row in cursor.fetchall()]

            cursor.execute('SELECT id FROM status')
            status_ids = [row[0] for row in cursor.fetchall()]

            # Insert data into tasks table
            for _ in range(users_count*2):
                title = fake.sentence(nb_words=6)
                description = fake.paragraph(nb_sentences=3)
                status_id = fake.random.choice(status_ids)
                user_id = fake.random.choice(user_ids)

                cursor.execute(
                    '''
                    INSERT INTO tasks (title, description, status_id, user_id)
                    VALUES (%s, %s, %s, %s);
                    ''',
                    (title, description, status_id, user_id),
                )

            conn.commit()
            print("Data seeded successfully.")

except Exception as error:
    print(f"Error: {error}")
