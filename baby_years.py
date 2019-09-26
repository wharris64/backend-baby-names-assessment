import re 
string1 = "a string that doesn't include what we need"
string2 = "a string that happens to include Popularity in 1980"
def extract_year(s):
    
    
    year = re.findall(r'Popularity\sin\s(\d\d\d\d)', s)
    return year
    


def main():
    print(extract_year(string1))
    print(extract_year(string2))

    

if __name__ == '__main__':
        main()