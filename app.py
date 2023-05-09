# from fastai.vision.all import *
# import gradio as gr

# learn = load_learner('model.pkl')

# categories = 'Sunflower', 'Orchid', 'Rose'

# def classify_image(img):
#     pred, idx, probs = learn.predict(img)
#     return(dict(zip(categories, map(float, probs))))

# image = gr.inputs.Image(shape=(192,192))
# label = gr.outputs.label()
# examples = ['sunflower.jpeg', 'orchid.jpeg', 'rose.jpeg']

# intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
# intf.launch(inline=False, share=True)

from fastai.vision.all import *
import gradio as gr

# Load the pre-trained model
learn = load_learner('model.pkl')

# Define the categories that the model can classify
categories = ['Sunflower', 'Orchid', 'Rose']

# Define the function to classify an image and return the predicted category label
def classify_image(img):
    pred, idx, probs = learn.predict(img)
    return categories[idx]

# Define the input and output types for the Gradio interface
image_input = gr.inputs.Image(shape=(224, 224))
label_output = gr.outputs.Label()

# Define example images for the interface
examples = [
    ['sunflower.jpeg'],
    ['orchid.jpeg'],
    ['rose.jpeg']
]

# Create the Gradio interface
interface = gr.Interface(
    fn=classify_image, 
    inputs=image_input, 
    outputs=label_output,
    examples=examples,
    title="Image Classifier",
    description="This app classifies images into three categories: Sunflower, Orchid, and Rose."
)

# Launch the interface
interface.launch()
