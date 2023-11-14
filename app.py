import gradio as gr
from bs4 import BeautifulSoup
def html_to_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    return text


css = """
#warning {background-color: #FFCCCB}
.feedback textarea {font-size: 24px !important}
.gradio-container {background-color: red}
"""
with gr.Blocks(css=css) as demo:
    
    box1 = gr.Textbox(value="公众号:正经人王同学", elem_classes="feedback")
    box2 = gr.Textbox(value="html转文本小工具", elem_id="warning", elem_classes="feedback")


    input = gr.Textbox(label="HTML",lines=15)
    output = gr.Textbox(label="文本输出")
    submit = gr.Button()
    # submit.click(html_to_text,inputs,outputs)
    submit.click(html_to_text,inputs=input,outputs=output)
demo.launch()
