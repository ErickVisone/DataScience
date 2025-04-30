import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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


def composition_hist_box(dataframe, column, interval="auto"):
    fig, (ax1, ax2) = plt.subplots(
    nrows=2
    , ncols=1
    , gridspec_kw={
        "height_ratios":(0.15, 0.85),
        "hspace": 0.05
    }
    , sharex=True
    , figsize=(6, 6)
    )

    sns.boxplot(
        data = dataframe, x = column , showmeans=True , color = 'C0' , ax=ax1
        , meanline=True 
        , meanprops={
            'color': 'C1'
            , 'linewidth': 0.5
            , 'linestyle': '--'
            , 'label': 'Mean'
        }
    )

    sns.histplot(data = dataframe, x = column, kde=True, bins= interval, ax=ax2)    

    for ax in (ax1, ax2):
        ax.grid(True, linestyle='--', color = 'gray', alpha=0.2)
        ax.set_axisbelow(True)

    ax2.axvline(dataframe[column].mean(), color='C1', linestyle='--', label='Mean', linewidth=0.5)
    ax2.axvline(dataframe[column].median(), color='C2', linestyle='--', label='Median', linewidth=0.5)
    ax2.axvline(dataframe[column].mode()[0], color='C3', linestyle='--', label='Mode', linewidth=0.5)

    ax2.legend(loc='upper right', fontsize=8, frameon=False)