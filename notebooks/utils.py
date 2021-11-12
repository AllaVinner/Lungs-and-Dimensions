





def centralize(dataframe, columns):
    centralized_df = dataframe.copy()
    centralized_df[columns]= centralized_df[columns] - dataframe[columns].mean()
    return centralized_df 


def normalize(dataframe, columns):
    normalized_df = dataframe.copy()
    normalized_df[columns] =     (normalized_df[columns] - dataframe[columns].mean())/dataframe[columns].std()
    return normalized_df




def get_column_categories():
    # Outputs a directory which stores different combinations of columns that could be
    # of intrest from the csv file '../data/WDBV.csv'.
    columns = {}
    columns['all'] = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst', 'Unnamed: 32']
    
    columns['mean'] = [col for col in columns['all'] if '_mean' in col]
    columns['se'] = [col for col in columns['all'] if '_se' in col]
    columns['worst'] = [col for col in columns['all'] if '_worst' in col] 
    columns['numerical'] = columns['mean'] + columns['se'] + columns['worst']

    measures = ['radius', 'texture', 'perimeter',
           'area', 'smoothness', 'compactness', 'concavity',
            'concave points', 'symmetry', 'fractal_dimension']
    for measure in measures:
        columns[measure] = [col for col in columns['all'] if measure in col]

    columns['id'] = ['id']
    columns['diagnosis'] = ['diagnosis']
    return columns 