import openai 
import streamlit as st 

openai.api_key = st.secrets["pass"]

#st.header('Simple Question-Answering')

#article_text = st.text_area('Enter your question here')

# output_size = st.radio(label='What kind of output do you want?',
#      options=['To-the-point', 'concise', 'detailed'])
prg = st.progress(0)
def main_page():
    st.markdown("# Welcome to Machine Learning quiz! 😀")
    st.sidebar.markdown("# Machine learning quiz 🧐")
    
# progress_text = "Operation in progress. Please wait."
# my_bar = st.progress(0, text=progress_text)

# def disable(b):
#     st.session_state["disabled"] = b
# def disable():
#   if "but_a":
#     st.session_state.disabled = True

# if "disabled" not in st.session_state:
#     st.session_state.disabled = False

def page2():
    st.markdown("# Question 1❓")
    st.sidebar.markdown("# Machine learning quiz 🧐")
    with st.form("my_form"):
      st.write("Question 1 : Suppose a random variable X assumes the values -c and c with probabilities p and 1 -p respectively. What are the expectation E [X] and variance var(X)?")
      article_text = st.text_area('Enter your question below:')
      # Every form must have a submit button. 
      submitted1 = st.form_submit_button("Submit", disabled=False)
      if submitted1:
        st.session_state.submit1 = True
       # st.script_runner.StopException("Stop execution")
        response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Please answer this question: " + article_text,
      temperature=0.5,
      max_tokens=516,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
    )
        st.write('Answer:')
        res = response['choices'][0]['text']
        st.success(res)
        prg.progress(12)
        # st.session_state.disabled = True 
        # if "disabled" not in st.session_state:
        #   st.session_state.disabled = False


def page3():
    st.markdown("# Question 2 ❓")
    st.sidebar.markdown("# Machine learning quiz 🧐")
    prg.progress(12)
    # my_bar.progress(percent_complete + 1, text=progress_text)
    with st.form("my_form"):
      st.write("Question 2 : Suppose A, B, C are events such that A and B are independent, and B and C are independent as well. True or false: P(A,B,C) = P(C|A)P(A)P(B)")
      article_text = st.text_area('Enter your question below:')
    #  slider_val = st.slider("Form slider")
      #checkbox_val = st.checkbox("Form checkbox")

      # Every form must have a submit button.
      submitted = st.form_submit_button("Submit")
      if submitted:
        response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Please answer this question: " + article_text,
      temperature=0.5,
      max_tokens=516,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
    )
        st.write('Answer:')
        res = response['choices'][0]['text']
        st.success(res)
        # st.session_state.disabled = True 
        # if "disabled" not in st.session_state:
        #   st.session_state.disabled = False
        prg.progress(24)

def page4():
    st.markdown("# Question 3 ❓")
    st.sidebar.markdown("# Machine learning quiz 🧐")
    with st.form("my_form"):
      st.write("Question 3 : You toss 30 times a coin which is loaded so that probability of heads is θ = 0.9. What is the probability that all 30 tosses yield heads? (You can round the answer to the third decimal digit))")
      article_text = st.text_area('Enter your question below:')
    #  slider_val = st.slider("Form slider")
      #checkbox_val = st.checkbox("Form checkbox")
      prg.progress(24)

      # Every form must have a submit button.
      submitted = st.form_submit_button("Submit")
      if submitted:
        response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Please answer this question: " + article_text,
      temperature=0.5,
      max_tokens=516,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
    )
        st.write('Answer:')
        res = response['choices'][0]['text']
        st.success(res)
        prg.progress(38)
        # st.session_state.disabled = True 
        # if "disabled" not in st.session_state:
        #   st.session_state.disabled = False

def page5():
    st.markdown("# Question 4 ❓")
    st.sidebar.markdown("# Machine learning quiz 🧐 ")
    prg.progress(38)
    with st.form("my_form"):
      st.write("Question 4 : Let x_i , i = 1 . . . N be N independent, identically distributed Gaussian random variables with zero mean and unit variance. Which of the following random variables will have zero mean (mark all that apply)?")
      article_text = st.text_area('Enter your question below:')
    #  slider_val = st.slider("Form slider")
      #checkbox_val = st.checkbox("Form checkbox")

      # Every form must have a submit button.
      submitted = st.form_submit_button("Submit")
      if submitted:
        response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Please answer this question: " + article_text,
      temperature=0.5,
      max_tokens=516,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
    )
        st.write('Answer:')
        res = response['choices'][0]['text']
        st.success(res)
        prg.progress(50)
        # st.session_state.disabled = True 
        # if "disabled" not in st.session_state:
        #   st.session_state.disabled = False

def page6():
    st.markdown("# Question 5 ❓")
    st.sidebar.markdown("# Machine learning quiz 🧐 ")
    prg.progress(50)
    with st.form("my_form"):
      st.write("Question 5 : Let U ∈ R^{d×d} be an orthonormal matrix, i.e., if u_i is the i-th column of U then u_i^Tu_i =1 and u_i^T u_j =0 for any i !=j. Let ||x||_2 stand for the Euclidean norm of the vector x, i.e., ||x||_2 = \sqrt(x^T x). Prove that ||U x||_2 = ||x||_2.")
      article_text = st.text_area('Enter your question below:')
    #  slider_val = st.slider("Form slider")
      #checkbox_val = st.checkbox("Form checkbox")

      # Every form must have a submit button.
      submitted = st.form_submit_button("Submit")
      if submitted:
        response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Please answer this question: " + article_text,
      temperature=0.5,
      max_tokens=516,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
    )
        st.write('Answer:')
        res = response['choices'][0]['text']
        st.success(res)
        # st.session_state.disabled = True 
        # if "disabled" not in st.session_state:
        #   st.session_state.disabled = False
        prg.progress(63)

def page7():
    st.markdown("# Question 6 ❓")
    st.sidebar.markdown("# Machine learning quiz 🧐")
    prg.progress(63)
    with st.form("my_form"):
      st.write("Question 6 :We are given matrices A ∈ R^{100×30} and B ∈ R^{30×100}. What can you say about the rank of the matrix C = AB?")
      article_text = st.text_area('Enter your question below:')
    #  slider_val = st.slider("Form slider")
      #checkbox_val = st.checkbox("Form checkbox")

      # Every form must have a submit button.
      submitted = st.form_submit_button("Submit")
      if submitted:
        response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Please answer this question: " + article_text,
      temperature=0.5,
      max_tokens=516,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
    )
        st.write('Answer:')
        res = response['choices'][0]['text']
        st.success(res)
        prg.progress(75)
        # st.session_state.disabled = True 
        # if "disabled" not in st.session_state:
        #   st.session_state.disabled = False

def page8():
    st.markdown("# Question 7 ❓")
    st.sidebar.markdown("# Machine learning quiz 🧐")
    prg.progress(75)
    with st.form("my_form"):
      st.write("Question 7 : Let e_j be the j-th basis vector for R^d. That is, elements of the length-d vector e_j are all zero, except e_{j,j} = 1. Which of the following equalities is correct for any x ∈ R^d ?")
      article_text = st.text_area('Enter your question below:')
    #  slider_val = st.slider("Form slider")
      #checkbox_val = st.checkbox("Form checkbox")

      # Every form must have a submit button.
      submitted = st.form_submit_button("Submit")
      if submitted:
        response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Please answer this question: " + article_text,
      temperature=0.5,
      max_tokens=516,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
    )
        st.write('Answer:')
        res = response['choices'][0]['text']
        st.success(res)
        prg.progress(88)
        # st.session_state.disabled = True 
        # if "disabled" not in st.session_state:
        #   st.session_state.disabled = False

def page9():
    st.markdown("# Question 8 ❓ ")
    st.sidebar.markdown("# Machine learning quiz 🧐 ")
    prg.progress(88)
    with st.form("my_form"):
      st.write("Question 8 : Let f:R^d →R be a function given by f(x, y) = sin(3x) − x log(5y^2). What is the gradient of f as a function of (x, y)?")
      article_text = st.text_area('Enter your question below:')
    #  slider_val = st.slider("Form slider")
      #checkbox_val = st.checkbox("Form checkbox")

      # Every form must have a submit button.
      submitted = st.form_submit_button("Submit")
      if submitted:
        response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Please answer this question: " + article_text,
      temperature=0.5,
      max_tokens=516,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
    )
        st.write('Answer:')
        res = response['choices'][0]['text']
        st.success(res)
        prg.progress(100)
        # st.session_state.disabled = True 
        # if "disabled" not in st.session_state:
        #   st.session_state.disabled = False
        st.balloons()

page_names_to_funcs = {
    "Main Page": main_page,
    "Question 1": page2,
    "Question 2": page3,
    "Question 3": page4,
    "Question 4": page5,
    "Question 5": page6,
    "Question 6": page7,
    "Question 7": page8,
    "Question 8": page9,
}

selected_page = st.sidebar.selectbox("Select question number", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


###
# with st.form("my_form"):
#    st.write("Question 1 : Suppose a random variable X assumes the values -c and c with probabilities p and 1 -p respectively. What are the expectation E [X] and variance var(X)?")
#    article_text = st.text_area('Enter your question below:')
#  #  slider_val = st.slider("Form slider")
#    #checkbox_val = st.checkbox("Form checkbox")

#    # Every form must have a submit button.
#    submitted = st.form_submit_button("Submit")
#    if submitted:
#     response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Please answer this question: " + article_text,
#   temperature=0.5,
#   max_tokens=516,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0,
# )
#     st.write('Answer:')
#     res = response['choices'][0]['text']
#     st.success(res)
    #st.download_button('Download result', res)
    # st.write("done")
       #st.write("slider", slider_val, "checkbox", checkbox_val)
##
# prev, _ ,next = st.columns([1, 10, 1])
# st.write("Outside the form")


# if output_size == 'To-the-point':
#     out_token = 50 
# elif output_size == 'concise':
#     out_token = 128 
# else:
#     out_token = 516 

# if st.button('Get answer', type='primary'):

#     response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Please answer this question: " + article_text,
#   temperature=0.5,
#   max_tokens=516,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0,
# )
#     res = response['choices'][0]['text']
#     st.success(res)
#     st.download_button('Download result', res)

    # print(response)
