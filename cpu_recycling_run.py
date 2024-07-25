import argparse
from cpu_recycling import run
import gradio as gr

# UI using Gradio
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=2):
            cameraPic = gr.Image(value=None, sources=["upload", "clipboard", "webcam"], type="filepath", show_label=False, interactive=True, show_download_button=False)
    with gr.Row():
        txtModelOutput = gr.Textbox(label="AI-generated output", lines=6)
    
    cameraPic.upload(fn=run, inputs=cameraPic, outputs=txtModelOutput)

demo.launch()
