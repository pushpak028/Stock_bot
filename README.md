# Stock_bot
This is an stock market bot for discord 
 this bot helps in creating desired stock market updates for the members they just need to type the command with prefix !
 and type the company code as listed in market

 for eg: !stocky INFY

 this will give you the market updates of infosys with data visualizationi will put the example images also please check it

 This Python code is used to download historical stock price data for a given company using the Yahoo Finance API (via the yfinance library), save it as a CSV file, and then create and save two different line charts using Plotly Express and Plotly Graph Objects libraries. The code also checks if an "images" directory exists and creates one if it doesn't to store the generated chart images.

Here is a step-by-step explanation of the code:

Import necessary libraries:

pandas for data manipulation and analysis.
csv for working with CSV files.
yfinance for downloading stock price data.
plotly.express and plotly.graph_objects for creating interactive charts.
os for working with the file system.
Prompt the user to enter a company code, which presumably represents a publicly traded company's ticker symbol (e.g., "TSLA" for Tesla).

Use the yf.download function to download historical stock price data for the specified company with a daily interval ("1d") and minute-level data ("1m"). This data is stored in the dataa variable.

Save the downloaded data as a CSV file named "Stock.csv" using the to_csv method.

Read the CSV file "Stock.csv" into a pandas DataFrame called df. This DataFrame contains columns like 'Datetime', 'Open', 'High', 'Low', 'Close', and 'Adj Close', representing various aspects of the stock price data.

Create multiple traces (line series) for different aspects of the stock price data using Plotly Graph Objects:

trace1 for opening prices.
trace2 for high prices.
trace3 for low prices.
trace4 for closing prices.
trace5 for adjusted closing prices.
Create two separate figures (fig and fig2) to visualize the stock price data. fig displays only the closing prices, while fig2 displays all five aspects of the stock prices.

Update the layout of both figures to set the title and background color and enable the legend.

Check if the "images" directory exists. If it doesn't, create it using os.mkdir.

Use the write_image method to save the two figures as PNG images in the "images" directory. The engine="kaleido" argument specifies the image rendering engine to be used by Plotly.
