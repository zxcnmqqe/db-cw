# Реалізація інформаційного та програмного забезпечення

В рамках проєкту розробляється:
## SQL-скрипт для створення на початкового наповнення бази даних

```sql

-- CreateEnum
CREATE TYPE "Status" AS ENUM ('COMPLETED', 'IN_PROGRESS');

-- CreateTable
CREATE TABLE "users" (
    "id" TEXT NOT NULL,
    "username" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "full_name" TEXT NOT NULL,

    CONSTRAINT "users_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "projects" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "status" "Status" NOT NULL,

    CONSTRAINT "projects_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "members" (
    "id" TEXT NOT NULL,
    "user_id" TEXT NOT NULL,
    "project_id" TEXT NOT NULL,

    CONSTRAINT "members_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "roles" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "member)id" TEXT NOT NULL,

    CONSTRAINT "roles_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "grants" (
    "id" TEXT NOT NULL,
    "role_id" TEXT NOT NULL,

    CONSTRAINT "grants_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "permissions" (
    "id" TEXT NOT NULL,
    "permission" TEXT NOT NULL,
    "grantId" TEXT NOT NULL,

    CONSTRAINT "permissions_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "tasks" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "status" "Status" NOT NULL,
    "price" TEXT NOT NULL,
    "deadline" TIMESTAMP(3) NOT NULL,
    "project_id" TEXT NOT NULL,

    CONSTRAINT "tasks_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "partipicants" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "user_id" TEXT NOT NULL,
    "task_id" TEXT NOT NULL,

    CONSTRAINT "partipicants_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "users_username_key" ON "users"("username");

-- CreateIndex
CREATE UNIQUE INDEX "users_email_key" ON "users"("email");

-- CreateIndex
CREATE UNIQUE INDEX "roles_member)id_key" ON "roles"("member)id");

-- AddForeignKey
ALTER TABLE "members" ADD CONSTRAINT "members_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "members" ADD CONSTRAINT "members_project_id_fkey" FOREIGN KEY ("project_id") REFERENCES "projects"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "roles" ADD CONSTRAINT "roles_member)id_fkey" FOREIGN KEY ("member)id") REFERENCES "members"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "grants" ADD CONSTRAINT "grants_role_id_fkey" FOREIGN KEY ("role_id") REFERENCES "roles"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "permissions" ADD CONSTRAINT "permissions_grantId_fkey" FOREIGN KEY ("grantId") REFERENCES "grants"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "tasks" ADD CONSTRAINT "tasks_project_id_fkey" FOREIGN KEY ("project_id") REFERENCES "projects"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "partipicants" ADD CONSTRAINT "partipicants_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "members"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "partipicants" ADD CONSTRAINT "partipicants_task_id_fkey" FOREIGN KEY ("task_id") REFERENCES "tasks"("id") ON DELETE CASCADE ON UPDATE CASCADE;

```

## RESTfull система управління проектами
controller.py
```python

from flask import Flask
from flask import request, jsonify
from model import Users

app = Flask(__name__)

users = Users()

@app.route("/users", methods=["GET"])
def get_all_users():
    result = users.get_all_users()
    return jsonify(result), 200

@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    result = users.get_user(id)
    return jsonify(result), 200

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    result = users.add_user(data)
    return jsonify(result), 200

@app.route("/users", methods=["PATCH"])
def update_user():
    data = request.get_json()
    result = users.update_user(data)
    return jsonify(result), 200

@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    result = users.delete_user(id)
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)

```

model.pu

```python

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

```
