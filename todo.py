import mysql.connector as mysql

# Establish database connection
con = mysql.connect(host="localhost", user="root", passwd="Sanika@12")

cursor = con.cursor()

# Create database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS TODOAPP")
print("Database created.....")

# Use the created database
cursor.execute("USE TODOAPP")

# Create table if not exists
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS tb_todo(
           id INT AUTO_INCREMENT PRIMARY KEY,
           task VARCHAR(50) NOT NULL,
           status ENUM('pending','completed') DEFAULT 'pending'
    )'''
)

print("Table created.......")

# Task Management System
while True:
    print("\n Task Management")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        cursor.execute("INSERT INTO tb_todo (task) VALUES (%s)", (task,))
        con.commit()
        print("✅ Task added successfully!")

    elif choice == "2":
        cursor.execute("SELECT * FROM tb_todo")
        tasks = cursor.fetchall()
        if not tasks:
            print("No tasks found.")
        else:
            print("\nID | Task | Status")
            for task in tasks:
                print(f"{task[0]} | {task[1]} | {task[2]}")

    elif choice == "3":
        task_id = input("Enter task ID to update: ")
        new_status = input("Enter new status (pending/completed): ").lower()
        if new_status in ["pending", "completed"]:
            cursor.execute("UPDATE tb_todo SET status = %s WHERE id = %s", (new_status, task_id))
            con.commit()
            print("✅ Task updated successfully!")
        else:
            print("Invalid status. Please enter 'pending' or 'completed'.")

    elif choice == "4":
        task_id = input("Enter task ID to delete: ")
        cursor.execute("DELETE FROM tb_todo WHERE id = %s", (task_id,))
        con.commit()
        print("✅ Task deleted successfully!")

    elif choice == "5":
        print("Exiting Task Manager. Goodbye! 👋")
        break

    else:
        print("❌ Invalid choice. Please select a valid option.")

# Close the database connection
cursor.close()
con.close()
