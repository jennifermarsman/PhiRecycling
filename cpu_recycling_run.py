import argparse
from cpu_recycling import run
import gradio as gr

def classify_image(image):
    # Run the classification
    result = run(image)
    
    # Determine the output image based on the result
    if 'YES' in result:
        output_image = 'triangular-arrows-sign-for-recycle.png'
    else:
        output_image = 'bin.png'
    
    return result, output_image

# UI using Gradio
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=2):
            cameraPic = gr.Image(value=None, sources=["upload", "clipboard", "webcam"], type="filepath", show_label=False, interactive=True, show_download_button=False)
        with gr.Column(scale=1):
            outputPic = gr.Image(value=None, sources=[], type="filepath", show_label=False, interactive=False, show_download_button=False)
    with gr.Row():
        txtModelOutput = gr.Textbox(label="AI-generated output", lines=6)
    
    # Call the classify_image function and display both the text and image outputs
    cameraPic.upload(fn=classify_image, inputs=cameraPic, outputs=[txtModelOutput, outputPic])

demo.launch()
