# motion-cue-2.0

# Motion Cue

Motion Cue is a vision-based project that incorporates three main services:
1. Gesture Presentation
2. Helmet Guardian
3. Virtual Mouse

Each service is designed to leverage computer vision for different applications, using Python and Streamlit.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

### Gesture Presentation
A tool that uses computer vision to recognize and interpret hand gestures for controlling presentations.

### Helmet Guardian
A safety application that detects whether a person is wearing a helmet, primarily aimed at promoting workplace safety.

### Virtual Mouse
A computer vision-based virtual mouse that allows users to control their computer cursor using hand movements.

## Features
- **Gesture Presentation**: Control presentations using simple hand gestures.
- **Helmet Guardian**: Real-time helmet detection to ensure safety compliance.
- **Virtual Mouse**: Hands-free computer interaction with a virtual mouse controlled by hand gestures.

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.11.7 (for Gesture Presentation and Helmet Guardian)
- Python 3.7.9 (for Virtual Mouse)
- Streamlit

### Clone the Repository
```bash
git clone https://github.com/your-username/motion-cue.git
cd motion-cue
```

### Install Dependencies
For Gesture Presentation and Helmet Guardian:
```bash
pip install -r requirements_3.11.7.txt
```

For Virtual Mouse:
```bash
pip install -r requirements_3.7.9.txt
```

## Usage

### Gesture Presentation
1. Navigate to the Gesture Presentation directory:
   ```bash
   cd gesture_presentation
   ```
2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

### Helmet Guardian
1. Navigate to the Helmet Guardian directory:
   ```bash
   cd helmet_guardian
   ```
2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

### Virtual Mouse
1. Ensure you are using Python 3.7.9.
2. Navigate to the Virtual Mouse directory:
   ```bash
   cd virtual_mouse
   ```
3. Run the application:
   ```bash
   python virtual_mouse.py
   ```

## Contributing
Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add Some Feature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance!

Happy Coding!


