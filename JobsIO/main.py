from jobs_io.search import Search
import jobs_io.openxl as osx

if __name__ == "__main__":
    
    new_search = Search("wfh customer service")
    results = new_search.search()

    osx.add_to_workbook(results)