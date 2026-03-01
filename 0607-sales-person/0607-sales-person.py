def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_companies = company[company['name'] == 'RED']
    
    if red_companies.empty:
        return sales_person[['name']]
    
    red_company_id = red_companies['com_id'].iloc[0]
    
    sales_with_red = orders[orders['com_id'] == red_company_id]['sales_id'].unique()
    
    result = sales_person[~sales_person['sales_id'].isin(sales_with_red)]
    
    return result[['name']]