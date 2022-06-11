import csv

with open('musicdatabase/data/smallmusic.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)

    print("[1] Song")
    print("[2] Artist")
    print("[3] Genre")
    print("[4] Year")
    print("[5] Decade")
    print("[6] Topic")
    print("[7] Location\n")

    choice = input("What do you want to do today? : ")

    # songs by search
    if choice == '1':
        print("[a] Search song by title")
        print("[b] By substring")
        print("[c] Print all songs and the artist")

        song_choices = input("a b or c: ")

        if song_choices == 'a':
            title_choice = input("What song are you looking for? : ")
            for row in reader:
                if row[0] == title_choice:
                    print(row[0], row[1], row[2], row[3], row[5])

        if song_choices == 'b':
            substring_choice = input("What word are you looking for in a song title? : ")
            for row in reader:
                if substring_choice in row[0]:
                    print(row[0],"by",row[1])
                    
        if song_choices == 'c':
            mapping = {}
            for row in reader:
                mapping[row[0]] = row[1]
            print(mapping) # TODO




    # songs by artist
    if choice == '2':
        print("[a] Search songs by this artist")
        print("[b] Search albums by this artist")
        print("[c] Print artists")

        artist_choice = input("a b or c? : ")
        if artist_choice == 'a':
            search_songs = input("What artist do you need songs from? : ")
            for row in reader:
                if search_songs == row[1]:
                    print(row[0], ",", row[2], row[3])

        if artist_choice == 'b':
            search_albums = input("What artist do you need albums from? : ")
            for row in reader:
                if search_albums == row[1]:
                    print(row[2], row[3])

        if artist_choice == 'c':
            mapping = {}

            for row in reader:
                mapping.add(row[1])
            print(mapping)




    # songs by genre
    if choice == '3':
        print("[a] Songs by this genre")
        print("[b] Artists by this genre")
        print("[c] Filter songs by genre with a specific Topic")
        print("[d] Genre and Year")
        print("[e] Genre and Decade")
        print("[f] Print Genres")

        genre_choice = input("a b c d e or f? :")

        if genre_choice == 'a':
            search_songs = input("What genre are you searching for songs from? : ")
            for row in reader:
                if row[5] == search_songs:
                    print(row[0], row[1])
                
        if genre_choice == 'b':
            search_artists = input("What genre are you searching for artists from? : ")
            mapping = {}
            for row in reader:
                if row[5] == search_artists:
                    mapping.add(row[1])
            print(mapping)

        if genre_choice == 'c':
            search_genre = input("What genre are you searching for? : ")
            search_topic = input("What topic are you looking for? : ")

            for row in reader:
                if row[5] == search_genre and row[6] == search_topic:
                    print(row[0], row[1])

        if genre_choice == 'd':
            search_genre = input("What genre are you searching for? : ")
            search_year = input("What year are you looking for music from? : ")

            for row in reader:
                if row[5] == search_genre and row[3] == search_year:
                    print(row[0], row[1])

        if genre_choice == 'e':
            search_genre = input("What genre are you searching for? : ")
            search_decade = input("What decade are you looking for music from? : ")

            for row in reader:
                if row[5] == search_genre and row[4] == search_decade:
                    print(row[0], row[1])

        if genre_choice == 'f':
            mapping = {}
            for row in reader:
                mapping.add(row[5])
            print(mapping)


    if choice == '4':
        print("[a] Who made music this Year")
        print("[b] What songs were made this Year")
        print("[c] Print Years")

        year_choice = input("a b or c? : ")

        if year_choice == 'a':
            year_input = input("What year do you need artists from? : ")
            mapping = {}
            for row in reader:
                if row[3] == year_input:
                    mapping.add(row[1])
            print(mapping)

        if year_choice == 'b':
            year_input = input("What year do you need songs from? : ")
            for row in reader:
                if row[3] == year_input:
                    print(row[0], "by", row[1])

        if year_choice == 'c':
            mapping = {}
            for row in reader:
                mapping.add(row[3])

            print(mapping)

    if choice == '5':
        print("[a] Artists this Decade")
        print("[b] Songs this Decade")
        print("[c] Print Decades")

        decade_choice = input("a b or c? : ")

        if decade_choice == 'a':
            decade_input = input("What decade do you need artists from? : ")
            
            mapping = {}
            for row in reader:
                if row[4] == decade_input:
                    mapping.add(row[4])
            print(mapping)


        if decade_choice == 'b':
            decade_input = input("What decade do you need songs from? : ")
            for row in reader:
                if row[4] == decade_input:
                    print(row[0], "by", row[1])
        

        if decade_choice == 'c':
            mapping = {}
            for row in reader:
                mapping.add(row[4])
        
            print(mapping)



    if choice == '6':
        print("[a] Give me songs that fit this Topic")
        print("[b] Give me artists that make songs like this")
        print("[c] Print all topics")


        topic_choice = input("a or b? : ")

        if topic_choice == 'a':
            topic_input = input("What topic are you searching songs for? : ")

            for row in reader:
                if row[6] == topic_input:
                    print(row[0], "by", row[1])

        if topic_choice == 'b':
            mapping = {}

            topic_input = input("What topic are you searching songs for? : ")

            for row in reader:
                if row[6] == topic_input:
                    mapping.add(row[1])

            print(mapping)


        if topic_choice == 'c':
            mapping = {}

            for row in reader:
                mapping.add(row[6])
            print(mapping)

    if choice == '7':
        print("[a] Give me all songs that I can find here (ex. YouTube)")
        print("[b] Songs not on all platforms")
        print("[c] Print Locations")

        location_choice = input("a b or c? : ")

        if location_choice == 'a':
            location_input = input("Where are you looking for songs from? : ")
            for row in reader:
                if row[7] == location_input or row[7] == "All":
                    print(row[0], "by", row[1])

        if location_choice == 'b':
            for row in reader:
                if row[7] != "All":
                    print(row[0], "by", row[1], ": on", row[7])


        if location_choice == 'c':
            mapping = {}

            for row in reader:
                mapping.add(row[7])

            print(mapping)