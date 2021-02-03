import pandas as pd;

def main():
    data = pd.read_excel('../../data/raw/Online Retail.xlsx', engine='openpyxl', header=0)

    cancelledEntries = data[(data['Quantity'] <= 0) | (data['UnitPrice'] < 0)]
    data.drop(cancelledEntries.index, inplace=True)
    data.drop_duplicates(inplace=True)

    final_data = data[['InvoiceNo', 'StockCode', 'Description']]
    final_data.to_csv('../../data/processed/data.csv', index=False)

main()
