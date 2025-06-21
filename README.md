# LAB_LISTS_TUPLES

## Cinema Booking Program
Create A small cinema program that uses a basic system to track **booked seats** for each show. Each booked seat is represented as a **tuple** of the form `(row_number, seat_number)`, and the full booking list is a **list of these tuples**.

---

### **Description**

You are given a list of booked seats for a movie show. Each seat is represented as a tuple `(row, seat)` where:

* `row` is an integer from 1 to 10
* `seat` is an integer from 1 to 20

Example:

```python
booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]
```

Write a program that performs the following tasks:

---

### **Tasks**

1. **Display all booked seats** in the format:

   ```
   Row 1, Seat 5  
   Row 1, Seat 6  
   ...
   ```

2. **Check availability:** Ask the user to enter a seat (e.g., row 2, seat 10), and tell them whether the seat is **booked** or **available**.

3. **Add a booking:** ask the user to enter the seat, row . if available, add it to the `booked_seats` list. else display a relevant message.

4. **Cancel a booking:** Ask the user to enter a row & a seat to cancel. If it's in the list, remove it.

5. **Print all booked seats, sorted by row and then seat**.

6. **Calculate and display**:

   * Total number of booked seats
   * Number of seats booked per row (use a list of counts for each row index 0–9)

### Note:
The program when run should run and displays a menu that asks the user what he/she wants to do based on the above tasks, and only exits if the user types in "exit".

---

### **Constraints**

* Use only **lists and tuples**.


# Bonus

## Movie Ratings Analysis

Scenario:
You have just been hired as a data analyst at a movie streaming platform. Your manager has given you a list of movies, each with a tuple containing the movie title, release year, and user ratings. The platform allows users to rate movies on a scale of 1 to 10. Your manager wants you to create a Python program that:

1. Accepts a list of movies, with each movie represented as a tuple containing the movie title, release year, and a list of user ratings.
2. Calculates the average rating for each movie.
3. Filters out movies with an average rating lower than 6.0.
5. Displays the  movies, along with their title, release year, and average rating.

Example input:
```
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
```

Expected output:
```
1. The Shawshank Redemption (1994) - Avergae rating: 9.17 ★
2. The Godfather (1972) - Avergae rating: 8.83 ★
3. The Dark Knight (2008) - Avergae rating: 8.83 ★
4. Schindler's List (1993) - Avergae rating: 7.83 ★
5. Pulp Fiction (1994) - Avergae rating: 7.17 ★
```

**Challenge: Display the movies sorted by the average rating.**
