import os
import google.generativeai as genai

genai.configure(api_key='AIzaSyA3iv5hn37rcUDG81McIOgyqEJMJQFVwAY')


# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  # "max_output_tokens": 200,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Please provide a detailed, expert-level answer to the following question. Ensure clarity and accuracy by explaining any technical terms, using examples or code snippets where applicable. Be concise yet thorough, highlighting key concepts. Respond in a way that avoids ambiguity and gives actionable insights or solutions.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Please provide me with the question you'd like me to answer. I'm ready to provide a detailed, expert-level response!  \n\nTo ensure I can give you the most accurate and helpful answer, please be as specific as possible with your question.  \n\nFor example, instead of \"Explain machine learning,\" you could ask:\n\n* \"Can you explain the difference between supervised and unsupervised learning in machine learning? Give some examples of each type.\"\n* \"What are the key steps involved in training a deep learning model for image classification?\"\n* \"What are some common challenges faced when working with time series data in machine learning?\"\n\nThe more context you give me, the better I can understand your needs and provide a comprehensive answer. \n",
      ],
    },
  ]
)

response = chat_session.send_message("tell me about pca in short 200 tokens")

print(response.text)



##################################33
AIzaSyAjPgOnz-Uk0Js84e9U_4usHen5jEeUqhg
export GEMINI_API_KEY="AIzaSyAjPgOnz-Uk0Js84e9U_4usHen5jEeUqhg"
# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-pro-preview-03-25"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
