body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: linear-gradient(135deg, #f8fafc, #eef2ff);
  color: #0f172a;
}

.app-shell {
  display: flex;
  min-height: 100vh;
}

.sidebar {
  width: 280px;
  background: #0f172a;
  color: white;
  padding: 24px;
}

.sidebar h2 {
  margin-top: 0;
}

.sidebar button {
  display: block;
  width: 100%;
  margin: 12px 0;
  padding: 10px 14px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  background: #8b5cf6;
  color: white;
}

.main-panel {
  flex: 1;
  padding: 24px;
}

.chat-window {
  height: 70vh;
  overflow-y: auto;
  background: rgba(255,255,255,0.7);
  border: 1px solid #e2e8f0;
  border-radius: 18px;
  padding: 20px;
  margin-bottom: 16px;
}

.message {
  max-width: 75%;
  padding: 12px 16px;
  border-radius: 16px;
  margin-bottom: 12px;
  line-height: 1.6;
}

.message.user {
  margin-left: auto;
  background: #8b5cf6;
  color: white;
}

.message.assistant {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
}

.composer {
  display: flex;
  gap: 12px;
}

textarea {
  width: 100%;
  border: 1px solid #cbd5e1;
  border-radius: 12px;
  padding: 12px;
  resize: vertical;
}

button#sendBtn {
  background: #2563eb;
  color: white;
  border: none;
  border-radius: 12px;
  padding: 12px 20px;
  cursor: pointer;
}
