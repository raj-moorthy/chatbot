import streamlit as st
import time
import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot pairs
pairs = [
    [r"hi|hello|hey|helo", ["Hello! This is Baira! How can I assist you today?"]],
    [r"how are you?", ["I'm just a bot, but I'm happy to chat with you! How about you?"]],
    [r"what is your name?", ["I'm Baira, your personal chatbot to know about you."]],
    [r"who created you?", ["I was created by RAJ to assist you!"]],
    [r"do you believe in love?", ["Love is a beautiful feeling! What do you think about love?"]],
    [r"how do i find true love?", ["Be yourself, stay honest, and surround yourself with people who appreciate you!"]],
    [r"what is love?", ["Love is a deep emotional connection. Some say, 'Love is when someone else's happiness is your own.'"]],
    [r"how do i impress my crush?", ["Be confident, be kind, and listen to them! Genuine connections matter."]],
    [r"does love at first sight exist?", ["Some believe in it, while others think love grows with time. What’s your opinion?"]],
    [r"what should i do if my partner is ignoring me?", ["Communication is key. Try talking to them and expressing how you feel."]],
    [r"can you be my valentine?", ["I’d love to, but I think you deserve someone real!"]],
    [r"who is raj lover?", ["He not believe in Love at all but had an emotion crush on ASWINI"]],
    [r"tell me about parents", ["Parents are the guiding force in our lives. They love and support us no matter what."]],
    [r"how can i make my parents happy?", ["Show them love, respect, and appreciation. Spend time with them and be grateful."]],
    [r"i miss my parents", ["It's okay to miss them. Maybe give them a call or write them a heartfelt message?"]],
    [r"why do parents get angry?", ["Parents sometimes get angry because they worry about us. Talking to them calmly can help."]],
    [r"how to deal with strict parents?", ["Try to understand their perspective and communicate your feelings with respect."]],
    [r"do you have a brother or sister?", ["I have two Sisters, Do you have any?"]],
    [r"how to be a good friend?", ["Be honest, supportive, and always listen when they need you."]],
    [r"why do friends fight?", ["Misunderstandings happen, but a good friendship is about forgiving and growing together."]],
    [r"what is your favorite color?", ["I like all colors especially lavender, but I’d love to know yours!"]],
    [r"what is your favorite food?", ["I don’t eat, but I hear pizza and biryani are amazing!"]],
    [r"what is your favorite song?", ["I enjoy all kinds of music. Do you have a favorite song?"]],
    [r"what is your favorite movie?", ["I like many movies! Do you prefer action, comedy, or romance?"]],
    [r"who is your favorite actor?", ["I think all actors bring something special. Who's your favorite?"]],
    [r"do you like animals?", ["Yes! Animals are wonderful companions. Do you have a pet?"]],
    [r"what is your favorite hobby?", ["I love chatting with you! What are your hobbies?"]],
    [r"i feel lonely", ["I'm here for you. Sometimes, reaching out to a friend or family member helps."]],
    [r"i am sad", ["I’m sorry to hear that. Do you want to talk about what’s on your mind?"]],
    [r"how to be happy?", ["Happiness comes from within! Focus on things you love and surround yourself with positive people."]],
    [r"tell me a joke", ["Why did the cricket player bring a ladder? Because he wanted to reach the top of the scoreboard!"]],
    [r"can you dance?", ["I wish I could, but I can definitely recommend some great dance songs!"]],
    [r"bye|goodbye", ["Goodbye! Keep smiling!", "See you soon! Stay happy."]],
     [r"who is raj moorthy", ["Raj Moorthy is a Undergraduate student currently pursuing AI at KCE"]],
      [r"what is his last match score", ["His last match score is 33*"]],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Streamlit UI
def main():
    st.set_page_config(page_title="Baira Chatbot", layout="centered")
    
    st.title("🤖 Baira Chatbot")
    
    # Static Greeting Message
    with st.chat_message("assistant"):
        st.markdown("Hello! This is Baira! you may talk me as you talk with Raj Moorthy")
    
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    
    # Display previous chat messages
    for sender, message in st.session_state["messages"]:
        with st.chat_message("user" if sender == "You" else "assistant"):
            st.markdown(message)
    
    # User input
    user_input = st.chat_input("Type your message...")
    if user_input:
        response = chatbot.respond(user_input)
        response = response if response else "I'm still learning! Can you rephrase that?"
        
        # Display user message
        st.session_state["messages"].append(("You", user_input))
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Display bot response
        st.session_state["messages"].append(("Baira", response))
        time.sleep(0.5)
        with st.chat_message("assistant"):
            st.markdown(response)
    
if __name__ == "__main__":
    main()