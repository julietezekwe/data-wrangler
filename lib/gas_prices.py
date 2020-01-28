import requests
import datetime
import os
from bs4 import BeautifulSoup

class GasPrice:
  ENDPOINT = 'https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm'
  OUTPUT_DIR = 'output/'
  DAILY_PRICES = OUTPUT_DIR + 'Output_daily_prices.csv'
  MONTHLY_PRICES = OUTPUT_DIR + 'Output_monthly_prices.csv'

  def __init__(self):
    self.html_doc = None
    self.data_node = None
    self.dataset = []
  
  def daily_prices_csv(self):
    self.__run()

    if self.__file_already_exit(self.DAILY_PRICES):
      print(self.DAILY_PRICES, 'already exit and will be overwritten! \n')
    
    with open(self.DAILY_PRICES, 'w') as csv_handle:
      csv_handle.write('DATE, PRICE \n')
      for day in self.dataset:
        csv_handle.write(','.join(day))
        csv_handle.write('\n')
      
    print('Completed! ')
    print('Open', os.path.join(os.getcwd(), self.DAILY_PRICES))

  def monthly_prices_csv(self):
    self.__run()

    if self.__file_already_exit(self.MONTHLY_PRICES):
      print(self.MONTHLY_PRICES, 'already exit and will be overwritten! \n')
    
    with open(self.MONTHLY_PRICES, 'w') as csv_handle:
      csv_handle.write('MONTH, PRICE \n')
      prev_day = self.dataset[0]

      for day in self.dataset:
        if self.__to_day(day) > self.__to_day(prev_day):
          csv_handle.write(prev_day[0][3:6] + ',' + prev_day[1])
          csv_handle.write('\n')
        prev_day = day
      
    print('Completed! ')
    print('Open', os.path.join(os.getcwd(), self.MONTHLY_PRICES))

  def __to_day(self, day):
    return int(day[0].split('-')[0])

  def __run(self):
    if len(self.dataset) == 0:
      self.__load_page()
      self.__extract_data_node()
      self.__extract_data()

  def __load_page(self):
    try:
      req = requests.get(self.ENDPOINT)
      if req.status_code == 200:
        self.html_doc = req.content
        print('HTML fetched...')
      else:
          print('Server error...')
    except Error as e:
      print('Unknown network error...')

  def __extract_data_node(self):
    html_node = BeautifulSoup(self.html_doc, 'html5lib')
    self.data_node = html_node.find(summary="Henry Hub Natural Gas Spot Price (Dollars per Million Btu)")
 
  def __extract_data(self):
    dataset = []
    for node in self.data_node.find_all('tr'):
      date_node = node.find('td', {'class': 'B6'})
      if date_node:
        date = date_node.string.replace('\xa0\xa0', '')
        dataset.append([date, *[val.text for val in node.find_all('td', {'class': 'B3'})]])
    self.dataset = self.__format_prices(dataset)
    self.dataset.reverse()

  def __format_prices(self, dataset):
    combined = []
    for week in dataset:
      start_date = self.__normalize_start_date(week[0])
      day_offset = 0
      for daily_price in week[1:]:
        day = start_date + datetime.timedelta(days = day_offset)
        combined.append([day.strftime('%d-%b-%Y'), daily_price])
        day_offset += 1
    return combined

  def __normalize_start_date(self, string):
    start_date = string.replace('- ',' ').replace('-', ' ').split(' ')[0:3]
    return datetime.datetime.strptime('-'.join(start_date), '%Y-%b-%d')

  def __file_already_exit(self, filename):
    return os.path.exists(filename)
  

def main():
  g = GasPrice()
  g.daily_prices_csv()
  g.monthly_prices_csv()
  

if __name__ ==  '__main__':
  main()