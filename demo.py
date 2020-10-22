movie_num = int(input())
movie_name = ''
movie_rating = 0
rating = []
movie = []
max_name = ''
min_name = ''
total = 0


for i in range(0, movie_num):

    movie_name = input()
    movie_rating = float(input())

    movie.append(movie_name)
    rating.append(movie_rating)

    if movie_rating == max(rating):
        max_name = movie_name
    elif movie_rating == min(rating):
        min_name = movie_name

    total += movie_rating

print(f'{max_name} is with highest rating: {max(rating):.1f}')
print(f'{min_name} is with lowest rating: {min(rating):.1f}')
print(f'Average rating: {(total / movie_num):.1f}')

