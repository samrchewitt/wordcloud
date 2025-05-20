# filters for text or otherwise
def filter_text(df, col, text, method='out', case=False):
    """
    Filters rows from the DataFrame based on whether the specified column contains 
    certain text patterns.

    Parameters:
    - df (pd.DataFrame): Input DataFrame
    - col (str): Column name to filter on
    - text (str or list of str): Substring(s) to match
    - method (str): 'in' to keep matching rows, 'out' to exclude them (default 'out')
    - case (bool): Case-sensitive match (default False)

    Returns:
    - pd.DataFrame: Filtered DataFrame
    """
    if col not in df.columns:
        raise ValueError(f"Column '{col}' does not exist in DataFrame")

    if isinstance(text, str):
        text = [text]

    for t in text:
        if method == 'in':
            df = df[df[col].str.contains(t, na=False, case=case)]
            # indicate how many rows were filtered
            print(f"Retained {len(df)} rows containing '{t}' in column '{col}'")
        elif method == 'out':
            df = df[~df[col].str.contains(t, na=False, case=case)]
            
        else:
            raise ValueError("Method must be 'in' or 'out'")

    return df
