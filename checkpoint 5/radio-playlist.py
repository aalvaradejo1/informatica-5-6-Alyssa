def main():
    songs = ["Blinding Lights","Levitating","As It Was","Heat Waves","Good 4 u"]

    songs.append("Drivers license")
    songs.insert(0, "Bohemian Rhapsody")
    songs.remove("Good 4 u")

    print(songs.index("Levitating"))
    print(songs.count("As it was"))
    
    playlist = songs

    songs.reverse()
    print(songs)
    songs.sort()
    print(songs)
    
    

    
main()