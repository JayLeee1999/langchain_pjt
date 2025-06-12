import yfinance as yf
import pandas as pd

class Stock:
    # 생성자: 기본값 설정
    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)

    # 회사 기본 정보
    def get_basic_info(self):
        basic_info = pd.DataFrame.from_dict(self.ticker.info, orient='index', columns=['values'])
        return basic_info.loc[['longName', 'marketCap', 'industry', 'sector', 'fullTimeEmployees', 'currentPrice', 'enterpriseValue']]
        
        # return basic_info
    

    # 재무제표 수집
    def get_financial_statement(self):
        
        # 손익 계산서
        income_state = self.ticker.income_stmt.loc[['Total Revenue', 'Gross Profit', 'Operating Income', 'Net Income']].iloc[:, :4].to_markdown()
            # 대차대조표를 마크다운 형식으로 변환
        # print(income_state)

        # 대차대조표를 마크다운 형식으로 변환
        balance_sheet = self.ticker.balance_sheet.loc[['Total Assets', 
                                                       'Total Liabilities Net Minority Interest',
                                                       'Stockholders Equity']].iloc[:, :4].to_markdown()
        # print(balance_sheet)

        # 현금 흐름표를 마크다운 형식으로 변환
        cash_flow = self.ticker.cashflow.loc[['Operating Cash Flow', 
                                              'Investing Cash Flow',
                                              'Financing Cash Flow']].iloc[:, :4].to_markdown()
        # print(cash_flow)


        return f"""
            ### 손익계산서
            {income_state}
            ### 대차대조표
            {balance_sheet}
            ### 현금흐름표
            {cash_flow}
            """
    
    # 주식 거래량
    def get_stock_volume(self):
        volume_data = self.ticker.history(period='6mo')['Volume']
        volume_data_desc = volume_data.sort_index(ascending=False)
        print(volume_data_desc)
        return volume_data_desc


# python stock_info.py 실행할때만 아래코드 실행됨
if __name__ == "__main__":
    # 회사 이름
    company_name = "AAPL"
    # Stock 객체생성
    stock = Stock(company_name)
    # print("회사 심볼", stock.symbol)
    # print("회사 티커 객체", stock.ticker)
    # stock.get_basic_info()

    # print(stock.get_financial_statement())
    print(stock.get_stock_volume())

