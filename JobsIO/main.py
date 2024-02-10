from jobs_io.search import Search

if __name__ == "__main__":
    
    new_search = Search("wfh")
    results = new_search.search()

    for result in results:
        print(result)