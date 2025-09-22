book_points = 0
movie_points = 0


answer = input ("do you have A) a short attention span, or B) have a long attention span?")
if answer == "A":
    movie_points += 1
elif answer == "B":
    book_points += 1


answer = input ("are you a A) a visual learner, or B) a auditory learners?")
if answer == "A":
    movie_points += 1
elif answer == "B":
    book_points += 1


answer = input ("do you like A) dark chocolate, or B) milk chocolate?")
if answer == "A":
    book_points += 1
elif answer == "B":
    movie_points += 1


answer = input ("do you like A) primary color wheel or B) black and white color scale")
if answer == "A":
    movie_points += 1
elif answer == "B":
    book_points += 1


answer = input ("are you energetic A) no or B) yes")
if answer == "A":
    book_points += 1
elif answer == "B":
    movie_points += 1

print (f"movie points = {movie_points}")
print (f"book_points = {book_points}")
# end of quiz
if book_points > movie_points:
    print ("You are a book person")
elif movie_points > book_points:
    print (" You are a movie person")
