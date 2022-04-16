def parse_chapters(text):
    lines = text.split('\n')
    result = []
    chapter_count = 0
    section_count = 0
    #print(lines)
    for line in lines:
        line = line.lstrip()
        if len(line) < 2:
            continue
        elif line[0:2] == '##':
            #this is section
            section_count += 1
            result.append(f'{chapter_count}.{section_count}. {line[2:]}')
        elif line[0] == '#':
            # this is chapter
            chapter_count += 1
            section_count = 0
            result.append(f'{chapter_count}. {line[1:]}')
        else:
            # this is regular section content, ignore
            pass

    return "\n".join(result)


text = """#Algorithms
    This chapter covers the most basic algorithms.
    ## Sorting
    Quicksort is fast and widely used in practice
    Merge sort is a deterministic algorithm
    ## Searching
    DFS and BFS are widely used graph searching algorithms
    Some variants of DFS are also used in game theory
    # Data Structures
    This chapter is all about data structures
    It's a draft for now and will contain more sections in the
    future
    # Binary Search Trees
"""
print(parse_chapters(text))

