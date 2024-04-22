# Movie Matchmaker!

Have you ever been sitting in your living room with freshly popped popcorn, only to realize you aren't sure what movie to watch? Movie Matchmaker is here to match you with YOUR ideal movie. Just enter a few of your favorite movies, actors, etc and we will determine which movies are the best fit for you!

In order to implement this, we used both the Graph and Heap data structures. We devised algorithms that utilized these data structures to determine a "similarity score" which was used to determine which movie is the most similar to the preferences entered by the user. After these algorithms run their course, the program will return the number of movies that the user requests to be generated!



## Authors

- Chloe Bai [@chloe-bai](https://www.github.com/chloe-bai)
- Nora Choukri [@norachoukri](https://www.github.com/norachoukri)
- Anna Hudson [@annahudson356](https://www.github.com/annahudson356)

## Run Instructions

### In order to use Movie MatchMaker to make your movie night smoother, please use the following steps to make sure that the program runs smoothly!
1. Download the Repository by clicking the Green Code<> button at the top right of the repository and pressing "Download Zip"
2. Once you have the file saved to the directory of your choice, extract the file and open Terminal
3. Make sure you have Python installed on your machine. Check this by typing the command 'python.' If this works, you should see the terminal change to >>>, type exit() to return back to the normal Terminal
4. Navigate to the folder containing the Python files, and type in the following command 'py .\MovieMatchmaker.py'
5. Enjoy your moviewatching experience!

## How it Works

#### Similarity Score:
After you input your ideal movie characteristics, an algorithm runs that gives each movie a similarity score. This score is out of 20 and assigns points based on certain attributes, such as length, star actor, rating, and genre. Each element is given a certain weight, i.e. actor is more important than the length of the movie, and we then use this information to output the movie that is most similar to the attributes that the you input!

#### Data Structures:
We used both a Heap and a Graph data structure to implement this. The Heap works by using a Max-Heap implementation to store the movie with the highest similarity score at the top. In order to get the highest similarity scores to return to the user, we extract the max from the heap and reorganize it to allow us to constantly get the highest similarity score movies. For the Graph, we used the ideal movie as a vertex and used weighted edges to connect movies that were the most similar to each other. The algorithm then checks these edges and prioritizes the movies with the edges with the highest similarity scores to return the optimal movies to the user.

#### Data
We used a dataset from Kaggle, specifically the 'Movie Industry' Data Set. This dataset can be found at the following link: https://www.kaggle.com/datasets/danielgrijalvas/movies

