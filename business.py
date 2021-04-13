import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    print(df['movies'].tolist())

    movies       = df['movies'].tolist()

    score        = df['score'].tolist()


    # print(df['quebec'].tolist())

    result_dict = {
        'movies'            : movies,
        'score'            : score,
    }

    # print(result_dict)

    return result_dict

def add_row(movies,score):

    df = pd.read_csv('data.csv') 

    new_row = {
    
        'movies'       : movies, 
        'score'       :  score, 
        
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('data.csv')

if __name__ == "__main__":
    get_data()