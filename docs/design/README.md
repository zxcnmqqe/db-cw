# Проєктування бази даних

## Модель бізнес-об'єктів
@startuml

      entity Users #FF0000
      entity Users.email #ffffff
      entity Users.id #ffffff
      entity Users.password #ffffff
      entity Users.username #ffffff
      entity Users.fullname #ffffff

      entity Project #FF0000
      entity Project.id #ffffff
      entity Project.description #ffffff
      entity Project.name #ffffff
      entity Project.status #ffffff

      entity Members #FF0000

      entity Role #FF0000
      entity Role.name #ffffff
      entity Role.id #ffffff

      entity Grant #FF0000

      entity Permission #FF0000
      entity Permission.permission #ffffff
      entity Permission.id #ffffff
      
      entity Task #FF0000
      entity Task.description #ffffff
      entity Task.id #ffffff
      entity Task.status #ffffff
      entity Task.deadline #ffffff 
      entity Task.name #ffffff
      entity Task.price #ffffff

      entity Participant #FF0000

      Users.email --d-* Users
      Users.id --d-* Users
      Users.fullname --d-* Users
      Users.password --d-* Users
      Users.username --d-* Users
       
      Project.id --d-* Project
      Project.name --d-* Project
      Project.status --d-* Project
      Project.description --d-* Project
      
      Task.description --d-* Task
      Task.id --d-* Task
      Task.status --d-* Task
      Task.name --d-* Task
      Task.price --d-* Task
      Task.deadline --d-* Task

      Role.name --d-* Role
      Role.id --d-* Role

      Permission.permission --d-* Permission
      Permission.id --d-* Permission

      Users "1,1" --u-"0,*" Members
      Members "0,*" --u-"1,1" Project
      Project "1,1" --u-"0,*" Task
      Task "1,1" --u-"0,*" Participant
      Participant "0,*" --u-"1,1" Members
      Role "1,1" --u-"0,*" Members
      Role "1,1"--u-"0,*" Grant
      Grant "1,1"--u-"0,*" Permission

@enduml

# ER-модель
@startuml

    namespace UserProfile {
        entity Users {
            ID: UUID
            USERNAME: TEXT
            PASSWORD: VARCHAR
            FULLNAME: TEXT
            EMAIL: TEXT
        }
    }

    namespace ProjectManagement {
        entity Projects {
            ID: UUID
            name: TEXT
            description: TEXT
            status: TEXT
        }

        entity Tasks {
            ID: UUID
            name: TEXT
            description: TEXT
            status: TEXT
            developer: TEXT
            price: TEXT
        }

        entity Participant {
            ID: UUID
            Name: TEXT
            Status: TEXT
            }
    }

    namespace AccessPolicy {
        entity Members {
            ID: UUID
        }

        entity Roles {
            ID: UUID
            Name: TEXT
        }

        administrator .d.> Roles: instanceOf
        manager .d.> Roles: instanceOf
        user .d.> Roles: instanceOf

        entity Grant {
        }

        entity Permission {
            id: int
            permission: text
        }
    }

Participant "0..*" --- "1*" Members
Tasks "1..*" --- "0..*" Participant
Roles "1" --- "1" Members
Users "1" --- "0..*" Members
Projects "1" --- "1..*" Members
Projects "1" --- "0..*" Tasks
Roles "1,1" -d-- "0,*"  Grant
Grant "0,*" -d-- "1,1" Permission

@enduml

## Опис ER-моделі

### Roles (Ролі у проекті)
Представляє собою ролі, які може приймати користувач у певному проекті.
- id: BINARY - унікальний код користувача у проекті
- name: VARCHAR - назва ролі

### Grant (Сукупність прав)
Це сутність-асоціація, яка зберігає сукупність прав, які має певна роль.
- id: BINARY - унікальний код гранту.

### Permission (Права)
Права, які можуть додаватися до ролі.
- id: BINARY - унікальний код ролі.
- permission: VARCHAR - право, яке надається

### Members (Учасники проекта)
Представляє собою базу з користувачів, які підв'язані до проекту.
- id: BINARY - унікальний код користувача

### Users (Користувачі)
Представляє собою користувачів.
- id: BINARY - унікальний код користувача
- username: VARCHAR - логін користувача
- password: VARCHAR - пароль користувача
- fullname: VARCHAR - справжнє ім'я користувача
- email: VARCHAR - поштова скринька користувача

### Projects (Проєкти)
Представляє собою проєкт.
- id: BINARY - унікальний код
- name: VARCHAR - ім'я проєкту
- description: VARCHAR - опис проєкту
- status: VARCHAR - статус проєкту

### Task (Завдання)
Представляє собою завдання. Має поля:
- id: BINARY - унікальний код
- name: VARCHAR - назва завдання
- description: VARCHAR - опис завдання
- status: VARCHAR - статус завдання
- price: VARCHAR - ціна виконання завдання
- deadline: Date - дата дедлайну

### Participant (Учасники завдання)
Participant - це сутність-асоціація, яка зберігає учасників, які працюють над завданням.
- id: BINARY - унікальний код