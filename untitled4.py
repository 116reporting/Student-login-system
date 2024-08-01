import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Bloodysweet19",
        database="student"
    )

    if conn.is_connected():
        print("Connected to MySQL database")

    # Create a cursor object
    cursor = conn.cursor()

    # Create tables (if not already created)
    create_students_table = '''
    CREATE TABLE IF NOT EXISTS Students (
        StudentID INT PRIMARY KEY AUTO_INCREMENT,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        DateOfBirth DATE,
        EnrollmentDate DATE
    );
    '''
    create_courses_table = '''
    CREATE TABLE IF NOT EXISTS Courses (
        CourseID INT PRIMARY KEY AUTO_INCREMENT,
        CourseName VARCHAR(100),
        Credits INT
    );
    '''
    create_enrollments_table = '''
    CREATE TABLE IF NOT EXISTS Enrollments (
        EnrollmentID INT PRIMARY KEY AUTO_INCREMENT,
        StudentID INT,
        CourseID INT,
        EnrollmentDate DATE,
        FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
        FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
    );
    '''

    create_login_table = '''
    CREATE TABLE IF NOT EXISTS login (
        rollnumber INT PRIMARY KEY,
        username VARCHAR(255),
        password VARCHAR(255),
        admissionno INT,
        class VARCHAR(10),
        phnumber VARCHAR(10),
        email VARCHAR(255),
        city VARCHAR(100),
        hobby VARCHAR(255),
        result INT
    );
    '''

    # Execute table creation commands
    cursor.execute(create_students_table)
    cursor.execute(create_courses_table)
    cursor.execute(create_enrollments_table)
    cursor.execute(create_login_table)

    # Insert data into Students
    insert_students = '''
    INSERT INTO Students (FirstName, LastName, DateOfBirth, EnrollmentDate)
    VALUES (%s, %s, %s, %s)
    '''
    students_data = [
        ('Alice', 'Johnson', '2001-03-12', '2024-07-01'),
        ('Bob', 'Brown', '2000-08-25', '2024-07-01'),
        ('Charlie', 'Davis', '1999-12-30', '2024-07-01'),
        ('Diana', 'Wilson', '2000-05-17', '2024-07-01'),
        ('Eve', 'Taylor', '2001-07-22', '2024-07-01')
    ]

    # Insert data into Courses
    insert_courses = '''
    INSERT INTO Courses (CourseName, Credits)
    VALUES (%s, %s)
    '''
    courses_data = [
        ('Database Systems', 3),
        ('Operating Systems', 4),
        ('Design and Analysis of Algorithms', 3),
        ('Software Engineering', 3),
        ('Computer Networks', 4)
    ]

    # Insert data into Enrollments
    insert_enrollments = '''
    INSERT INTO Enrollments (StudentID, CourseID, EnrollmentDate)
    VALUES (%s, %s, %s)
    '''
    enrollments_data = [
        (2, 2, '2024-07-01'),
        (3, 1, '2024-07-01'),
        (3, 3, '2024-07-01'),
        (4, 2, '2024-07-01'),
        (4, 4, '2024-07-01'),
        (5, 3, '2024-07-01'),
        (5, 5, '2024-07-01')
    ]

    # Insert data into login
    insert_login = '''
    INSERT INTO login (rollnumber, username, password, admissionno, class, phnumber, email, city, hobby, result)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    person_info_data = [
        (7073412, 'Mohit', 'Prateek', 42, '10th and h', '9548024128', 'gautampm2006@gmail.com', 'roorkee', 'watching movies', 85),
        (7073567, 'rohit', 'krateek', 49, '11th and h', '9548067128', 'rohitpm2006@gmail.com', 'modinagar', 'cricket', 95)
    ]

    # Execute insert commands
    cursor.executemany(insert_students, students_data)
    cursor.executemany(insert_courses, courses_data)
    cursor.executemany(insert_enrollments, enrollments_data)
    cursor.executemany(insert_login, person_info_data)

    # Commit changes
    conn.commit()
    print("Data inserted successfully")

except Error as e:
    print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()
