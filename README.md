# MindFlow

## Summary

MindFlow is an innovative AI architecture inspired by a psychological model of nine modes of activity. This architecture is designed to emulate human-like processing by structuring an artificial agent into modular services, including sensation, cognition, emotion, memory, and holisitic synthesis. By integrating these components, MindFlow aims to achieve a balanced and holistic approach to artificial intelligence, enabling agents to not only emulation perception and cognition but also to reflect and synthesize those perceptions and outputs of cognition.

## Main Architecture

MindFlow's architecture is divided into several key modules, each responsible for a different aspect of the AI's processing capabilities:

- **Sensation Module**: Handles the perception of external stimuli, acting as the interface between the agent and its environment.
- **Cognition Module**: Processes the information gathered by the sensation module, enabling the agent to make sense of its surroundings.
- **Emotion Module**: Generates emulated emotional responses based on the processed information, adding a layer of human-like reactivity and decision-making.
- **Memory Module**: Stores "experiences" and information, allowing the agent to learn from past actions and to adapt its behavior over time.
- **Holistic Module**: Integrates the outputs from all other modules, facilitating self-reflection and the application of learned knowledge to new situations.

These modules work in concert to create an AI agent capable of complex behaviors and decision-making processes that mirror human psychological processes.

## Setup and Usage

To set up and start using MindFlow in your projects, follow these steps:

1. **Clone the Repository**: First, clone the MindFlow repository to your local machine using Git:

```bash
git clone https://github.com/jpwinans/MindFlow.git
```

2. **Install Dependencies**: Navigate to the cloned repository's directory and install the necessary dependencies:

```bash
cd MindFlow
# Install dependencies here, e.g., using pip for Python projects
pip install -r requirements.txt
```

3. **Configuration**: create `.anthropic_key` file in base folder with your Antropic key. (MindFlow is currently using Claude v2 to power the Mental Service and language faculties.)

4. **Running MindFlow**: 

```bash
chainlit run mindflow/chat.py -w
```

## Contributing

We welcome contributions to MindFlow! If you have suggestions for improvements or bug fixes, please feel free to fork the repository, make your changes, and submit a pull request.
