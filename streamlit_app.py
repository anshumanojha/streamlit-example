import streamlit as st
import pandas as pd

# Tic Tac Toe Game Logic
class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.winner = None

    def make_move(self, position):
        if self.board[position] == ' ' and not self.winner:
            self.board[position] = self.current_player
            self.check_winner()
            self.switch_player()

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                self.winner = self.current_player

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

# Streamlit App
st.title("Anshuman's Portfolio with Tic Tac Toe Game")

# Tic Tac Toe Game
tic_tac_toe = TicTacToe()

# Button to start the Tic Tac Toe Game
if st.button("Start Tic Tac Toe Game"):
    st.sidebar.title("Tic Tac Toe Game")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.sidebar.button("", key="btn_0"):
            tic_tac_toe.make_move(0)
    with col2:
        if st.sidebar.button("", key="btn_1"):
            tic_tac_toe.make_move(1)
    with col3:
        if st.sidebar.button("", key="btn_2"):
            tic_tac_toe.make_move(2)

    col4, col5, col6 = st.columns(3)
    with col4:
        if st.sidebar.button("", key="btn_3"):
            tic_tac_toe.make_move(3)
    with col5:
        if st.sidebar.button("", key="btn_4"):
            tic_tac_toe.make_move(4)
    with col6:
        if st.sidebar.button("", key="btn_5"):
            tic_tac_toe.make_move(5)

    col7, col8, col9 = st.columns(3)
    with col7:
        if st.sidebar.button("", key="btn_6"):
            tic_tac_toe.make_move(6)
    with col8:
        if st.sidebar.button("", key="btn_7"):
            tic_tac_toe.make_move(7)
    with col9:
        if st.sidebar.button("", key="btn_8"):
            tic_tac_toe.make_move(8)

# Add the rest of your existing code below


# Add the rest of your existing code below


# Add the rest of your existing code below

# Add links to LinkedIn and GitHub profiles
st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/anshuman-ojha-34093885/)")
st.markdown("[GitHub - Python Projects Automated Google Search](https://github.com/anshumanojha/pythonprojects/blob/master/Googlewebsearchauto.ipynb)")
st.markdown("[GitHub - Python Projects Automated Location Automate](https://github.com/anshumanojha/pythonprojects/blob/master/browser.py)")

# Create bar chart for tools data
tools_data = [10, 10, 8, 9, 7]
tools_labels = ['MYSQL', 'Python', 'Dashboard Development', 'Power Bi']
tools_chart = dict(zip(tools_labels, tools_data))

# Create line chart for technology data
technology_data = [9, 10, 10, 8, 7, 10]
technology_labels = ['Superset', 'SQL', 'Python', 'AWS', 'AI', 'ML']
technology_chart = dict(zip(technology_labels, technology_data))

# Create pie chart for skills data
skills_data = [30, 60, 60, 33, 50]
skills_labels = ['Data Scraping', 'Python Automation', 'Cohort Analysis', 'Trend Analysis', 'Repayment Automation']
skills_chart = dict(zip(skills_labels, skills_data))

col1, col2, col3 = st.columns(3)

with col1:
    st.header('Tools Known')
    st.bar_chart(tools_chart, use_container_width=True)

with col2:
    st.header('Technology Known')
    st.line_chart(technology_chart, use_container_width=True)

with col3:
    st.header('Skills Proficiency')
    st.bar_chart(skills_chart, use_container_width=True)

st.header('Certifications')
st.markdown(
    "<ul style='font-size: 18px; color: #333333; list-style-type: square;'>"
    "<li><a href='https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V' target='_blank'>IBM-Data Analysis certificate</a></li>"
    "<li><a href='https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX' target='_blank'>IBM-Data Visualization with Python</a></li>"
    "<li><a href='https://www.coursera.org/account/accomplishments/certificate/ST57AP42DMXS' target='_blank'>Databases and SQL for Data Science with Python</a></li>"
    "<li><a href='https://www.coursera.org/account/accomplishments/certificate/PWQGKGYMMMQU' target='_blank'>Machine Learning with Python</a></li>"
    "<li><a href='https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV' target='_blank'>Python for Data Science, AI & Development</a></li>"
    "<li><a href='https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9' target='_blank'>IBM Data Science Specialization</a></li>"
    "</ul>",
    unsafe_allow_html=True
)
# Map section
st.header('Location - Bengaluru')
# Create a DataFrame with your location data
location_df = pd.DataFrame({'LATITUDE': [12.9716], 'LONGITUDE': [77.5946]})
st.map(location_df, zoom=10)

# Certifications section

# Project 1: Data Scraping
st.title('Projects and Codes')
st.subheader('Project 1: Data Scraping')
st.write("Description: A Python script to scrape data from a website.")

code_project1 = '''
def get_smaller_urls(search_query):
    url = "https://google.com/search?q=" + search_query
    request_result = requests.get(url)
    search_results = request_result.text
    start_index = search_results.find("https://www.zomato.com/")
    end_index = search_results.find("&", start_index)
    smaller_url = search_results[start_index:end_index]
    return smaller_url
search_query = "biryani"
result = get_smaller_urls(search_query)
df = pd.DataFrame({"Search Query": [search_query],
                   "Smaller URL": [result]})
df
'''

if 'selected_project' not in st.session_state:
    st.session_state.selected_project = None

if st.button('Python Scraping: Click to Run'):
    st.session_state.selected_project = 'Project 1: Data Scraping'

if st.session_state.selected_project == 'Project 1: Data Scraping':
    st.subheader('Project 1: Data Scraping')
    st.write("Description: A Python script to scrape the first link from Google")
    st.code(code_project1, language='python')
    st.subheader('Output:')
    df = get_smaller_urls("biryani in bangalore")
    st.write(df)

# Project 2: Weather App
st.subheader('Project 2: Weather App')
st.write("Description: A Python script to fetch weather information for a given city.")

def get_weather(city):
    api_key = "4cb3a44e7cab1adb19e17ecc44c6da11"  # Replace with your OpenWeatherMap API key

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            city_name = data["name"]
            temperature = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"]

            weather_info = f"City: {city_name}\nTemperature: {temperature}°C\nWeather: {weather_desc}"
            st.info(weather_info)
        else:
            st.error(f"Failed to fetch weather data: {data['message']}")

    except Exception as e:
        st.error(f"Failed to fetch weather data: {e}")

city = st.text_input("Enter city name:")
if st.button("Get Weather"):
    get_weather(city)

# Add the rest of your existing code below
