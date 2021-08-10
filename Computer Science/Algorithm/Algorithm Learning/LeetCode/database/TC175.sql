-- Write your MySQL query statement below

-- select Person.FirstName,
--        Person.LastName,
--        Address.City,
--        Address.State
-- from Person,
--      Address
-- where Person.PersonId = Address.PersonId

select Person.FirstName, Person.LastName, Address.City, Address.State
from Person
         left join Address on Person.PersonId = Address.PersonId