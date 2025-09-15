def main():
    songs = ["Blinding Lights","Levitating","As It Was","Heat Waves","Good 4 u"]
    
    songs.append("Good for u")
    songs.insert(0, "Bohemian Rhapsody")
    songs.remove("Good for u")
    print(songs.index("Levitating"))
    print(songs.count())
