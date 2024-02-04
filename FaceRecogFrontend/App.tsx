import React, { useState, useEffect } from "react";
import "./App.css";
import initialImage from "./images/mysteryMan.png";
import hetImage from "./images/het.png";
import virenImage from "./images/viren.png";
import nolanImage from "./images/nolan.png";
import eiqanImage from "./images/eiqan.png";

import data from "./texts/finalText.json"; // Import your JSON data

function App() {
  const [imageSrc, setImageSrc] = useState(initialImage);
  const [text, setText] = useState("No suspect found");
  const [location, setLocation] = useState(""); // State variable for location
  const [hardcodedId, setHardcodedId] = useState(0); // Initial ID
  const [currentTime, setCurrentTime] = useState(
    new Date().toLocaleTimeString()
  );

  useEffect(() => {
    const timerId = setInterval(() => {
      setCurrentTime(new Date().toLocaleTimeString());
    }, 4500);

    return () => clearInterval(timerId);
  }, []);

  useEffect(() => {
    const timer = setTimeout(() => {
      setHardcodedId(0); // Change to the desired ID for hardcoded data
    }, 2000); // Wait for 2 seconds before switching

    return () => clearTimeout(timer); // Clear the timer on component unmount
  }, []);

  useEffect(() => {
    const currentData = data.find((item) => item.id === hardcodedId);
    if (currentData) {
      setText(currentData.Name);
      setLocation(currentData.Location || "Location not available"); // Set location

      switch (currentData.Name) {
        case "Het":
          setImageSrc(hetImage);
          break;
        case "Viren":
          setImageSrc(virenImage);
          break;
        case "Nolan":
          setImageSrc(nolanImage);
          break;
        case "Eiqan":
          setImageSrc(eiqanImage);
          break;
        default:
          setImageSrc(initialImage);
          break;
      }
    }
  }, [hardcodedId]);

  return (
    <div className="app">
      <div className="current-time">
        <span className="time-label">Time:</span> {currentTime}
      </div>

      <div className="image-display">
        <h1 className="text">Suspect: {text}</h1>
        <h2 className="location">Location: {location}</h2>
        <img src={imageSrc} alt={text} className="image" />
      </div>
    </div>
  );
}

export default App;
