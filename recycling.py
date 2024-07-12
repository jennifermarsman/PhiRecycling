import gradio as gr
import phi_helper as phi3v

prompt = "Is this recyclable?  Plastics and cardboard may be recycled.  Please answer 'YES, RECYCLABLE' or 'NO, TRASH'.  "
## NOTE: You may adjust the prompt for the recycling guidelines in your area.  See the exammple below.  
#prompt = "Plastics and cardboard may be recycled.  Anything with a recycling symbol may be recycled.  Styrofoam may not be recycled.  Aerosol cans may not be recycled.  \n\nFocus on the item in the person's hand.  Is this recyclable?  Please answer 'YES, RECYCLABLE' or 'NO, TRASH'.  "

def phi3v_wrapper(cameraPicPath):
    out = phi3v.call_with_single_local_image(cameraPicPath, prompt)
    return out

def set_image(txtModelOutput):
    output = txtModelOutput.replace(prompt, "", 1)
    print("Output is: " + output)
    if "YES" in output.upper():
        # Recycle! 
        print("Entered recycle")
        outputPic = "triangular-arrows-sign-for-recycle.png"
    elif "NO" in output.upper():
        # Trash!  
        print("Entered trash")
        outputPic = "bin.png"
    else:
        # Uh-oh!  What to do here? 
        print("Neither option selected")
        outputPic = "bin.png"   # Default so there is always something during debugging
    return outputPic


# UI using Gradio
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=2):
            cameraPic = gr.Image(value=None, sources=["upload", "clipboard", "webcam"], type="filepath", show_label=False, interactive=True, show_download_button=False)
        with gr.Column(scale=1):
            outputPic = gr.Image(value=None, sources=[], type="filepath", show_label=False, interactive=False, show_download_button=False)
    with gr.Row():
        txtModelOutput = gr.Textbox(label = "AI-generated output", lines=6)

    cameraPic.upload(fn=phi3v_wrapper, inputs=cameraPic, outputs=txtModelOutput)
    txtModelOutput.change(fn=set_image, inputs=txtModelOutput, outputs=outputPic)

demo.launch()
