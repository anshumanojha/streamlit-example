import streamlit as st
import requests
import pandas as pd
import streamlit.components.v1 as components

# Add HTML and JavaScript for the game
game_code = """
<script>
    let colors = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange"];
    let score = 0;
    let attempts = 0;
    let max_attempts = 3;  // Adjust this as needed
    let gameFinished = false;

    function startGame() {
        document.getElementById("game-container").style.display = "block";
        document.getElementById("portfolio-container").style.display = "none";
        showColor();
    }

    function showColor() {
        let randomIndex = Math.floor(Math.random() * colors.length);
        let colorToMatch = colors[randomIndex];
        let colorElement = document.getElementById("color-display");
        colorElement.innerText = colorToMatch;
    }

    function checkMatch(selectedColor) {
        let colorToMatch = document.getElementById("color-display").innerText;
        if (selectedColor === colorToMatch) {
            score += 1;
            st.text("Correct! Keep Going.")
        } else {
            st.text("Incorrect. Try Again.");
        }

        attempts += 1;
        if (attempts >= max_attempts) {
            finishGame();
        } else {
            showColor();
        }
    }

    function finishGame() {
        gameFinished = true;
        document.getElementById("game-container").style.display = "none";
        document.getElementById("portfolio-container").style.display = "block";
    }
</script>
"""

st.title("Anshuman's Portfolio")
# Add game container and portfolio container
st.markdown(f"<div id='game-container'>{game_code}</div>", unsafe_allow_html=True)
st.markdown("<div id='portfolio-container' style='display: none;'>", unsafe_allow_html=True)

# Button to start the game
if st.button("Start Color Matching Game"):
    st.markdown("<script>startGame();</script>", unsafe_allow_html=True)

# Game UI
st.markdown("<div id='color-display'></div>", unsafe_allow_html=True)
selected_color = st.selectbox("Select the Matching Color", ["Red", "Green", "Blue", "Yellow", "Purple", "Orange"], key="selected_color", on_change="checkMatch(value)")

# Close the portfolio container
st.markdown("</div>", unsafe_allow_html=True)

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



