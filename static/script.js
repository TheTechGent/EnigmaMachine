class EnigmaMachineUI {
  constructor() {
    this.inputMessage = document.getElementById("input-message");
    this.outputMessage = document.getElementById("output-message");
    this.reflector = document.getElementById("reflector");
    this.rotor1 = document.getElementById("rotor1");
    this.rotor2 = document.getElementById("rotor2");
    this.rotor3 = document.getElementById("rotor3");

    this.initEventListeners();
  }

  initEventListeners() {
    this.inputMessage.addEventListener("input", this.handleInput.bind(this));

    [this.reflector, this.rotor1, this.rotor2, this.rotor3].forEach(
      (configChange) => {
        configChange.addEventListener(
          "change",
          this.encipherCurrentMessage.bind(this)
        );
      }
    );
  }

  async handleInput(event) {
    const message = event.target.value;
    await this.encipherMessage(message);
  }

  async encipherMessage() {
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
      const response = await fetch("/api/encipher", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(config),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      this.outputMessage.value = result.encrypted_message;

      // lamp lights up corresponding letter.
      if (result.encrypted_message) {
        const lastChar = result.encrypted_message.slice(-1);
        this.glowLamp(lastChar);
      }
    } catch (error) {
      console.error("Encryption error", error);
      this.outputMessage.value = "Error: Could not encipher message";
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
  new EnigmaUI();
});
