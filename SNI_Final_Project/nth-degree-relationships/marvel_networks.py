import time


def setup():
    # Reads in the file with all
    # character information
    in_file = open("marvel_info.txt", "r")
    # 1 - 6486: Characters
    # 6486 - 19428: Comics
    # All remaining lines: character - comics they are in

    val = in_file.readline().split()
    num_characters = int(val[2])
    num_char_comics = int(val[1]) - num_characters
    names = []
    comics_characters = {}

    # Put all the character names in the names array
    print("Reading in character names...")
    start_time = time.time()
    for i in range(num_characters):
        val = in_file.readline().split()
        name = " "
        for j in range(1, len(val)):
            name += val[j] + " "
        names.append(name)
    end_time = "--- %s seconds ---" % (time.time() - start_time)
    print(end_time)

    # Put the comic books in the dictionary of arrays
    # where the key is number associated with the
    # comic book and the values will be a list
    # of all the characters in that comic
    print("Reading in comic book names & setting up dictionary...")
    start_time = time.time()
    for i in range(num_char_comics):
        val = in_file.readline().split()
        name = " "
        for j in range(len(val) - 1):
            name += val[j + 1] + " "
        names.append(name)
        comics_characters[int(val[0])] = []
    val = in_file.readline().split()
    end_time = "--- %s seconds ---" % (time.time() - start_time)
    print(end_time)

    # Fill the list in the dictionary with the
    # characters in each comic book
    print("Filling the dictionary with characters in each comic...")
    start_time = time.time()
    while len(val) is not 0:
        val = in_file.readline().split()
        for i in range(1, len(val)):
            comics_characters[int(val[i])].append(int(val[0]))
    end_time = "--- %s seconds ---" % (time.time() - start_time)
    print(end_time)

    return num_characters, names, comics_characters


def fill_zeros(_names, _num_characters, _character_character):
    print("\n---Network analysis for" + names[character] + "---\n")

    # Fill the relational matrix with zeros
    print("Setting up the relational matrix...")
    start_time = time.time()
    for i in range(_num_characters):
        for j in range(_num_characters):
            _character_character[0][i].append(0)
    end_time = "--- %s seconds ---" % (time.time() - start_time)
    print(end_time)

    return character_character


def initialize_matrix(_comics_characters, _character_character):
    # Set the relational matrix by making a copy of
    # each comics character list and setting each
    # index at character1 x character2 to 1 for a
    # degree 1 relationship between them or in other
    # words they are in a comic book together. This
    # be done by distributing the character lists
    print("Setting the relational matrix...")
    start_time = time.time()
    for c in _comics_characters:
        for i in _comics_characters[c]:
            for j in _comics_characters[c]:
                if j is not i:
                    _character_character[0][i - 1][j - 1] = 1
    end_time = "--- %s seconds ---" % (time.time() - start_time)
    print(end_time)

    return _comics_characters, _character_character


def matrix_mul(_character, _depth,  _names, _num_characters, _character_character, _relationships):
    # Now that the relational matrix has been set
    # we can begin squaring the matrix to get the
    # desired relations.
    # Squaring the matrix (^2) will leave us with
    # all two edge paths to and from each
    # character. Similarly the matrix to the nth
    # power will leave us with all n edge paths
    # to and from each character.

    # the column we will use for the first matrix
    # because the matrix is n x p. All following
    # matrices for spider man number 2-4 will be
    # n x 1, thus the column we will look at is
    # column 0 for those matrices. The variable
    # character will will determine which
    # character we base the relation on.
    # The variable depth will be used to
    # determine the degree of relation we are
    # looking for plus one.
    character_ = _character
    for m in range(_depth):
        print("Squaring matrix (" + _names[_character] + "number of " + str(m + 2) + ")...")
        start_time = time.time()
        for i in range(_num_characters):
            for j in range(1):
                sum_ = 0
                for k in range(_num_characters):
                    sum_ += _character_character[0][i][k] * _character_character[m][k][character_]
                _character_character[m + 1][i].append(sum_)
        character_ = 0
        _relationships.append(0)
        end_time = "--- %s seconds ---" % (time.time() - start_time)
        print(end_time)

    return _character_character, _relationships


def find_relationships(_relationships, _character, _character_character):
    # For every power of the matrix check how
    # many characters have a relationship
    # with the character we are looking at
    # and collect data on relationships
    # to print to file
    rel_for_file = []
    relationships.append(0)
    character_ = character
    for i in range(len(relationships)):
        rel_for_file.append(set())
        for j in range(len(character_character[i])):
            if character_character[i][j][character_] is not 0:
                relationships[i] += 1
                rel = f"{names[character]}-{names[j]}"
                rel_for_file[i].add(str(rel))

        character_ = 0

    return rel_for_file


def write_to_file(_rel_for_file):
    # Writes the relationships to file
    # by using sets to store them. We
    # take the difference of each set
    # to determine what the
    # relationships are for each degree
    file_name = str(names[character]).replace('\"', '').replace(' ', '').replace('/', '_').replace('\\', '_')
    with open(f"{file_name}.txt", 'w') as outfile:
        for i in range(len(rel_for_file)):
            outfile.write(f" ---- Relationships of Degree: {i + 1} ----\n")
            if i > 0:
                diff = rel_for_file[i].difference(rel_for_file[i - 1])
            else:
                diff = rel_for_file[i]
            for r in diff:
                outfile.write(f"{r}\n")


if __name__ == "__main__":
    num_characters, names, comics_characters = setup()

    while True:
        option = input("\nMenu\n1) See all characters and their number\n2) Check a characters network\ne) Exit\n")

        if option[0] == '1':
            for i in range(num_characters):
                print(str(i + 1) + " :" + names[i])

        elif option[0] == '2':
            character = int(input("Enter the character number you want to check a relationship for "
                                  "(ie. 5306 for Peter Parker's Spider-man):\n")) - 1
            depth = int(input("Enter the degree of relationships you would like to see:\n")) - 1
            character_character = [[[] for i in range(num_characters)] for j in range(depth + 1)]
            relationships = []

            character_character = fill_zeros(names, num_characters, character_character)
            comics_characters, character_character = initialize_matrix(comics_characters, character_character)
            character_character, relationship = matrix_mul(character, depth,  names, num_characters, character_character, relationships)
            rel_for_file = find_relationships(relationships, character, character_character)
            write_to_file(rel_for_file)

            print("There are " + str(1) + " characters with " + names[character] + " number of 0.")
            print("There are " + str(relationships[0]) + " characters with " + names[character] + " number of 1.")
            for i in range(1, len(relationships)):
                print("There are " + str(relationships[i] - relationships[i - 1])
                      + " characters with " + names[character] + " number of " + str(i + 1) + ".")
            relationships.clear()
            character_character.clear()
            rel_for_file.clear()

        elif option[0] == 'e' or option[0] == 'E':
            exit(0)

        else:
            print("Enter a valid option...")
