# UG_DBST2VO Exercise2.1

##Exercise 1: Play around with sqlite (2)
Complete the Exercise 2 from the previous lecture (install sqlite, write code to create a database, write a code to connect to a database)

-create a folder session2

-inside the session2 folder create a module test_session2.py

-inside the test_session2.py module write a test that

-creates a database test-db.db
-table Professor with attributes PersNr (int), FirstName (string/varchar), and LastName (string/varchar)
-insert the professor (123, Foo, Bar)
-insert the same professor (123, Foo, Bar) again
-assert that the second query fail
Can you make the test fail?

Fix the previous test to make the assertion fail (hint, define a PRIMARY KEY)

-write another test that

-connect to test-db.db
-create a second professor (234, Donald, Duck)
-check that the Professor contains two entries one for (123, Foo, Bar) and one for (234, Donald, Duck). Note the order does not matter
What's the issue with those test cases?
