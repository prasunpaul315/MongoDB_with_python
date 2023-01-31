# MongoDB_with_python

Works only the following SQL commands
1. SELECT * FROM GRADE
2. SELECT SCORES FROM GRADE WHERE STUDENT_ID = <ANY-VALID-STUDENT_ID>
3. SELECT STUDENT_ID AS _id, COUNT(STUDENT_ID) AS Total Count FROM GRADE GROUP BY STUDENT_ID
4. (continuing for other query)

After successfully executing the python file the output stores inside the test.csv

We can give the input(SQL Query) by command line argument while executing the python file.
