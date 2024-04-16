# Google Analytics 4 x Custom Backend

## Here is what you need to do to install it and test that it works:

1. Download/clone/pull the repository to your local machine
2. First, test that the code is working: in the root directory, open the terminal and write: `python ga4_script.py`
3. Script will prompt you to add the name of the Google Analytics Website csv file name:

- Type: `fake_data.csv`

4. Script will proceed and will ask you for the month and year:

- Type: `April` (or any other month but best to type the current month)
- Type: `2024` (or the current year)

5. Script will proceed and will ask you the name of Google Analytics Native csv file name:

- Type: `fake_native_data.csv`

6. That's it! You should wait until script ends and your **final.xlsx** file will be available in the root directory.

## If you want to make this script working for you perform the following steps:

1. Head inside **ga4_script.py**
2. Delete the following lines:<br>
   ```"cd step-0",```<br>
   ```"python fake_app_ga4.py",```<br>
   ```"python fake_backend.py",```<br>
   ```"python fake_channels.py",```<br>
   ```"python fake_ga4.py",```<br>
3. Add your data Google Analytics report about website performance to folder **step-1** - CSV format
4. Add your data Backend report about current month performance to folder **step-2** - EXCEL format
5. Add your data Google Analytics report about app performance to folder **step-5** - CSV format
6. Add your lookup Channels report with all traffic resource channels to folder **step-7** - CSV format
7. Make sure that names of reports in **step-1** and **step-5** are easy to write in the terminal.
8. Open the terminal and write: `python ga4_script.py`
9. Further steps are as above but you need to input your data

## Here is the image how this report is working:
![doc_ga4_reporting](https://github.com/NGPetrovich/ga4-traffic-sources/assets/75169515/96e7937e-1708-45f6-ad12-07ef32aecef6)
