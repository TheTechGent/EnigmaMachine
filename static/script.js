class EnigmaMachineUI {
  constructor() {
    this.inputMessage = document.getElementById("input-message");
    this.outputMessage = document.getElementById("output-message");
    this.reflector = document.getElementById("reflector");
    this.rotor1 = document.getElementById("rotor1");
    this.rotor2 = document.getElementById("rotor2");
    this.rotor3 = document.getElementById("rotor3");

    // Check if all elements were found
    console.log("Elements found:", {
      inputMessage: !!this.inputMessage,
      outputMessage: !!this.outputMessage,
      reflector: !!this.reflector,
      rotor1: !!this.rotor1,
      rotor2: !!this.rotor2,
      rotor3: !!this.rotor3,
    });

    this.initEventListeners();
  }

  initEventListeners() {
    this.inputMessage.addEventListener("input", this.handleInput.bind(this));

    [this.reflector, this.rotor1, this.rotor2, this.rotor3].forEach(
      (configChange) => {
        configChange.addEventListener("change", (event) => {
          console.log(
            "Configuration changed:",
            event.target.id,
            event.target.value
          );
          this.encryptCurrentMessage();
        });
      }
    );
  }

  async handleInput(event) {
    const message = event.target.value;
    console.log("Input detected:", message);
    await this.encryptMessage(message);
  }

  async encryptMessage(message) {
    if (!message.trim()) {
      this.outputMessage.value = "";
      return;
    }

    const config = {
      message: message,
      rotor1: this.rotor1.value,
      rotor2: this.rotor2.value,
      rotor3: this.rotor3.value,
      reflector: this.reflector.value,
      position: "AAA",
      rings: [1, 1, 1],
      plugboard: [],
    };

    try {
      console.log("Sending POST request to /api/encrypt with config:", config);

      const response = await fetch("/api/encrypt", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(config),
      });

      console.log("Response received:", response);

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      console.log("Encrypted message received:", result);
      this.outputMessage.value = result.encrypted_message;

      if (result.encrypted_message) {
        const lastChar = result.encrypted_message.slice(-1);
        this.glowLamp(lastChar);
      }
    } catch (error) {
      console.error("Encryption error:", error);
      this.outputMessage.value = "Error: Could not encrypt message";
    }
  }

  glowLamp(letter) {
    // Remove previous glow
    document.querySelectorAll(".lamp.active").forEach((lamp) => {
      lamp.classList.remove("active");
    });

    // Add glow to current letter
    const lamp = document.getElementById(`lamp-${letter}`);
    if (lamp) {
      lamp.classList.add("active");
      setTimeout(() => {
        lamp.classList.remove("active");
      }, 1000);
    }
  }

  async encryptCurrentMessage() {
    await this.encryptMessage(this.inputMessage.value);
  }
}

// Initialize the UI when the page loads
document.addEventListener("DOMContentLoaded", () => {
  new EnigmaMachineUI();
});
