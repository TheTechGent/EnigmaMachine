# 🛡️ Enigma Machine Web App

A modern, web-based recreation of the historic Enigma Machine using Python, FastAPI, and vanilla JavaScript. This project demonstrates full-stack development, web deployment, and test-driven engineering.

---

## 🚀 Live Demo

Hosted entirely on [Railway](https://railway.app):  
**Frontend + Backend**: [Enigma Machine](https://www.thetechgent.co.uk)

---

## 🧠 Project Overview

This app simulates the encryption behavior of the WWII-era Enigma 1 Machine. It features:

- A fully functional Enigma engine written in Python
- A FastAPI backend exposing encryption via REST API
- A lightweight frontend using HTML, CSS, and JavaScript
- CSS-based animations to mimic rotor spins and lampboard glow
- Deployment to Railway for hosting

---

## 🧱 Architecture

| Layer       | Tech Stack                     | Purpose                          |
|-------------|--------------------------------|----------------------------------|
| Frontend    | HTML, CSS, JavaScript          | User interface and interaction   |
| Backend     | Python, FastAPI                | Encryption logic and API         |
| Hosting     | Railway                        | Unified hosting for full-stack app|

---

## 🧪 Testing & Coverage

- Unit tests written using `pytest`
- API tests using FastAPI’s `TestClient`
- Coverage reports via `pytest-cov`
- Front end testing `jest`

```bash
pytest --cov=app/enigma
```

---

## 📦 Deployment Strategy

### Continuous Deployment with Railway PaaS

- **Git-Ops Workflow**: Automatic deployment triggered by pushes to `main` branch
- **Platform**: Railway as Platform-as-a-Service (no Docker configuration required)
- **Build System**: NIXPACKS auto-detects Python project and installs dependencies
- **Architecture**: Single FastAPI service serves both API endpoints and static frontend files
- **Health Monitoring**: Zero-downtime deployments with `/health` endpoint validation
- **Environment**: Containerized deployment managed entirely by Railway's infrastructure

**Configuration:**

- `railway.toml` defines build and deployment settings
- `requirements.txt` specifies Python dependencies
- Static files served via FastAPI's `StaticFiles` middleware
- Automatic port binding via Railway's `$PORT` environment variable

---

## 📁 Folder Structure

```plaintext
EnigmaMachine/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app + basic routing only
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py           # Your API endpoints
│   │   └── models.py           # Pydantic models
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py           # Configuration settings
│   ├── enigma/                 # Your existing Enigma logic
│   │   ├── __init__.py
│   │   └── configuration.py    # Enums for rotor and reflector wiring
│   │   └── keyboard.py         # Handles text input
│   │   └── machine.py          # Initialises components to encipher and decipher
│   │   └── plugboard.py        # Handles swapping of letters
│   │   └── reflector.py        # Handles signal bounce back
│   │   └── rotor.py            # Handles rotor setup and stepping
│   └── services/
│       ├── __init__.py
│       └── enigma_service.py   # Business logic layer
├── static/                     # Move to root for Railway
│   ├── index.html
│   ├── style.css
│   └── script.js
├── tests/
│   ├── __init__.py
│   ├── backend/
│   │   ├── test_api.py
│   │   ├── test_encipher.py
│   │   └── test_rotor_stepping.py
│   └── frontend/
│       └── glowlamp.test.js
├── requirements.txt
├── requirements-dev.txt
├── railway.toml
└── README.md
```

---

## 🔮 Future Enhancements

This project is a work in progress. There are features I want to add:

- **Mobile Responsiveness**  
  Refactor the frontend layout and animations to support mobile devices and touch interaction. This includes responsive scaling of rotors, keys, and lampboard, as well as optimizing input methods for smaller screens.

- **Rotor Reversal on Message Deletion**  
  Implement logic to reverse rotor steps when characters are deleted, maintaining historical accuracy and enabling true bidirectional encryption. This will allow users to backspace through a message and preserve rotor state integrity.

- **Enhanced 2D/3D Visualization**  
  Improve the frontend experience by exploring both 2D and 3D representations of the Enigma Machine. For 3D, I will experiment with libraries like Three.js. For 2D, the focus will be on refining layout, interactivity, and visual clarity — using SVG, CSS transitions, and canvas-based rendering to simulate mechanical motion and feedback. This would include smoother rotor animations, dynamic plugboard mapping, and responsive lampboard glow. The goal is to create an immersive, historically inspired interface. At present I do not know how to acheive this so to loosely quote Anthony Hopkins in The Mask of Zorro "as my skill with code improves, I will progress to a smaller circle. With each new circle, my world contracts, bringing me that much closer to this goal, that much closer to mastery."

---

## 🧩 Other Implementations

Python was my first implementation of the Enigma machine but this was originally to deepen my understanding of its encipher mechanics, and how I would design and write its architecture to break down and explain to one of my students. After this I created two other versions:

- **C++ Console Version**  
  This was to improve my knowledge and ability to write pure C++ without external frameworks, as my only experience had been in Unreal for game development. At present it is a console application and has more features than this full-stack web version - I have almost finished the 'Rotor Reversal on Message Deletion.' Next steps with this project is to make it into a cross-platform desktop app and this is to give me a project to learn qt. Something I hope to get round to at some point.
  → [View on GitHub](https://github.com/TheTechGent/C_nigmaMachine_PlusPlus)

- **Unreal Engine Blueprint Version**  
  This version was to demonstrate to the student that sparked this passion project how they could approach it. It was for their game so recreating it in Unreal was the end goal.

These implementations complement the Python web app by showcasing cross-disciplinary fluency in systems programming, game development, and full-stack architecture.

---

## TO DO

- Fix: frontend text field not displaying encrypted message.
- Fix: frontend lampboard not lighting up encypted letter.
- Feature: add interactive plugboard to set letter swap.
- Feature: backspace deletes previously entered letter and reverses the rotor step
- Refactor: Work on edge cases - punctuation, non-alpha characters.
- Refactor: Clean up code.
  