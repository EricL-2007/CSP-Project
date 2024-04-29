def input_songs():
    """
    Asks the user to input multiple songs and stores them in a list.
    
    Returns:
        list: A list containing the inputted songs.
    """
    songs = []
    while True:
        song = input("Enter a song (or type 'done' to finish): ")
        if song.lower() == 'done':
            break
        songs.append(song)
    return songs

def rank_songs(songs):
    """
    Asks the user to rank each song out of 10.
    
    Parameters:
        songs (list): A list of songs to be ranked.
        
    Returns:
        dict: A dictionary where each song is paired with its ranking.
    """
    ranked_songs = {}
    for song in songs:
        rating = input(f"How much do you like '{song}'? Rate it from 1 to 10: ")
        while not rating.isdigit() or int(rating) < 1 or int(rating) > 10:
            rating = input("Please enter a number from 1 to 10: ")
        ranked_songs[song] = int(rating)
    return ranked_songs

def display_sorted_songs(ranked_songs):
    """
    Displays the final list of songs sorted by rating and alphabetically.
    
    Parameters:
        ranked_songs (dict): A dictionary where each song is paired with its ranking.
    """
    unique_ratings = sorted(set(ranked_songs.values()), reverse=True)
    for rating in unique_ratings:
        print(f"Songs rated {rating}:")
        sorted_songs = sorted([song for song, r in ranked_songs.items() if r == rating])
        for song in sorted_songs:
            print(song)
        print('-' * 20)

def main():
    """
    Executes the program.
    """
    print("Welcome to the song ranking program!")
    print("Please enter the songs you'd like to rank:")
    songs = input_songs()
    print("\nNow, let's rank each song from 1 to 10:")
    ranked_songs = rank_songs(songs)
    print("\nThank you for ranking the songs! Here are the results:")
    display_sorted_songs(ranked_songs)

if __name__ == "__main__":
    main()