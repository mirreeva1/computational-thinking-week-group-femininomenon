from datetime import datetime

def solution_station_1(date_str):
    
    date_format = "%Y-%m-%d"
    
    # Dictionary to map English days to Japanese
    days_of_week_japanese = {
        "Monday": "月曜日",
        "Tuesday": "火曜日",
        "Wednesday": "水曜日",
        "Thursday": "木曜日",
        "Friday": "金曜日",
        "Saturday": "土曜日",
        "Sunday": "日曜日"
    }
    
    try:
        # Parse the date string into a datetime object
        date_obj = datetime.strptime(date_str, date_format)
        # Get the day of the week in English
        day_of_week_english = date_obj.strftime("%A")
        # Convert to Japanese using the dictionary
        day_of_week_japanese = days_of_week_japanese.get(day_of_week_english, "不明な日")
        return day_of_week_japanese
    except ValueError:
        return "無効な日付形式"


if __name__ == "__main__":
    test_date = "2023-01-07"
    print(solution_station_1(test_date))  # Output: 土曜日

