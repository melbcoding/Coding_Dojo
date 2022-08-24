Prework 
build out flask structure


1) 5 Templates 
    a) log & reg
    b) view all - 
         *need to get current user with their recipes
            SELECT *
            FROM users
            LEFT JOIN recipes
            ON users.id = recipes.user_id
            WHERE users.id = %(id)s;


         *need to get all recipes
           select * from recipes;

    c) view one
    d) edit
    e) add one

2) Create EER Diagram with relationships and keys
   table users
    columns ....
    table recipes 
    columns...

3) SQL Queries 
    Insert
    Update
    Delete
    Select one or all
    *many to many 

4) build Models to controllers to the Templates