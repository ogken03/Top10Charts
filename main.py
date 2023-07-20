import billboard
def get_top_songs(billboardChoice):
    chart = billboard.ChartData(billboardChoice)

    top_10_songs = []
    for entry in chart[:10]:
        song_name = entry.title
        artist_name = entry.artist

        top_10_songs.append({"song": song_name, "artist": artist_name})

    return top_10_songs

if __name__ == "__main__":
    choice = int(input("Enter the number that correlates to your choice \n1.'hot-100' \n2.'billboard-200' \n3.'billboard-global-200' \nChoice: "))
    result = ""
    if choice == 1:
        result = "hot-100"
    elif choice == 2:
        result = 'billboard-200'
    elif choice == 3:
        result = 'billboard-global-200'

    top_songs = get_top_songs(result)
    if top_songs:
        print("\nTop 10 songs of " + result + ": ")
        for idx, song_info in enumerate(top_songs, 1):
            print(f"{idx}. {song_info['song']} - {song_info['artist']}")
    else:
        print("Something Went Wrong")
