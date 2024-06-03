import psycopg2 as psycopg2


class Users:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
        dbname="test",
        user="postgres",
        host="localhost",
        port="5432"
    )
            print("Connection to database established successfully!")
            self.cursor = self.connection.cursor()
        except psycopg2.Error as error:
            print("Failed to connect to the database:", str(error))

    def get_all_users(self):
        try:
            self.cursor.execute("SELECT * FROM users")
            result = self.cursor.fetchall()
            if self.cursor.rowcount == 0:
                return {"message": "There are no users", "error": "Not Found", "status_code": 404}
            return {"data": result, "status_code": 200}
        except psycopg2.Error as error:
            return {"message": str(error), "error": "Database Error", "status_code": 500}

    def get_user(self, id):
        if not str(id).isdigit():
            return {"message": "Invalid user id", "error": "Bad Request", "status_code": 400}
        try:
            self.cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
            result = self.cursor.fetchall()
            if self.cursor.rowcount == 0:
                return {"message": f"There is no user with id {id}", "error": "Not Found", "status_code": 404}
            return {"data": result, "status_code": 200}
        except psycopg2.Error as error:
            return {"message": str(error), "error": "Database Error", "status_code": 500}

    def add_user(self, data):
        data = dict(data)
        required_keys = {'id', 'username', 'email', 'password', 'full_name'}
        if not required_keys.issubset(data):
            return {"message": "Invalid or missing keys", "error": "Bad Request", "status_code": 400}
        try:
            query = "INSERT INTO users (id, username, email, password, full_name) VALUES (%s, %s, %s, %s, %s)"
            values = (data['id'], data['username'], data['email'], data['password'], data['full_name'])
            self.cursor.execute(query, values)
            self.connection.commit()
            if self.cursor.rowcount > 0:
                return {"message": "User added succesfully", "status_code": 200}
            else:
                return {"message": "User wasn`t added to database", "error": "Not Acceptable", "status_code": 406}
        except psycopg2.Error as error:
            self.connection.rollback()
            return {"message": "Add user failed: " + str(error), "error": "Database Error", "status_code": 500}


    def update_user(self, data):
        data = dict(data)
        if 'id' not in data:
            return {"message": "No user id provided", "error": "Bad Request", "status_code": 400}
        id = data['id']
        del data['id']
        if not data:
            return {"message": "No data provided", "error": "Bad Request", "status_code": 400}
        set_clause = ', '.join([f"{key} = %s" for key in data])
        values = list(data.values())
        values.append(id)  # id should be appended to the end for the WHERE clause

        try:
            query = f"UPDATE users SET {set_clause} WHERE id = %s::integer"  # Cast id to integer
            self.cursor.execute(query, values)
            self.connection.commit()

            if self.cursor.rowcount > 0:
                return {"message": "User updated successfully", "status_code": 200}
            else:
                return {"message": "User wasn't updated", "error": "Not Found", "status_code": 404}
        except psycopg2.Error as error:
            self.connection.rollback()
            return {"message": "User update failed: " + str(error), "error": "Database Error", "status_code": 500}

    def delete_user(self, id):
        if not str(id).isdigit():
            return {"message": "Invalid user id", "error": "Bad Request", "status_code": 400}
        try:
            self.cursor.execute("DELETE FROM users WHERE id = %s", (id,))
            self.connection.commit()

            if self.cursor.rowcount > 0:
                return {"message": "User deleted successfully", "status_code": 200}
            else:
                return {"message": "Nothing to delete", "error": "Not Found", "status_code": 404}
        except Exception as error:
            self.connection.rollback()
            return {"message": "Delete user failed", "error": str(error), "status_code": 500}