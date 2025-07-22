import { useState } from "react";

function App() {
  const [pdfName, setPdfName] = useState(null);
  const [pdfText, setPdfText] = useState(null);
  const [chat, setChat] = useState([
    {
      role: "system",
      text: "Hi, I am your AI Education Agent. Please upload a PDF book so I can assist you.",
    },
  ]);
  const [userInput, setUserInput] = useState("");
  const [isRecording, setIsRecording] = useState(false);
  const [lastAIResponse, setLastAIResponse] = useState("");
  const [selectedLanguage, setSelectedLanguage] = useState("en-US");

  const languageOptions = [
    { code: "en-US", label: "English" },
    { code: "hi-IN", label: "Hindi" },
    { code: "mr-IN", label: "Marathi" },
    { code: "ar-SA", label: "Arabic" },
  ];

  function startVoiceInput() {
    const recognition =
      new window.webkitSpeechRecognition() || new window.SpeechRecognition();
    recognition.continuous = false;
    recognition.lang = selectedLanguage;
    recognition.interimResults = false;

    setIsRecording(true);

    recognition.onresult = function (event) {
      const transcript = event.results[0][0].transcript;
      setUserInput(transcript);
      setIsRecording(false);
    };

    recognition.onerror = function () {
      alert("Speech recognition failed or was blocked.");
      setIsRecording(false);
    };

    recognition.onend = () => setIsRecording(false);

    recognition.start();
  }

  function speak(text) {
    if ("speechSynthesis" in window && text) {
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = selectedLanguage;
      window.speechSynthesis.speak(utterance);
    }
  }

  async function handleFileChange(e) {
    const file = e.target.files[0];
    if (!file) return;

    setPdfName(file.name);

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://localhost:8000/upload-pdf/", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setPdfText(data.full_text);
    setChat((prev) => [
      ...prev,
      {
        role: "system",
        text: `✅ PDF received: ${data.filename}`,
      },
    ]);
  }

  async function handleAsk() {
    if (!userInput || !pdfText) return;

    const userQuestion = userInput;
    setChat((prev) => [...prev, { role: "user", text: userQuestion }]);
    setUserInput("");

    const res = await fetch("http://localhost:8000/ask/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question: userQuestion,
        context: pdfText,
        language: selectedLanguage,
      }),
    });

    const data = await res.json();
    const aiResponse = data.answer || data.error || "❌ No response from AI";

    setChat((prev) => [...prev, { role: "ai", text: aiResponse }]);
    setLastAIResponse(aiResponse);
  }

  return (
    <div className="min-h-screen bg-black flex flex-col items-center">
      {/* Fixed Top Banner */}
      <div className="w-full bg-gray-800 text-white py-3 text-center text-3xl font-semibold fixed top-0 shadow z-10">
        Multilingual AI Assistant
      </div>

      {/* Main chat box with padding to clear fixed header */}
      <div className="mt-20 max-w-full w-[95%] sm:w-[90%] lg:w-[85%] xl:w-[80%] bg-black rounded-lg p-8 space-y-6">

        {/* Chat Display */}
        {chat.map((msg, idx) => (
          <div
            key={idx}
            className={`rounded-xl px-6 py-4 max-w-[80%] whitespace-pre-wrap animate-fade-in ${
              msg.role === "user"
                ? "bg-white text-black self-end ml-auto text-lg"
                : msg.role === "ai"
                ? "bg-gray-700 text-white self-start mr-auto text-lg"
                : "bg-gray-700 text-white self-start mr-auto text-lg"
            }`}
          >
            {msg.text}
          </div>
        ))}

        {/* File Upload */}
        <input
          type="file"
          accept="application/pdf"
          onChange={handleFileChange}
          className="block w-full text-sm text-black bg-white border border-white rounded-xl px-6 py-4 cursor-pointer"
        />

        {/* Controls */}
        {pdfText && (
          <>
            <div className="flex flex-col sm:flex-row gap-4 items-center justify-between">
              {/* Language Selector */}
              <select
                value={selectedLanguage}
                onChange={(e) => setSelectedLanguage(e.target.value)}
                className="text-black bg-white border border-white rounded-xl p-4 text-lg w-full sm:w-64"
              >
                {languageOptions.map((lang) => (
                  <option key={lang.code} value={lang.code}>
                    {lang.label}
                  </option>
                ))}
              </select>

              <div className="flex gap-4 w-full sm:w-auto">
                <input
                  type="text"
                  value={userInput}
                  onChange={(e) => setUserInput(e.target.value)}
                  placeholder="Ask a question..."
                  className="flex-1 p-4 border border-white text-black rounded-xl bg-white text-xl"
                />
                <button
                  onClick={startVoiceInput}
                  className="bg-white text-black rounded-xl px-6 py-4 hover:bg-gray-100"
                  title="Voice input"
                >
                  🎤
                </button>
                <button
                  onClick={handleAsk}
                  className="bg-white text-black px-6 py-4 rounded-xl hover:bg-gray-100"
                >
                  Ask
                </button>
                <button
                  onClick={() => speak(lastAIResponse)}
                  className="bg-white text-black px-6 py-4 rounded-xl hover:bg-gray-100"
                  title="Play last AI response"
                >
                  🔊
                </button>
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
}

export default App;
