# Elon Musk's bad monetary advice
With the value of bitcoin fluctuating so much, even on the whim of a few influencers on Twitter, I decided to program a very simple AI based off Elon Musk tweets to invest in the cryptocurrency.
**Disclaimer: This project is intended as parody on the fluctuating bitcoin prices and should in no way be used as investment advice.**

## The project:
Steps in the project are noted with a dot ('•'), solved problems with a [x] and current problems with a [ ]. Additional info is noted with a "->"

Goal of the project is to make a Twitter bot that invests in Bitcoin based off Elon Musk's tweets. As a very rudimentary AI, the program evaluated tweets to correlate them to the bitcoin value and calculate a percentage to buy/sell and sell/buy an hour later every time a new tweet is posted.

### 1) Find a decent dataset of Elon Musk tweets and Bitcoin Prices
- The dataset of Elon Musk was obtained by the webscrape of residentmario on Kaggle: https://www.kaggle.com/residentmario/exploring-elon-musk-tweets
- Bitcoin Prices was found on https://www.CryptoDataDownload.com and based off the 1h Binance USDT/BTC timestamps
  -> the hourly value was taken as this dataset goes back to 2017, contrary to the dataset for every minute which starts in September 2019. While the dataset would be sufficiently large with more than 4000 tweets, initially the larger combination of tweets and bitcoin price is considered.
- [x] One of the problems was that the tweets had some characters that were not UTF-8 so the script 'rewrite_2021_toutf8.py' was used to ignore such cases.

    -> The script reads through the separate symbols and just ignores any errors if the symbol is not UTF8 compliant.

    -> For some reason, even though the dataset includes CSV files named '2010' - '2021', it seems that it describes 'all tweets until' rather than 'tweets made in the year'.
- [x] Afterwards I improved on the previous solution by just ignoring any non-alphanumeric characters in the parse script altogether.
- [x] Another problem encountered was that somewhere in 2019, the scraped data changes its notation for Unix timestamps (between line 5096 to 10393 both are present) from '1605855600000' to '1596322800.0'. To accommodate this the short script 'rewriteBinance.py' was written to get the proper Unix timestamp.

    -> The first one was 3 digits too long, maybe to count in milliseconds, the script removed them.

    -> The second one was supposed to be in decimals so the '.0' was removed.


### 2) Parse tweets to correlate the tweets to bitcoin
- [x] To circumvent using Pandas, open().readlines().split(",") was used as the package takes rather long time to process and import the CSV: The open() version is finished before Pandas is done importing the CSV.

    -> There are 4 variants of tweets in the Musk CSV: Either a tweet or a reply, and either containing a comma or not.

    -> The first case was eventually removed, and replies were also used. There is some omitted code in case tweets only are used.

      - Replies contain a '{[' on the line to list the replies to whereas regular tweets do not. As such a distinction can be made between the entries in the CSV.
      - As the dataset is a Comma Separated Value file, tweets containing a comma can be disruptive for the parser. Luckily, the file also accommodates for this and uses "" for the tweet containing any commas. This is also how the parser deals with these.
- [x] The dataset for bitcoin price starts somewhere in 2017, so in case a better dataset is found the parser first checks if Unix timestamps for the starting value and the final value are present before retrieving them.
- As the dataset is currently in hours, the hour in which the tweet is made is used as well as the following hour.
- In absolute terms, Bitcoin rose and fell much more in the near future than in 2017-2018, therefore the percentage is considered instead. For example: The famous tweet "In retrospect, it was inevitable" saw bitcoin rise with 6000 USDT in an hour, which is just shy of the biggest week for bitcoin in 2017 (1-7 December, a rise of about 7000 USDT). The tweet translates to a rise of about 19%, compared to the weeks 70%.
- The way tweets are considered is as following:

  -> Calculate the percentual change (Xf / Xi * 100) - 100 = Y

  -> Calculate the percentage change per symbol in the tweet (Y / length of the tweet = Z)

  -> Add the average to the weight dictionary (for symbol in tweet add Z to symbol in dictionary)

  -> Calculate the weight of the symbols by dividing the totals in the dictionary by dividing by the number of tweets (for symbol in dict divide weight by total tweets)

    - [ ] An improvement on this would be dividing by the total occurrences of the symbol itself, now vowels have more impact on decisions.

- An analysis was performed on the tweets using a few short examples like "Bitcoin", "bitcoin", "To the moon!" and "In retrospect, it was inevitable" as well as a 900 symbol long string that is representative for the occurrence of a letter in the English language (for example, the letter 'a' makes up about 8,2% of all letters in a dictionary so it is added 82 times to the string. Data is obtained from: https://en.wikipedia.org/wiki/Letter_frequency)

    -> A few variants were explored: Including or excluding the peak in 2017, open or closing of the hour(s).

      -> For example, excluding 2017, and opening and closing in the hour that the tweets were posted resulted in 'Bitcoin' 1.00, 'To the moon!' 1.15, 'In retrospect...' 3.53 and the testword 97.88. Including would result in 1.08, 1.20, 4.02 and 113.60 respectively.

    -> Why the letter occurrence percentages do not add up to 100% is unknown

- [x] The decision is made to use the 'Including, open, open variant' to continue


### 3) Create twitter bot to read and ""Invest"" bitcoin

- [ ] Get familiar with the Twitter API

- [ ] Get familiar with an exchange API to request the bitcoin value
