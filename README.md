# CPU-Powered AI Tutor

## Overview

**CPU-Powered AI Tutor** is a project that enables real-time, interactive tutoring using the **Llama-2 7B Chat** model, optimized to run on a CPU. This intelligent AI tutor can answer questions, explain concepts step-by-step, and adapt its responses based on the user's level of understanding, all while running efficiently on a CPU.

The project leverages **Gradio** for the user interface and **ctransformers** for loading and running the Llama-2 model. It allows users to engage with the model through a simple chat interface, making it ideal for educational use cases.

---

### Features

- **CPU-Friendly:** Run a large-scale AI model (Llama-2 7B Chat) on a CPU without needing a GPU.
- **Real-Time Interaction:** Get instant responses, with step-by-step explanations and examples.
- **Interactive Tutor:** The AI adapts its explanations to suit the user's knowledge level and needs.
- **Gradio Interface:** An intuitive, easy-to-use chat interface for seamless interaction.

---

### Project Structure

```plaintext
llama-2-7b-chat.ggmlv3.q3_K_L.bin  # Pre-trained model file for Llama-2 7B
llamaCPU.py                        # Python script that powers the interaction
requirements.txt                   # Python dependencies
```

---
### Screenshot

![Screenshot 1]()

---

### Installation

##### Prerequisites

Before running the project, ensure you have the following installed:

```plaintext
Python 3.x
Pip (Python package installer)
```

##### Steps to Install

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Mangaleshwaran2002/CPU-Powered-AI-Tutor.git
cd CPU-Powered-AI-Tutor
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Download the Llama-2 7B Chat model file (llama-2-7b-chat.ggmlv3.q3_K_L.bin) from the official source (or if you already have it, place it in the project folder).
---
##### Running the Application

1. After the dependencies are installed and the model file is downloaded, run the following command:

```bash
python llamaCPU.py
```

2. The application will launch a Gradio interface in your terminal, with a link to access the chat interface in your browser. Once opened, you can start interacting with the AI tutor.
---

## Author
Created by K.Mangaleshwaran on **March 13, 2025**.