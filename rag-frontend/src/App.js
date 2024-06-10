import React, { useState } from 'react';

import './App.css';

function App() {
    const [query, setQuery] = useState('');
    const [response, setResponse] = useState('');
    const [reset, setReset] = useState(false);
    const [dataDir, setDataDir] = useState('');
    const [conversation, setConversation] = useState([]); // State for conversation history
    const [isLoading, setIsLoading] = useState(false); // State for loading animation

    const handleQueryChange = (e) => {
        setQuery(e.target.value);
    };

    const handleDataDirChange = (e) => {
        setDataDir(e.target.value);
    };

    const handleSubmitQuery = async () => {
        setIsLoading(true); // Start loading animation
        try {
            const res = await fetch('http://localhost:5001/query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ query, conversation }) // Send the conversation history
            });
            const data = await res.json();
            const botResponse = data.response;
            setResponse(botResponse);
            setConversation(prev => [...prev, { sender: 'user', text: query }, { sender: 'llm', text: botResponse }]);
        } catch (error) {
            console.error(error);
            setResponse('Error querying the database.');
        }
        setIsLoading(false); // Stop loading animation
    };

    const handleUpdateDatabase = async () => {
        setIsLoading(true); // Start loading animation
        try {
            const res = await fetch('http://localhost:5001/update-database', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ reset })
            });
            const data = await res.json();
            setResponse(data.message);
        } catch (error) {
            console.error(error);
            setResponse('Error updating the database.');
        }
        setIsLoading(false); // Stop loading animation
    };

    const handleSetDataDir = async () => {
        setIsLoading(true); // Start loading animation
        try {
            const res = await fetch('http://localhost:5001/set-data-dir', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ data_dir: dataDir })
            });
            const data = await res.json();
            setResponse(data.message);
        } catch (error) {
            console.error(error);
            setResponse('Error setting data directory.');
        }
        setIsLoading(false); // Stop loading animation
    };

    return (
        <div className="App">
            <h1>RAG for local files</h1>
            <div>
                <label>
                    Data Directory:
                    <input type="text" value={dataDir} onChange={handleDataDirChange} />
                </label>
                <button onClick={handleSetDataDir}>Set Data Directory</button>
            </div>
            <div>
                <label>
                    Query:
                    <input type="text" value={query} onChange={handleQueryChange} />
                </label>
                <button onClick={handleSubmitQuery}>Submit Query</button>
            </div>
            <div>
                <label>
                    <input
                        type="checkbox"
                        checked={reset}
                        onChange={() => setReset(!reset)}
                    />
                    Reset Database
                </label>
                <button onClick={handleUpdateDatabase}>Update Database</button>
            </div>
            <div>
                <h2>Response:</h2>
                {isLoading ? (
                     <img src="/logo192.png" className="spinner" alt="Loading..." />
                ) : (
                    <pre>{response}</pre>
                )}
            </div>
            <div>
                <h2>Conversation History:</h2>
                {conversation.map((msg, index) => (
                    <div key={index} className={msg.sender === 'user' ? 'user-message' : 'bot-message'}>
                        <strong>{msg.sender}:</strong> {msg.text}
                    </div>
                ))}
            </div>
        </div>
    );
}

export default App;
