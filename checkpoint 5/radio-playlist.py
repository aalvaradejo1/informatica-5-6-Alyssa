def main():
    songs = ["Blinding Lights","Levitating","As It Was","Heat Waves","Good 4 u"]
    

    
    songs.append("Drivers license")
    songs.insert(0, "Bohemian Rhapsody")
    songs.remove("Good for u")
    songs.index("Levitating")
    print(songs)
    songs.count("As it was")
    print(songs)
    songs.reverse()
    print(songs)
    songs.sort()
    print(songs)
    
    playlist = songs

    print(playlist)

main()