# Модель прецедентів

## Загальна схема

<center style="
   border-radius:4px;
   border: 1px solid #cfd7e6;
   box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
   padding: 1em;"
>

@startuml

    skinparam noteFontColor white

    actor "Користувач" as User


    usecase "<b>Authorization</b>\nАвторизація" as Authorization
    usecase "<b>UserUpdate</b>\nКерування власнми даними" as UserUpdate
    usecase "<b>Support</b>\nЗв'язок з службою підтримки" as Support


    User -r-> Authorization
    User -u-> UserUpdate
    User -l-> Support


    actor "Менеджер" as Manager

    usecase "<b>ProjectManage</b>\nКерувати проектом" as ProjectManage
    usecase "<b>TaskManage</b>\nКерувати задачами" as TaskManage
    usecase "<b>ProjectStatus</b>\nВідслідковувати прогрес проєкту" as ProjectStatus

    Manager -r-> ProjectManage
    Manager -r-> TaskManage
    Manager -l-> ProjectStatus
    Manager -u-|> User

    actor "Адміністратор" as Admin

    usecase "<b>SystemManage</b>\nКерувати системою" as SystemManage
    usecase "<b>TeamManage</b>\nКерувати командою" as TeamManage

    Admin -r-> SystemManage
    Admin -l-> TeamManage
    Admin -u-|> Manager

@enduml
</center>

## Користувач

<center style="
   border-radius:4px;
   border: 1px solid #cfd7e6;
   box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
   padding: 1em;"
>


@startuml

    actor "Користувач" as User

    usecase "<b>AccountManage</b>\nКерувати обліковим записом" as AccountManage
    usecase "<b>Authorization</b>\nКерувати сесією" as Authorization
    usecase "<b>Support</b>\nЗв'язок з службою підтримки" as Support

    User -l-> AccountManage
    User -u-> Authorization
    User -d-> Support

    usecase "<b>UserSignUp</b>\nЗареєструватися" as UserSignUp
    usecase "<b>UserSignIn</b>\nУвійти в систему" as UserSignIn

    UserSignUp ..d.> Authorization :extends
    UserSignIn ..r.> Authorization :extends

    usecase "<b>UserUpdate</b>\nРедагувати дані користувача" as UserUpdate
    usecase "<b>UserDelete</b>\nВидалити користувача" as UserDelete

    UserUpdate ..d.> AccountManage :extends
    UserDelete ..r.> AccountManage :extends

@enduml

</center>

## Менеджер

<center style="
   border-radius:4px;
   border: 1px solid #cfd7e6;
   box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
   padding: 1em;"
>


@startuml

    actor "Менеджер" as Manager

    usecase "<b>ProjectManage</b>\nКерувати проєктами" as ProjectManage
    Manager -d-> ProjectManage

    usecase "<b>ProjectCreate</b>\nСтворити проєкт" as ProjectCreate
    usecase "<b>ProjectUpdate</b>\nРедагувати проєкт" as ProjectUpdate
    usecase "<b>ProjectDelete</b>\nВидалити проєкту" as ProjectDelete

    ProjectCreate ..d.> ProjectManage :extends
    ProjectUpdate ..r.> ProjectManage :extends
    ProjectDelete ..r.> ProjectManage :extends

    usecase "<b>TaskManage</b>\nКерувати задачами" as TaskManage
    Manager -u-> TaskManage

    usecase "<b>TaskAdd</b>\nДодавання задачі в проєкт" as TaskAdd
    usecase "<b>TaskUpdate</b>\nРедагування задачі в проєкті" as TaskUpdate
    usecase "<b>TaskDelete</b>\nВидалення задачі з проєкту" as TaskDelete

    TaskManage ..d.> TaskAdd :extends
    TaskManage ..r.> TaskUpdate :extends
    TaskManage ..r.> TaskDelete :extends
@enduml

</center>

### Адміністратор

<center style="
   border-radius:4px;
   border: 1px solid #cfd7e6;
   box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
   padding: 1em;"
>

@startuml

    actor "Адмінстратор" as Admin

    usecase "<b>AddUser</b>\nДодати користувача" as AddUser
    usecase "<b>DeleteUser</b>\nВидалити користувача" as DeleteUser

    usecase "<b>TeamManage</b>\nКерувати командою" as TeamManage
    usecase "<b>SystemManage</b>\nКерувати системою" as SystemManage

    Admin -d-> TeamManage
    Admin -d-> SystemManage

    AddUser ..u.> TeamManage :extends
    DeleteUser .l.> TeamManage :extends

@enduml

</center>

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;"
>

**Діаграма прецедентів**

# Сценарії використання

### UserSignUp

<table>
    <tr>
        <td><b>ID</b></td>
        <td><code>UserSignUp</code></td>
    </tr>
    <tr>
        <td><b>Назва:</b></td>
        <td>Реєстрація нового облікового запису</td>
    </tr>
     <tr>
        <td><b>Учасники:</b></td>
        <td>Користувач, система</td>
    </tr>
     <tr>
        <td><b>Передумови:</b></td>
        <td>Користувач не має облікового запису</td>
    </tr>
     <tr>
        <td><b>Результат:</b></td>
        <td>Новий обліковий запис</td>
    </tr>
     <tr>
        <td><b>Виключні ситуації:</b></td>
        <td>
        - SignUpException_InvalidData - введені користувачем дані не коректні<br/>
        - SignUpException_AccAlreadyExist - обліковий запис по вказаному Email вже існує<br/>
        - SignUpException_InvalidEmail - введений Email не існує<br/>
        </td>
    </tr>
</table>


@startuml

    |Користувач|
    start;

    :Натискає кнопку "Зареєструватися";
    |Система|
    :Відкриває вікно з формою для реєстрації;
    |Користувач|
    :Заповнює поля у формі для реєстрації;
    :Натискає на кнопку "Створити";
    |Система|
    :Перевіряє введені дані;
    note right #ffaaaa
    <b> Можливі помилки:
    <b> SignUpException_InvalidData
    <b> SignUpException_AccAlreadyExist
    <b> SignUpException_InvalidEmail
    end note
    :Створює новий обліковий запис;
    |Користувач|
    stop;

@enduml


### UserSignIn

<table>
    <tr>
        <td><b>ID</b></td>
        <td><code>UserSignIn</code></td>
    </tr>
    <tr>
        <td><b>Назва:</b></td>
        <td>Автентифікація у існуючий обліковий запис</td>
    </tr>
     <tr>
        <td><b>Учасники:</b></td>
        <td>Користувач, система</td>
    </tr>
     <tr>
        <td><b>Передумови:</b></td>
        <td>
         - Користувач має обліковий запис<br/>
         - Користувач не авнтентифікований<br/>
        </td>
    </tr>
     <tr>
        <td><b>Результат:</b></td>
        <td>Користувач автентифікований у системі</td>
    </tr>
     <tr>
        <td><b>Виключні ситуації:</b></td>
        <td>
        - SignInException_InvalidData - введені користувачем дані не коректні<br/>
        - SignInException_AccDoesn`tExist - обліковий запис по вказаному Email не існує<br/>
        - SignInException_InvalidPassword - введений користувачем пароль не правильний<br/>
        </td>
    </tr>
    <tr>
        <td><b>Основний сценарій:</b></td>
        <td>
            <ol>
                <li>Користувач заповнює поля у формі для входу</li>
                <li>Користувач натискає кнопку "Увійти"</li>
                <li>Система перевіряє введені дані(SignInException_InvalidData, SignInException_AccDoesn`tExist, SignInException_InvalidPassword)</li>
                <li>Система автентифікує користувача</li>
            </ol>
        </td>
    </tr>
</table>

@startuml

    |Користувач|
    start;
    :Заповнює поля у формі для входу;
    :Натискає кнопку "Увійти";
    
    |Система|
    :Перевіряє введені дані;
    note right #ffaaaa
    <b> Можливі помилки:
    <b> SignInException_InvalidData
    <b> SignInException_AccDoesn
    <b> SignInException_InvalidPassword
    end note
    :Автентифікує менеджера/користувача;
    
    |Користувач|
    stop;

@enduml

### UserUpdate

| ID                 | <span id=UserUpdate>`UserUpdate`</span>                                                                                                                                                               |
| :----------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Назва:             | Редагування існуючого облікового запису                                                                                                                                                               |
| Учасники:          | Користувач, система                                                                                                                                                                                   |
| Передумови:        | Користувач автентифікований у системі                                                                                                                                                                 |
| Результат:         | Дані облікового запису менеджера/користувача змінені                                                                                                                                                  |
| Виключні ситуації: | Введені Користувачем дані не коректні <font color="red">UserUpdateException_InvalidData</font><br> менеджер/користувач не авторизований <font color="red">UserUpdateException_Unauthorized</font><br> |

@startuml

    |Користувач|
    start;
    
    :Натискає кнопку "Редагувати обліковий запис";

    |Система|
    :Відкриває вікно редагування облікового запису;

    |Користувач|
    :Змінює дані та натискає кнопку "Зберегти";
    
    |Система|
    :Перевіряє введені дані;
    note right #ffaaaa
    <b> Можливі помилки:
    <b> UserUpdateException_InvalidData
    <b> UserUpdateException_Unauthorized
    end note
    
    : Система зберігає зміни в обліковому записі;
    
    |Користувач|
    :Отримує оновленні дані;
    stop;

@enduml

### UserDelete

<table>
    <tr>
        <td><b>ID</b></td>
        <td><code>UserDelete</code></td>
    </tr>
    <tr>
        <td><b>Назва:</b></td>
        <td>Видалення існуючого облікового запису</td>
    </tr>
     <tr>
        <td><b>Учасники:</b></td>
        <td>Користувач, система</td>
    </tr>
     <tr>
        <td><b>Передумови:</b></td>
        <td>
        Користувач автентифікований у системі
        </td>
    </tr>
     <tr>
        <td><b>Результат:</b></td>
        <td>Обліковий запис користувача видалено</td>
    </tr>
     <tr>
        <td><b>Виключні ситуації:</b></td>
        <td>
         UserDeleteException_InvalidPassword - введений користувачем пароль не правильний
        </td>
    </tr>
</table>

@startuml

    |Користувач|
    start;
    :Натискає кнопку "Видалити обліковий запис";
    |Система|
    :Запитує у менеджера/користувача пароль до його облікового запису;
    |Користувач|
    :Вводить пароль і натискає кнопку "Видалити";
    |Система|
    :Перевіряє введені дані;
    note right #ffaaaa
    <b> Можливі помилки:
    <b> UserDeleteException_InvalidPassword
    end note
    :Видаляє обліковий запис;
    |Користувач|
    stop;

@enduml

### ProjectCreate

<table>
    <tr>
        <td><b>ID</b></td>
        <td><code>ProjectCreate</code></td>
    </tr>
    <tr>
        <td><b>Назва:</b></td>
        <td>Створення нового проєкту</td>
    </tr>
     <tr>
        <td><b>Учасники:</b></td>
        <td>Менеджер, система</td>
    </tr>
     <tr>
        <td><b>Передумови:</b></td>
        <td>
         Менеджер автентифікований у системі
        </td>
    </tr>
     <tr>
        <td><b>Результат:</b></td>
        <td>Створено новий проєкт</td>
    </tr>
     <tr>
        <td><b>Виключні ситуації:</b></td>
        <td>
        ProjectCreate_InvalidData - введені менеджером дані не коректні
        </td>
    </tr>
</table>

@startuml

    |Менеджер|
    start;
    :Натискає кнопку "Створити проєкт";
    |Система|
    :Відкриває вікно з формою для створення проєкту;
    |Менеджер|
    :Заповнює форму та натискає кнопку "Створити";
    |Система|
    :Перевіряє введені дані;
    note right #ffaaaa
    <b> Можливі помилки:
    <b> ProjectCreate_InvalidData
    end note
    :Створює новий проєкт;
    |Менеджер|
    stop;

@enduml

### ProjectUpdate

<table>
    <tr>
        <td><b>ID</b></td>
        <td><code>ProjectUpdate</code></td>
    </tr>
    <tr>
        <td><b>Назва:</b></td>
        <td>Редагування існуючого проєкту</td>
    </tr>
     <tr>
        <td><b>Учасники:</b></td>
        <td>Менеджер, система</td>
    </tr>
     <tr>
        <td><b>Передумови:</b></td>
        <td>
         Менеджер автентифікований у системі
        </td>
    </tr>
     <tr>
        <td><b>Результат:</b></td>
        <td>Існуючий проєкт відредаговано</td>
    </tr>
     <tr>
        <td><b>Виключні ситуації:</b></td>
        <td>
        - ProjectUpdateException_InvalidData - введені менеджером дані не коректні<br/>
        - ProjectUpdateException_Unauthorized - менеджер не має прав на редагування<br/>
        </td>
    </tr>
</table>

@startuml

    |Менеджер|
    start;
    :Обирає проєкт у розділі "Проєкти";
    :Натискає кнопку "Редагувати проєкт";
    |Система|
    :Відкриває вікно з формою для редагування проєкту;
    |Менеджер|
    :Заповнює форму та натискає кнопку "Редагувати";
    |Система|
    :Перевіряє введені дані;
    note right #ffaaaa
    <b> Можливі помилки:
    <b> ProjectUpdateException_InvalidData
    <b> ProjectUpdateException_Unauthorized
    end note
    :Зберігає зміни в проєкті;
    |Менеджер|
    stop;

@enduml

### ProjectDelete

<table>
    <tr>
        <td><b>ID</b></td>
        <td><code>ProjectDelete</code></td>
    </tr>
    <tr>
        <td><b>Назва:</b></td>
        <td>Видалення існуючого проєкту</td>
    </tr>
     <tr>
        <td><b>Учасники:</b></td>
        <td>Менеджер, система</td>
    </tr>
     <tr>
        <td><b>Передумови:</b></td>
        <td>
         Менеджер автентифікований у системі
        </td>
    </tr>
     <tr>
        <td><b>Результат:</b></td>
        <td>Існуючий проєкт видалено</td>
    </tr>
     <tr>
        <td><b>Виключні ситуації:</b></td>
        <td>
         ProjectDeleteException_Unauthorized - менеджер не має прав на видалення
        </td>
    </tr>
</table>

@startuml

    |Менеджер|
    start;
    :Обирає проєкт у розділі "Проєкти";
    :Натискає кнопку "Видалити проєкт";
    |Система|
    :Перевіряє права менеджера;
    note right #ffaaaa
    <b> Можливі помилки:
    <b> ProjectDeleteException_Unauthorized
    end note
    :Питає чи точно менеджер бажає видалити проєкт;
    |Менеджер|
    :Натискає кнопку "Видалити";
    |Система|
    :Видаляє проєкт;
    |Менеджер|
    stop;

@enduml

### UserAdd

<table>
    <tr>
        <td><b>ID</b></td>
        <td><code>UserAdd</code></td>
    </tr>
    <tr>
        <td><b>Назва:</b></td>
        <td>Додавання користувача до проєкту</td>
    </tr>
     <tr>
        <td><b>Учасники:</b></td>
        <td>Адміністратор, користувач, система</td>
    </tr>
     <tr>
        <td><b>Передумови:</b></td>
        <td>
         - Адміністратор автентифікований у системі<br/>
         - Користувач якого додають до проєкту існує<br/>
        </td>
    </tr>
     <tr>
        <td><b>Результат:</b></td>
        <td>До проєкту додано користувача</td>
    </tr>
     <tr>
        <td><b>Виключні ситуації:</b></td>
        <td>
        - UserAddException_InvalidData - введені адміністратором дані не коректні<br/>
        - UserAddException_Unauthorized - адміністратор не має прав на додавання користувача<br/>
        </td>
    </tr>
</table>

@startuml

    |Адміністратор|
    :Обирає проєкт у розділі "Проєкти";
    :Натискає кнопку "Додати користувача";
    |Система|
    :Відкриває вікно з полем для вводу імені користувача;
    |Адміністратор|
    :Заповнює поле та натискає кнопку "Додати";
    |Система|
    :Перевіряє введені дані;
    note right #ffaaaa
    <b> Можливі помилки:
    <b> UserAddException_InvalidData
    <b> UserAddException_Unauthorized
    end note
    :Додає нового користувача;
    |Адміністратор|
    stop;

@enduml

### UserDelete

<table>
    <tr>
        <td><b>ID</b></td>
        <td><code>UserDelete</code></td>
    </tr>
    <tr>
        <td><b>Назва:</b></td>
        <td>Видалення користувача з проєкту</td>
    </tr>
     <tr>
        <td><b>Учасники:</b></td>
        <td>Адміністратор, користувач, система</td>
    </tr>
     <tr>
        <td><b>Передумови:</b></td>
        <td>
         - Адміністратор автентифікований у системі<br/>
         - Користувач якого видаляють є в проєкті<br/>
        </td>
    </tr>
     <tr>
        <td><b>Результат:</b></td>
        <td>З проєкту видалено користувача</td>
    </tr>
     <tr>
        <td><b>Виключні ситуації:</b></td>
        <td>
        - UserDeleteException_InvalidData - введені адміністратором дані не коректні<br/>
        - UserDeleteException_Unauthorized - адміністратор не має прав на видалення користувача<br/>
        </td>
    </tr>
    <tr>
        <td><b>Основний сценарій:</b></td>
        <td>
            <ol>
                <li>Адміністратор обирає проєкт у розділі "Проєкти"</li>
                <li>Адміністратор обирає користувача у розділі "Користувачі"</li>
                <li>Адміністратор натискає кнопку "Видалити користувача"</li>
                <li>Система запитує чи менеджер дійсно хоче видалити користувача</li>
                <li>Адміністратор натискає кнопку "Видалити"</li>
                <li>Система перевіряє введені дані(UserDeleteException_InvalidData, UserDeleteException_Unauthorized)</li>
                <li>Система видаляє користувача з проєкту</li>
            </ol>
        </td>
    </tr>
</table>

@startuml

    |Адміністратор|
    :Обирає проєкт у розділі "Проєкти";
    :Обирає користувача у розділі "Користувачі";
    :Натискає кнопку "Видалити користувача";
    |Система|
    :Запитує чи менеджер дійсно хоче видалити користувача;
    |Адміністратор|
    :Натискає кнопку "Видалити";
    |Система|
    :Перевіряє введені дані;
    note right #ffaaaa
    <b> Можливі помилки:
    <b> UserDeleteException_InvalidData
    <b> UserDeleteException_Unauthorized
    end note
    :Видаляє користувача з проєкту;
    |Адміністратор|
    stop;

@enduml

### TaskAdd

<table>
    <tr>
        <td><b>ID</b></td>
        <td><code>TaskAdd</code></td>
    </tr>
    <tr>
        <td><b>Назва:</b></td>
        <td>Додавання задачі в проєкт</td>
    </tr>
     <tr>
        <td><b>Учасники:</b></td>
        <td>Менеджер, система</td>
    </tr>
     <tr>
        <td><b>Передумови:</b></td>
        <td>
         - Менеджер автентифікований у системі<br/>
         - Проєкт в який додають задачу існує<br/>
        </td>
    </tr>
     <tr>
        <td><b>Результат:</b></td>
        <td>В проєкт додано задачу</td>
    </tr>
     <tr>
        <td><b>Виключні ситуації:</b></td>
        <td>
        - TaskAddException_InvalidData - введені менеджером дані не коректні<br/>
        - TaskAddException_Unauthorized - менеджер не має прав на додавання задачі<br/>
        </td>
    </tr>
</table>

@startuml

    |Менеджер|
    start;
    :Обирає проєкт у розділі "Проєкти";
    :Натискає кнопку "Додати задачу";
    |Система|
    :Відкриває вікно з формою для додавання задачі;
    |Менеджер|
    :Заповнює форму та натискає кнопку "Додати";
    |Система|
    :Перевіряє введені дані;
    note right #ffaaaa
    <b> Можливі помилки:
    <b> TaskAddException_InvalidData
    <b> TaskAddException_Unauthorized
    end note
    :Додає задачу в проєкт;
    |Менеджер|
    stop;

@enduml

### TaskUpdate

<table>
    <tr>
        <td><b>ID</b></td>
        <td><code>TaskUpdate</code></td>
    </tr>
    <tr>
        <td><b>Назва:</b></td>
        <td>Редагування задачі в проєкті</td>
    </tr>
     <tr>
        <td><b>Учасники:</b></td>
        <td>Менеджер, система</td>
    </tr>
     <tr>
        <td><b>Передумови:</b></td>
        <td>
         - Менеджер автентифікований у системі<br/>
         - Проєкт в якому редагують задачу існує<br/>
        </td>
    </tr>
     <tr>
        <td><b>Результат:</b></td>
        <td>Задачу відредаговано</td>
    </tr>
     <tr>
        <td><b>Виключні ситуації:</b></td>
        <td>
         - TaskUpdateException_InvalidData - введені менеджером дані не коректні<br/>
         - TaskUpdateException_Unauthorized - менеджер не має прав на змінення задачі<br/>
        </td>
    </tr>
    <tr>
        <td><b>Основний сценарій:</b></td>
        <td>
            <ol>
                <li>Менеджер обирає проєкт у розділі "Проєкти"</li>
                <li>Менеджер обирає задачу у розділі "Задачі"</li>
                <li>Менеджер натискає кнопку "Редагувати"</li>
                <li>Система відкриває вікно з формою для редагування задачі</li>
                <li>Менеджер заповнює форму та натискає кнопку "Зберегти"</li>
                <li>Система перевіряє введені дані(TaskUpdateException_InvalidData, TaskUpdateException_Unauthorized)</li>
                <li>Система змінює задачу</li>
            </ol>
        </td>
    </tr>
</table>

@startuml

    |Менеджер|
    start;
    :Обирає проєкт у розділі "Проєкти";
    :обирає задачу у розділі "Задачі";
    :натискає кнопку "Редагувати";
    
    |Система|
    :Відкриває вікно з формою для редагування задачі;
    
    |Менеджер|
    :Заповнює форму та натискає кнопку "Зберегти";
    
    |Система|
    :Перевіряє введені дані;
    note right #ffaaaa
    <b> Можливі помилки:
    <b> TaskUpdateException_InvalidData
    <b> TaskUpdateException_Unauthorized
    end note
    :Система змінює задачу;

    |Менеджер|
    stop;

@enduml

### TaskDelete

<table>
    <tr>
        <td><b>ID</b></td>
        <td><code>TaskDelete</code></td>
    </tr>
    <tr>
        <td><b>Назва:</b></td>
        <td>Видалення задачі з проєкту</td>
    </tr>
     <tr>
        <td><b>Учасники:</b></td>
        <td>Менеджер, система</td>
    </tr>
     <tr>
        <td><b>Передумови:</b></td>
        <td>
         - Менеджер автентифікований у системі<br/>
         - Проєкт з якого видаляють задачу існує<br/>
        </td>
    </tr>
     <tr>
        <td><b>Результат:</b></td>
        <td>Задачу видалено</td>
    </tr>
     <tr>
        <td><b>Виключні ситуації:</b></td>
        <td>
         TaskDeleteException_Unauthorized - менеджер не має прав на видалення задачі
        </td>
    </tr>
    <tr>
        <td><b>Основний сценарій:</b></td>
        <td>
            <ol>
                <li>Менеджер обирає проєкт у розділі "Проєкти"</li>
                <li>Менеджер обирає задачу у розділі "Задачі"</li>
                <li>Менеджер натискає кнопку "Видалити"</li>
                <li>Система запитує менеджера чи точно він хоче видалити задачу</li>
                <li>Менеджер натискає кнопку "Видалити"</li>
                <li>Система перевіряє права доступу(TaskDeleteException_Unauthorized)</li>
                <li>Система видаляє задачу</li>
            </ol>
        </td>
    </tr>
</table>

@startuml

    |Менеджер|
    start;
    :Обирає проєкт у розділі "Проєкти";
    :обирає задачу у розділі "Задачі";
    :натискає кнопку "Видалити";
    
    |Система|
    :Запитує менеджера чи точно він хоче видалити задачу;
    
    |Менеджер|
    :Натискає кнопку "Видалити";
    
    |Система|
    :Перевіряє права доступу;
    note right #ffaaaa
    <b> Можливі помилки:
    <b> TaskDeleteException_Unauthorized
    end note
    :Система видаляє задачу;

    |Менеджер|
    stop;

@enduml

### Support

<table>
    <tr>
        <td><b>ID</b></td>
        <td><code>Support</code></td>
    </tr>
    <tr>
        <td><b>Назва:</b></td>
        <td>Зв'язок з службою підтримки</td>
    </tr>
     <tr>
        <td><b>Учасники:</b></td>
        <td>Користувач, система</td>
    </tr>
     <tr>
        <td><b>Передумови:</b></td>
        <td>
         Користувач автентифікований у системі
        </td>
    </tr>
     <tr>
        <td><b>Результат:</b></td>
        <td>Користувач надіслав запит до служби підтримки</td>
    </tr>
     <tr>
        <td><b>Виключні ситуації:</b></td>
        <td></td>
    </tr>
    <tr>
        <td><b>Основний сценарій:</b></td>
        <td>
            <ol>
                <li>Користувач натискає кнопку "Зв'язатися зі службою підтримки"</li>
                <li>Система відкриває форму для зв'язку зі службою підтримки</li>
                <li>Користувач заповнює форму та натискає кнопку "Надіслати"</li>
            </ol>
        </td>
    </tr>
</table>

@startuml

    |Користувач|
    start;
    :Натискає кнопку "Зв'язатися зі службою підтримки";
    
    |Система|
    :Відкриває форму для зв'язку зі службою підтримки;

    |Користувач|
    :Заповнює форму та натискає кнопку "Надіслати";

    |Користувач|
    stop;

@enduml

</center>

