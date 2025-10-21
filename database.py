from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from pymysql.constants import CLIENT

load_dotenv()

db_url = f'mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}'

engine = create_engine(
    db_url,
    connect_args={"client_flag": CLIENT.MULTI_STATEMENTS}
)



session =sessionmaker(bind = engine)

db = session()


# db.execute(create_table_query)
# print("Tables has been created")

# # query =  text("select * from user")
# # users = db.execute(query).fetchall()
# # print(users)
#                         

create_table_query = text("""
CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS courses(
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    level VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS enrollments(
    id INT AUTO_INCREMENT PRIMARY KEY,
    userid INT,
    courseid INT,
    FOREIGN KEY(userid) REFERENCES users(id),
    FOREIGN KEY(courseid) REFERENCES courses(id)
);
""")

db.execute(create_table_query)
db.commit()

print("Tables have been created")