--Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.
select * from tasks 
where user_id = 10;

--Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
select tasks.title from tasks LEFT JOIN status
on TASKS.status_id=status.id  
where status.name = 'new';

--Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
update tasks
set status_id = 2
where id =1

select * from tasks;

--Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
select fullname
FROM users
WHERE id NOT IN (SELECT user_id FROM tasks);

--Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
insert into tasks (id, title, description, status_id, user_id)
values (31, 'texts about life science', 'tralialia', 1, '17')

select * from tasks;

--Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.
--select tasks.title, tasks.description, status.name  from tasks LEFT JOIN status 
--on TASKS.status_id=status.id
--where status.name not like 'completed';
SELECT title, description 
FROM tasks
WHERE status_id <> (SELECT id FROM status WHERE name = 'completed');

--Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
DELETE from tasks where id=31;

--Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
select * from users
where email like '%example.com';

--Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
update users
set fullname  = 'Kelly Stark2'
where fullname ='Kelly Stark'

select * from users;

--Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
--select tasks.title, tasks.description, status.name  from tasks LEFT JOIN status 
select  status.name, count(*)  from tasks LEFT JOIN status
on TASKS.status_id=status.id
group by status.name;

--Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою 
--LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
select  users.fullname, tasks.title, tasks.description, users.email  from tasks LEFT JOIN users
on tasks.user_id=users.id
where email like '%example.com';

--Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
select * from tasks 
WHERE description IS NULL
   OR description = '';

--Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх 
--завдань із певним статусом.
select  users.fullname, tasks.title, tasks.description, tasks.status_id from tasks inner JOIN users
on tasks.user_id=users.id
where tasks.status_id = 2;

--Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
select  users.fullname, count(*)  from tasks LEFT JOIN users
on tasks.user_id=users.id
group by users.fullname;