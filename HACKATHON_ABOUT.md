## Inspiration
Learning can be a large hurdle for many people worldwide as a result of convoluted topics that confuse them. Thus, ELI-X aims to make learning more frictionless by breaking down complex topics into easily digestible chunks for users to take in according to their academic level. 

## What it does
ELI-X is an AI-powered app that explains any topic in many different degrees of expertise, depending on the user’s preference. It allows beginners to easily grasp new, complex topics without feeling overwhelmed, while allowing experts to easily get a quick refresh on familiar topics. ELI-X caters to a wide demographic of different academic backgrounds, such as elementary school, middle school, high school, college, and PhD levels. For instance, a user can ask ‘What is quantum computing?’ and choose elementary, high school, or PhD level. 
## How we built it
ELI-X was built using the Python programming language and used libraries such as Streamlit for the UI and google-genai for sending prompts to Gemini AI. The Streamlit UI was built manually as a rough framework and then used AI-assisted code suggestions to refine the Streamlit layout for users. A custom AIModel class was created to make accessing the google-genai library more streamlined, which made the overall code tidier and more robust. The app flow is: 
- User selects an academic level and enters their question. 
- The app constructs a level-specific and detailed prompt. 
- The AIModel wrapper sends the prompt to Gemini and streams the response to the UI. 

## Challenges we ran into
Building ELI-X was not all smooth sailing. The first problem we encountered was the prompts being empty when sent to Gemini AI. We diagnosed the problem as Streamlit’s rendering resetting user questions with every key press due to the use of random placeholder prompts. To fix this, we used Streamlit’s session state to store the random placeholder, keeping user inputs stable across rerenders. The second issue we encountered was the API rate limits of the Gemini AI API, as they would cause our app to crash when exceptions occured. We implemented try/except blocks to act as a fallback in the event of any failed API requests and prevent the app from crashing. 
## Accomplishments that we're proud of
We successfully incorporated Gemini AI into a sleek UI in Streamlit that enhances user experience. Moreover, we also ensured that prompts sent to Gemini AI are structured and clear for the AI to understand while also capturing the user's inquiry as well as academic level. 

## What we learned
AI models are exceptionally powerful at simplifying convoluted topics into easily digestible chunks that anyone can easily understand. However, such powerful free AI models have strict limitations such as frequent rate limits and only a small pool of free AI models. Thus, we learnt that handling frequent API errors is paramount to ensuring app stability and functionality as well as user experience. 

## What's next for ELI-X: Explain Like I’m X
ELI-X’s development has only just started. We aim to give this project many more features in the future to enhance the user experience and quality of this project. 
- Short term: Expand range of academic backgrounds 
- Mid-term: Incorporate chats to allow for back-and-forth conversations that retain context 
- Long term: Database saving and downloading/copying chats to text.
