import pandas as pd

def filtro(dataframe, variable, valor):
    if isinstance(variable, str):
        if variable in dataframe.columns:
            return dataframe[dataframe[variable] == valor]
        else:
            raise ValueError(f"La variable '{variable}' no está presente en el DataFrame.")
    elif isinstance(variable, int):
        if variable < len(dataframe.columns):
            return dataframe[dataframe[dataframe.columns[variable]] == valor]
        else:
            raise ValueError(f"El índice de columna '{variable}' está fuera de rango.")
    else:
        raise TypeError("La variable debe ser un nombre de columna (str) o un índice de columna (int).")

if __name__ == "__main__":
    data = {
        'A': [1, 2, 3, 4],
        'B': ['a', 'b', 'c', 'd'],
        'C': [10, 20, 30, 40]
    }
    df = pd.DataFrame(data)

    df_filtrado = filtro(df, 'B', 'b')
    print("DataFrame filtrado por 'B' igual a 'b':")
    print(df_filtrado)
