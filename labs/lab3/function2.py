movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def good_movie(name):
    for i in movies:
        if i["name"]==name:
            return i["imdb"]>5.5
        
print(good_movie("We Two"))

#2
def list_good_movies():
    ans = []
    for i in movies:
        if i["imdb"]>5.5:
            ans.append(i["name"])
    return ans

print(*list_good_movies())

#3
def task3(category_name):
    ans = []
    for i in movies:
        if i["category"] == category_name:
            ans.append(i["name"])
    return ans

print(task3("Romance"))

#4
def avg_ranking(movie_list):
    l = len(movie_list)
    s = 0
    for i in movie_list:
        for j in movies:
            if j["name"]==i:
                s+=j["imdb"]
                break
    return s/l

print(avg_ranking(['The Choice', 'Colonia', 'Love', 'Bride Wars', 'We Two']))

#5
def avg_category(category_name):
    return avg_ranking(task3(category_name))

print(avg_category("Romance"))