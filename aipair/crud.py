import sqlite3

DB_PATH = "courses.db"

def get_conn():
    try:
        return sqlite3.connect(DB_PATH)
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def create_table():
    try:
        conn = get_conn()
        if conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS Courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    duration INTEGER NOT NULL,
                    fee REAL NOT NULL
                )
            """)
            conn.commit()
            conn.close()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def add_course(title, duration, fee):
    try:
        conn = get_conn()
        if conn:
            conn.execute(
                "INSERT INTO Courses (title, duration, fee) VALUES (?, ?, ?)",
                (title, duration, fee)
            )
            conn.commit()
            conn.close()
    except sqlite3.Error as e:
        print(f"Error adding course: {e}")

def get_courses():
    try:
        conn = get_conn()
        if conn:
            cursor = conn.execute("SELECT id, title, duration, fee FROM Courses")
            results = cursor.fetchall()
            conn.close()
            return results
    except sqlite3.Error as e:
        print(f"Error fetching courses: {e}")
    return []

def get_course(course_id):
    try:
        conn = get_conn()
        if conn:
            cursor = conn.execute(
                "SELECT id, title, duration, fee FROM Courses WHERE id = ?",
                (course_id,)
            )
            result = cursor.fetchone()
            conn.close()
            return result
    except sqlite3.Error as e:
        print(f"Error fetching course: {e}")
    return None

def update_course(course_id, title, duration, fee):
    try:
        conn = get_conn()
        if conn:
            conn.execute(
                "UPDATE Courses SET title = ?, duration = ?, fee = ? WHERE id = ?",
                (title, duration, fee, course_id)
            )
            conn.commit()
            conn.close()
    except sqlite3.Error as e:
        print(f"Error updating course: {e}")

def delete_course(course_id):
    try:
        conn = get_conn()
        if conn:
            conn.execute("DELETE FROM Courses WHERE id = ?", (course_id,))
            conn.commit()
            conn.close()
    except sqlite3.Error as e:
        print(f"Error deleting course: {e}")

if __name__ == "__main__":
    create_table()
    # Example usage:
    # add_course("Python Basics", 30, 5000)
    # print(get_courses())
    # update_course(1, "Python Advanced", 40, 6000)
    # delete_course(1)
