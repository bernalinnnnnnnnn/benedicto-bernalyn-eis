from connector import Connector

class Employee:

    @staticmethod
    def get_all():
        query = "SELECT * FROM employees"
        Connector.cursor.execute(query)
        result = Connector.cursor.fetchall()
        return result

    @staticmethod
    def get_by_id(emp_id):
        query = "SELECT * FROM employees WHERE emp_id = %s"
        Connector.cursor.execute(query, (emp_id,))
        result = Connector.cursor.fetchone()
        return result

    @staticmethod
    def add_employee(emp_id, lname, fname, mname):
        query = "INSERT INTO employees (emp_id, lname, fname, mname) VALUES (%s, %s, %s, %s)"
        try:
            Connector.cursor.execute(query, (emp_id, lname, fname, mname))
            Connector.db.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def update_employee(emp_id, lname, fname, mname):
        query = "UPDATE employees SET lname = %s, fname = %s, mname = %s WHERE emp_id = %s"
        try:
            Connector.cursor.execute(query, (lname, fname, mname, emp_id))
            Connector.db.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def delete_employee(emp_id):
        query = "DELETE FROM employees WHERE emp_id = %s"
        try:
            Connector.cursor.execute(query, (emp_id,))
            Connector.db.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
