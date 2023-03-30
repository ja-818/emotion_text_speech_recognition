import gradio as gr
from models import infere_speech_emotion, infere_text_emotion, infere_voice2text

with gr.Blocks() as demo:
    gr.HTML('''
        <h1 style="text-align:center;">holi</h1>
        <h2 style="text-align:center;">Instrucciones</h2>
        <br>
        ''')
    with gr.Row():
        input = gr.Audio(label="Audio File", type="filepath")
        with gr.Column():
            output0 = gr.Textbox(label="Text from the audio")
            output1 = gr.Textbox(label="Speech emotion")
            output2 = gr.Textbox(label="Text emotion")
    btn = gr.Button("Analyze the audio!")   
        
    btn.click(fn=infere_voice2text, inputs=input, outputs=output0)
    btn.click(fn=infere_speech_emotion, inputs=input, outputs=output1)
    output0.change(fn=infere_text_emotion, inputs=output0, outputs=output2)

demo.launch()