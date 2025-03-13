import pandas as pd

def frequency_table(dataframe, column, frequency_column= False):
    '''
    This function can be used when we need to create a frequency table for categorical features:

    Parameters
    -----------
    dataframe: pd.DataFrame
        Dataframe with data.
    columns: srt
        Categorical column name.
    frequency_column: bool
        indicate if your column is already a frequency column. Std= False
    
    Returns
    --------
        pd.Dataframe with frequency table.
    '''
    df_frequency = pd.DataFrame()

    if frequency_column:
        df_frequency['frequency'] = dataframe[column]
        df_frequency['relative_frequency'] = df_frequency['frequency'] / df_frequency['frequency'].sum()
    else:
        df_frequency['frequency'] = dataframe[column].value_counts().sort_index()
        df_frequency['relative_frequency'] = dataframe[column].value_counts(normalize=True).sort_index()

    df_frequency['cummulative_frequency'] = df_frequency['frequency'].cumsum()
    df_frequency['cummulative_relative_frequency'] = df_frequency['relative_frequency'].cumsum()

    return df_frequency